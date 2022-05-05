from typing import Tuple
from inputs import get_gamepad

from threading import Thread
import datetime as dt
from time import sleep, time
import os

from api import LastControllerInputApi

LAST_CONTROLLER_INPUT_SET_DELAY = 2
_CONTROLLER_URL_ENV = "FT_CONTROLLER_URL"
CONTROLLER_URL = (
    os.environ[_CONTROLLER_URL_ENV]
    if _CONTROLLER_URL_ENV in os.environ
    else "http://localhost:8000"
)


class LastControllerInput:
    def __init__(self):
        self._api = LastControllerInputApi(CONTROLLER_URL)
        self.last_interaction = [int(time() * 1000), False]
        self.holding = {}

        # threads for getting the inputs and posting the latest input
        get_input_loop_thread = Thread(target=self.get_input_loop, daemon=True)
        set_last_input_loop_thread = Thread(
            target=self.update_last_input_loop, daemon=True
        )
        # get_input_loop_thread.setDaemon(True)
        # set_last_input_loop_thread.setDaemon(True)
        get_input_loop_thread.start()
        set_last_input_loop_thread.start()
        while True:
            pass

    # pulls inputs from the controller
    def get_input_loop(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.ev_type == "Key":
                    # binary inputs (buttons, bumpers, etc.)
                    self.holding[event.code] = True if event.state == 1 else False
                if event.code[0:3] == "ABS":
                    if event.code[4:7] == "HAT":
                        # d-pad
                        self.holding[event.code] = (
                            True if abs(event.state) == 1 else False
                        )
                    elif "Z" in str(event.code[4:6]):
                        # triggers
                        self.holding[event.code] = True if event.state > 10 else False
                    else:  # ABS_X or ABS_Y
                        # left/right stick
                        if abs(event.state) > 12000:
                            self.holding[event.code] = True
                        else:
                            self.holding[event.code] = False

                self.last_interaction = [
                    int(event.timestamp * 1000),
                    self.is_held(),
                ]

    def is_held(self):
        # what happens with multiple controllers?
        # for sticks: add 1 when something being held, subtract one when no longer being held
        # for buttons: add 1 to general total?

        # for everything?? just have a general total and return true when not 0, false when 0

        return True in self.holding.values()

    # periodically sets the last input through the api
    def update_last_input_loop(self):
        while True:
            sleep(LAST_CONTROLLER_INPUT_SET_DELAY)
            self._api.set_last_input(self.last_interaction)


test = LastControllerInput()

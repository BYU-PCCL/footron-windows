from typing import Tuple
from xinput import get_gamepad
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
        self.holding = [{} for _ in range(4)]  # 4 controllers

        # threads for getting the inputs and posting the latest input
        get_input_loop_thread = Thread(target=self.get_input_loop, daemon=True)
        set_last_input_loop_thread = Thread(
            target=self.update_last_input_loop, daemon=True
        )
        # get_input_loop_thread.setDaemon(True)
        # set_last_input_loop_thread.setDaemon(True)
        get_input_loop_thread.start()
        set_last_input_loop_thread.start()
        self.gamepads = None
        while True:
            pass

    # pulls inputs from the controller
    def get_input_loop(self):
        while True:
            events = get_events()
            for event in events:
                last_input_time = datetime.now()
                # print(event)
                if event.type == 2:
                    holding[event.user_index] = {}
                elif hasattr(event, "button"):
                    if event.button == "GUIDE":
                        print("guide")
                    else:
                        holding[event.user_index][event.button] = (
                            True if event.type == 3 else False
                        )
                elif hasattr(event, "trigger"):
                    holding[event.user_index]["trigger" + str(event.trigger)] = (
                        True if event.value >= 0.001 else False
                    )
                elif hasattr(event, "stick"):
                    holding[event.user_index]["stick" + str(event.stick)] = (
                        True if event.value >= 0.01 else False
                    )
                # elif hasattr(event, "stick"):
                #     holding[event.user_index]["stick" + str(event.stick)] = (
                #         True if (abs(event.x) >= 0.025 or abs(event.y) >= 0.025) else False
                #     )

                # print(event)
                print(is_held())
                # if hasattr(event, "stick"):
                #     print(event)
                #     print(is_held())

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

    def update_gamepads(self):
        self.gamepads = DeviceManager().gamepads


test = LastControllerInput()

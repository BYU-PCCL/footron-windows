from typing import Tuple
from XInput import get_events, EVENT_DISCONNECTED
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
        self.last_interaction = time() * 1000

        # threads for getting the inputs and posting the latest input
        get_input_loop_thread = Thread(target=self.get_input_loop, daemon=True)
        set_last_input_loop_thread = Thread(
            target=self.update_last_input_loop, daemon=True
        )
        get_input_loop_thread.start()
        set_last_input_loop_thread.start()
        while True:
            pass

    # pulls inputs from the controllers
    def get_input_loop(self):
        while True:
            events = get_events()
            for event in events:
                if event.type != EVENT_DISCONNECTED:
                    self.last_interaction = time() * 1000

    def update_last_input_loop(self):
        while True:
            sleep(LAST_CONTROLLER_INPUT_SET_DELAY)
            self._api.set_last_input(self.last_interaction)

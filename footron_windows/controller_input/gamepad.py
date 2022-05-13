from XInput import get_events, EVENT_DISCONNECTED
from threading import Thread
from time import sleep, time
import os

from .api import LastControllerInputApi

LAST_CONTROLLER_INPUT_SET_DELAY = 2
_CONTROLLER_URL_ENV = "FT_CONTROLLER_URL"
CONTROLLER_URL = (
    os.environ[_CONTROLLER_URL_ENV]
    if _CONTROLLER_URL_ENV in os.environ
    else "http://localhost:8000"
)


class LastControllerInput:
    def __init__(self):
        self.api = LastControllerInputApi(CONTROLLER_URL)
        self.last_interaction = None
        self.last_update = None
        self.update_last_interaction()

        # threads for getting the inputs and posting the latest input
        get_input_loop_thread = Thread(target=self._get_input_loop, daemon=True)
        set_last_input_loop_thread = Thread(
            target=self._update_last_input_loop, daemon=True
        )
        get_input_loop_thread.start()
        set_last_input_loop_thread.start()

    # pulls inputs from the controllers
    def _get_input_loop(self):
        while True:
            events = get_events()
            for event in events:
                if event.type != EVENT_DISCONNECTED:
                    self.update_last_interaction()

    def _update_last_input_loop(self):
        while True:
            if self.last_interaction != self.last_update and self.is_windows_exp():
                self.api.set_last_input(self.last_interaction)
                self.last_update = self.last_interaction
            sleep(LAST_CONTROLLER_INPUT_SET_DELAY)

    def is_windows_exp(self):
        current_exp = self.api.get_current()
        return current_exp["type"] == "capture"

    def update_last_interaction(self):
        self.last_interaction = int(time() * 1000)

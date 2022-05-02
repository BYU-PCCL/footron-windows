from typing import Tuple
from inputs import get_gamepad

from threading import Thread
import datetime as dt
from time import sleep, time
import os

from api import LastControllerInputApi

LAST_CONTROLLER_INPUT_SET_DELAY = 2
LAST_CONTROLLER_INPUT_ENDPOINT = "last_controller_input"

CONTROLLER_URL = (
    os.environ["FT_CONTROLLER_URL"]
    if "FT_CONTROLLER_URL" in os.environ
    else "http://localhost:8000"
)


class LastControllerInput:
    def __init__(self):
        self._api = LastControllerInputApi(CONTROLLER_URL)
        self.last_interaction = [
            time(),
            False,
        ]  # event.timestamp is in the format of seconds, so this might be the best strat
        self.holding = {}
        # self.holding_map = {
        #     "ABS_X": False,
        #     "ABS_Y": False,
        #     "ABS_RX": False,
        #     "ABS_RY": False,
        # }

        def get_input_loop():
            while True:
                events = get_gamepad()
                for event in events:
                    if event.ev_type == "Key":
                        # binary inputs (buttons, bumpers)
                        self.holding[event.code] = True if event.state == 1 else False
                    if event.code[0:3] == "ABS":
                        if event.code[4:7] == "HAT":
                            # d-pad
                            self.holding[event.code] = (
                                True if abs(event.state) == 1 else False
                            )
                        elif "Z" in str(event.code[4:6]):
                            # triggers
                            self.holding[event.code] = (
                                True if event.state > 10 else False
                            )
                        else:  # ABS_X or ABS_Y
                            # left and right stick
                            if abs(event.state) > 12000:
                                self.holding[event.code] = True
                            else:
                                self.holding[event.code] = False
                    # self.holding_map.update({event.code: abs(event.state) > 12000})
                    # holding = False
                    # if (
                    #     self.holding_map.get("ABS_X")
                    #     or self.holding_map.get("ABS_Y")
                    #     or self.holding_map.get("ABS_RX")
                    #     or self.holding_map.get("ABS_RY")
                    # ):
                    #     holding = True
                    self.last_interaction = [
                        event.timestamp,
                        True in self.holding.values(),
                    ]

        def update_last_input_loop():
            while True:
                sleep(LAST_CONTROLLER_INPUT_SET_DELAY)
                self._api.set_last_input(self.last_interaction)

        # threads for getting the inputs and posting the latest input
        get_input_loop_thread = Thread(target=get_input_loop)
        set_last_input_loop_thread = Thread(target=update_last_input_loop)
        get_input_loop_thread.setDaemon(True)
        set_last_input_loop_thread.setDaemon(True)
        get_input_loop_thread.start()
        set_last_input_loop_thread.start()
        while True:
            pass

            # send message or get api to do it

            # do we need the whole event? or just the time? Do we even need the time?
            # I guess we just compare the time to make sure there's a new interaction. Not bigger/less than, just !=

        # I mean, we just need to send a message every 5 seconds or so...
        # event thread loop will set the last event
        # the other loop will just post every 5 seconds.


test = LastControllerInput()


# for every event:
#   if the amount is more than thresh
#       set it as holding (store event?)
#
# Loop
# While True
#   While True
#       try to get the thing, if not break
#       last_event = the last event in the queue
#
#
#

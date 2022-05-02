from typing import Tuple
from inputs import get_gamepad

# from queue import Queue
from threading import Thread, Queue
import datetime as dt
from time import sleep, time
import asyncio
from queue import Empty
import os

LAST_CONTROLLER_INPUT_SET_DELAY = 5
LAST_CONTROLLER_INPUT_ENDPOINT = "last_controller_input"

CONTROLLER_URL = (
    os.environ["FT_CONTROLLER_URL"]
    if "FT_CONTROLLER_URL" in os.environ
    else "http://localhost:8000"
)


class LastControllerInput:
    def __init__(self):
        # self._queue = Queue()
        # self._queue_loop_thread = Thread(target=queue_loop, args=(self._queue))
        self._event_loop_thread = Thread(target=event_loop, args = )

        self.last_interaction = (
            time()
        )  # event.timestamp is in the format of seconds, so this might be the best strat
        self.holding_map = {
            "ABS_X": False,
            "ABS_Y": False,
            "ABS_RX": False,
            "ABS_RY": False,
        }

    async def queue_loop(self):
        self._queue_loop_thread.start()
        while True:
            sleep(LAST_CONTROLLER_INPUT_SET_DELAY)
            # send message or get api to do it

    def _start_event_thread_loop(self):
        events = get_gamepad()
        for event in events:
            self.holding_map.update(event.code, abs(event.state) > 12000)
            holding = False
            # time = event.timestamp
            # if (event.code == "ABS_X"
            # or event.code == "ABS_Y"
            # or event.code == "ABS_RX"
            # or event.code == "ABS_RY"):
            #     if abs(event.state) > 12000:
            #         holding = True
            if (
                self.holding_map.get("ABS_X")
                or self.holding_map.get("ABS_Y")
                or self.holding_map.get("ABS_RX")
                or self.holding_map.get("ABS_RY")
            ):
                holding = True
            # self.queue.put(Tuple(event, holding))
            self.last_interaction = Tuple(event, holding)
            # do we need the whole event? or just the time? Do we even need the time?
            # I guess we just compare the time to make sure there's a new interaction. Not bigger/less than, just !=

    

        # while True:
        #     while True:
        #         try:
        #             event = self.queue.get_nowait()
        #         except Empty:
        #             break
        #         # event: Tuple(event.timestamp, bool)
        #         # last_event = Tuple(event.timestamp, bool)
        #     # last_interaction = None
        #     if event[1]:
        #         self.last_interaction = event[0].timestamp
        # last_interaction = dt.datetime.now()
        # else:
        #     last_interaction = event[0]

        # I mean, we just need to send a message every 5 seconds or so...
        # event thread loop will set the last event
        # the other loop will just post every 5 seconds.

    # async def queue_loop(self):
    #     self._queue_loop_thread.start()
    #     while True:
    #         while True:
    #             try:
    #                 event = self.queue.get_nowait()
    #             except Empty:
    #                 break
    #             # event: Tuple(event.timestamp, bool)
    #             # last_event = Tuple(event.timestamp, bool)
    #         # last_interaction = None
    #         if event[1]:
    #             self.last_interaction = event[0].timestamp
    #             # last_interaction = dt.datetime.now()
    #         # else:
    #         #     last_interaction = event[0]

    #         # I mean, we just need to send a message every 5 seconds or so...
    #         # event thread loop will set the last event
    #         # the other loop will just post every 5 seconds.

    # Mapping of holding for the axis

    queue = Queue()

    start()


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

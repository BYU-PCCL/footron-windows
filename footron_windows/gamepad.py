from typing import Tuple
from inputs import get_gamepad
# from queue import Queue
from threading import Thread, Queue
import datetime as dt
import asyncio
from queue import Empty

class LastInputChecker:

    def __init__(self):
        self._queue_loop_thread = Thread(target=queue_loop, args=(queue))
        self._queue = Queue()
        self.holding_map = {
        "ABS_X": False,
        "ABS_Y": False,
        "ABS_RX": False,
        "ABS_RY": False
    }

    

    def _start_event_thread_loop(self):
        events = get_gamepad()
        for event in events:
            self.holding_map.update(event.code, abs(event.state) > 12000) 
            holding == False
            time = event.timestamp
            if (event.code == "ABS_X"
            or event.code == "ABS_Y"
            or event.code == "ABS_RX"
            or event.code == "ABS_RY"):
                if abs(event.state) > 12000:
                    holding = True
            self.queue.put(event)


    async def queue_loop(self):
        self._queue_loop_thread.start()
        while True:
            while True:
                try:
                    event = self.queue.get_nowait()
                except Empty:
                    break
                event: Tuple(event., bool)
            last_interaction = None
            if event[1]:
                last_interaction = dt.datetime.now()
            else:
                last_interaction = event[0]
            

# Mapping of holding for the axis
            

    queue = Queue()

    start()
import asyncio
from pathlib import Path
from typing import Optional

from footron_windows.job_popen import JobPopen


class WindowsController:
    _id: Optional[str]
    _process: Optional[JobPopen]
    _process_lock: asyncio.Lock

    def __init__(self):
        self._id = None
        self._process = None
        self._process_lock = asyncio.Lock()

    @property
    def id(self):
        return self._id

    async def stop_current(self):
        async with self._process_lock:
            await self._stop_current_inner()

    async def set_current(self, id: str, path: Path):
        async with self._process_lock:
            await self._set_current_inner(id, path)

    async def _stop_current_inner(self):
        if not self._id:
            return

        self._process.kill()
        self._id = None
        self._process = None

    async def _set_current_inner(self, id: str, path: Path):
        # Don't change anything if the desired experience is already set
        if id == self._id:
            return

        # Note that we DO NOT USE stop_current because it would wait for the lock
        # that we are currently holding, creating a deadlock
        await self._stop_current_inner()

        if not id:
            return

        self._id = id
        self._process = JobPopen(str(path))

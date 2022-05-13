import re
from pathlib import Path
from typing import Optional

import win32con
import win32gui
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from footron_windows.controller_input.gamepad import LastControllerInput

from .controller import WindowsController

app = FastAPI()

BASE_EXPERIENCE_PATH = Path("C:\\footron-experiences\\")

controller = WindowsController()
last_controller_input = None


class CurrentExperience(BaseModel):
    id: Optional[str]
    path: Optional[str]


class CurrentResponse(BaseModel):
    id: Optional[str]
    processes: Optional[int]


@app.on_event("startup")
async def startup_event():
    global last_controller_input
    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
    last_controller_input = LastControllerInput()


@app.put("/current")
async def set_current(body: CurrentExperience):
    if not body.id:
        await controller.stop_current()
    else:
        if not body.path:
            return HTTPException(
                status_code=400, detail="'path' is required when 'id' is specified"
            )
        if re.search(r"[^a-zA-Z0-9-]", body.id) is not None:
            raise HTTPException(status_code=400, detail=f"Invalid id '{body.id}'")
        experience_path = BASE_EXPERIENCE_PATH / body.id
        binary_path = (experience_path / (re.sub(r"\.\./", "", body.path))).resolve()
        if not binary_path.is_relative_to(BASE_EXPERIENCE_PATH):
            raise HTTPException(
                status_code=400, detail=f"Invalid or unauthorized path '{body.path}'"
            )
        await controller.set_current(body.id, binary_path)
    return {"status": "ok"}


@app.get("/current", response_model=CurrentResponse)
async def get_current():
    return CurrentResponse(id=controller.id, processes=controller.processes())

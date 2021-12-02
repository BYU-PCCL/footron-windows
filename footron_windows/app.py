import re
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .controller import WindowsController

app = FastAPI()

BASE_EXPERIENCE_PATH = Path("D:\\footron-experiences\\")

controller = WindowsController()


class CurrentExperience(BaseModel):
    id: Optional[str]
    path: Optional[str]


@app.put("/current")
async def root(body: CurrentExperience):
    if not body.id:
        await controller.stop_current()
    else:
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

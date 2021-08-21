import time

from fastapi import FastAPI

from .job_popen import JobPopen

app = FastAPI()


@app.get("/")
async def root():
    process = JobPopen("C:\\Users\\remote\\Desktop\\WindowsNoEditor\\DungeonBrawlers.exe")
    time.sleep(5)
    process.kill()
    return {"message": "Hello World"}

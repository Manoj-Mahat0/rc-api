# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from controller import update_state, get_current_state

app = FastAPI(title="RC Car Control API")

class Command(BaseModel):
    cmd: str  # e.g., forward, backward

@app.post("/command")
def set_command(command: Command):
    updated = update_state(command.cmd.lower())
    if updated:
        return {"message": f"Command '{updated}' applied"}
    raise HTTPException(status_code=400, detail="Invalid command")

@app.get("/status")
def get_status():
    return {"current_state": get_current_state()}

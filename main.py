from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow frontend apps (like React) to communicate with this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# To store current command state
current_state = {"status": "idle"}


class CommandInput(BaseModel):
    cmd: str  # Example: "forward", "backward", "left", "right", "stop", "voice:<text>"


@app.post("/control")
async def control_car(cmd_input: CommandInput):
    cmd = cmd_input.cmd.lower()
    current_state["status"] = cmd
    return {"message": f"Command '{cmd}' received."}


@app.get("/state")
def get_state():
    return {"status": current_state["status"]}

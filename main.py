from fastapi import FastAPI
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

# To store current command state and distance
current_state = {"status": "idle", "distance": 0.0}

class CommandInput(BaseModel):
    cmd: str  # Example: "forward", "backward", "left", "right", "stop", "voice:<text>"

class DistanceInput(BaseModel):
    distance: float

@app.post("/control")
async def control_car(cmd_input: CommandInput):
    cmd = cmd_input.cmd.lower()
    current_state["status"] = cmd
    return {"message": f"Command '{cmd}' received."}

@app.post("/distance")
async def set_distance(distance_input: DistanceInput):
    current_state["distance"] = distance_input.distance
    return {"message": f"Distance set to {distance_input.distance}"}

@app.get("/distance")
def get_distance():
    return {"distance": current_state["distance"]}

@app.get("/state")
def get_state():
    return {"status": current_state["status"]}
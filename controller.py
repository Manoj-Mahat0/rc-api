# controller.py

car_state = {"status": "stopped"}  # Initial state

def update_state(cmd: str):
    valid_cmds = {"forward", "backward", "left", "right", "stop"}
    if cmd not in valid_cmds:
        return None
    car_state["status"] = cmd
    print(f"🔄 Car state updated: {cmd}")
    return cmd

def get_current_state():
    return car_state["status"]

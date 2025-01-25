class DoorSensor:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def simulate_door_event(self, state):
        if state not in ["open", "closed"]:
            print("[DoorSensor] Invalid state")
            return
        print(f"[DoorSensor] Door {state}")
        self.event_bus.emit("door_event", state)

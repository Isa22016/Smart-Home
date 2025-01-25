class LightingSystem:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.light_on = False

    def toggle_light(self, action):
        self.light_on = action == "on"
        state = "on" if self.light_on else "off"
        print(f"[LightingSystem] Light turned {state}")
        self.event_bus.emit("light_change", state)

    def react_to_motion(self, data):
        print("[LightingSystem] Turning light on due to motion.")
        self.toggle_light("on")

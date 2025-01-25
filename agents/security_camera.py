class SecurityCamera:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def detect_motion(self):
        print("[SecurityCamera] Motion detected!")
        self.event_bus.emit("motion_detected", "motion")

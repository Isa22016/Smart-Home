class Thermostat:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def set_temperature(self, temperature):
        print(f"[Thermostat] Temperature set to {temperature}°C")
        self.event_bus.emit("temperature_change", temperature)

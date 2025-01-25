from agents.event_bus import EventBus
from agents.thermostat import Thermostat
from agents.security_camera import SecurityCamera
from agents.door_sensor import DoorSensor
from agents.lighting_system import LightingSystem

if __name__ == "__main__":
    event_bus = EventBus()

    thermostat = Thermostat(event_bus)
    camera = SecurityCamera(event_bus)
    door_sensor = DoorSensor(event_bus)
    lighting = LightingSystem(event_bus)

    event_bus.subscribe("motion_detected", lighting.react_to_motion)

    thermostat.set_temperature(22)
    door_sensor.simulate_door_event("open")
    camera.detect_motion()
    door_sensor.simulate_door_event("closed")

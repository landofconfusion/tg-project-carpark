import random
import json

from pathlib import Path
from datetime import datetime

from display import Display
from sensor import Sensor


class CarPark:
    def __init__(self, capacity, location = "Unknown", plates = None, sensors = None, displays = None, log_file = Path("log.txt"), config_file = Path("config.json")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)
        self.config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        self.config_file.touch(exist_ok=True)

    def __str__(self):
        return f'Car park at {self.location} has {self.capacity} bays'

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or a Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        #print("called add_car in carpark")
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        self.plates.remove(plate)
        #print("called remove_car in carpark")
        self.update_displays()
        self._log_car_activity(plate, "exited")

    @property
    def available_bays(self):
        return max(0,self.capacity - len(self.plates))

    def update_displays(self):
        random_temperature = format(random.randint(18,40))
        for display in self.displays:
            #print(f'Updating display {display.id}')
            display.update(f"Available Bays: {self.available_bays}\nTemperature: {random_temperature} degrees")

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f'{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n')

    def write_config(self):
        with self.config_file("w") as f:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])
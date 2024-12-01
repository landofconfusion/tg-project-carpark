import random
from abc import ABC, abstractmethod

class Sensor(ABC):
    def __init__(self, id, car_park, is_active = False):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f'Sensor {self.id} status is {self.is_active}'

    @abstractmethod
    def update_car_park(self, plate):
        ...

    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0,999), "03d")

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)


class EntrySensor(Sensor):
        ...


class ExitSensor(Sensor):
        ...
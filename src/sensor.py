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
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f'Incoming vehicle detected, plate: {plate}')


class ExitSensor(Sensor):
    def _scan_plate(self):
        return random.choice(self.car_park.plates)

    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f'Outgoing vehicle detected, plate: {plate}')

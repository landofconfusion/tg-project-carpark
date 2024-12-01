class Sensor:
    def __init__(self, id, is_active = False, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park


    def __str__(self):
        return f'Sensor {self.id} status is {self.is_active}'


    def EntrySensor (Sensor):
        ...


    def ExitSensor (Sensor):
        ...
class CarPark:
    def __init__(self, capacity, location = "Unknown", plates = None, sensors = None, displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f'Car park at {self.location} has {self.capacity} bays'
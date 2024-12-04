class Display:
    def __init__(self, id, car_park, message = "", is_on = False):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def update(self, message):
        self.message = message
        print("-" * 80)
        print(f'ID: {self.id}')
        print(message)
        print("-" * 80)

    def __str__(self):
        return f'Display {self.id}: {self.message}'


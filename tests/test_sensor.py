import unittest

from car_park import CarPark
from sensor import Sensor, EntrySensor, ExitSensor


class TestEntrySensor(unittest.TestCase):
    def setUp(self):
        self.sensor = EntrySensor(1, CarPark(1,"123 test street", None), True)
        self.car_park = CarPark(1,"123 test street", None)
        self.car_park.add_car("FAKE-123")

    def test_entry_sensor_initialized_with_all_attributes(self):
        self.assertEqual(self.sensor.id, 1)
        self.assertIsInstance(self.sensor.car_park, CarPark)
        self.assertEqual(self.sensor.is_active, True)

    def test_detect_vehicle_enter(self):
        plate_count_initial = 0
        self.sensor.detect_vehicle()
        plate_count_test = len(self.car_park.plates)
        self.assertGreater(plate_count_test, plate_count_initial)


class TestExitSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark(1,"123 test street", None)
        self.car_park.plates.append("FAKE-123")
        self.sensor = ExitSensor(1, self.car_park, True)

    def test_exit_sensor_initialized_with_all_attributes(self):
        self.assertEqual(self.sensor.id, 1)
        self.assertIsInstance(self.sensor.car_park, CarPark)
        self.assertEqual(self.sensor.is_active, True)

    def test_detect_vehicle_exit(self):
        plate_count_initial = len(self.car_park.plates)
        self.sensor.detect_vehicle()
        plate_count_test = len(self.car_park.plates)
        self.assertLess(plate_count_test, plate_count_initial)


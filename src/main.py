from pathlib import Path
from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

moondalup_car_park = CarPark(100, "Moondalup City", log_file = Path("moondalup.txt"))
display_one = Display("001", message = "Welcome to Moondalup", car_park = moondalup_car_park, is_on = True)
moondalup_car_park.register(display_one)
entry_sensor = EntrySensor("001", is_active = True, car_park=moondalup_car_park)
exit_sensor = ExitSensor("002", is_active = True, car_park=moondalup_car_park)

entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
exit_sensor.detect_vehicle()
exit_sensor.detect_vehicle()


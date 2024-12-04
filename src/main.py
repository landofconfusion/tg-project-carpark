from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

cp = CarPark(100, "Perth City central")
d1 = Display("Perth Display 001", cp)
d2 = Display("Perth Display 002", cp)
d3 = Display("Perth Display 003", cp)
cp.register(d1)
cp.register(d2)
#cp.register(d3)
es = EntrySensor("Perth Entry no 321", cp)
es.detect_vehicle()
exits = ExitSensor("Perth Exit no 123", cp)
exits.detect_vehicle()

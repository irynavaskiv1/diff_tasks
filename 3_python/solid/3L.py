"""
Liskov Substitution Principle- Об'єкти в програмі можуть бути заміненими їх нащадками без зміни коду програми.
Підкласи повинні доповнювати, а не змінювати батьківські класи.
"""


class Vehicle:
    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self) -> str:
        return f"The vehicle name {self.name}"

    def get_speed(self) -> str:
        return f"The vehicle speed {self.speed}"


class VehicleWithoutEngine(Vehicle):
    def start_moving(self):
        raise NotImplemented


class VehicleWithEngine(Vehicle):
    def engine(self):
        pass

    def start_engine(self):
        return self.engine()


class Car(VehicleWithEngine):
    def start_engine(self):
        pass


class Bicycle(VehicleWithoutEngine):
    def start_moving(self):
        pass

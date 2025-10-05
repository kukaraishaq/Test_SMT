class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.engine_on = False

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

    def start_engine(self):
        self.engine_on = True
        print(f"{self.make} {self.model} engine started.")

    def stop_engine(self):
        self.engine_on = False
        print(f"{self.make} {self.model} engine stopped.")

    def accelerate(self):
        if self.engine_on:
            print(f"{self.make} {self.model} is accelerating.")
        else:
            print(f"{self.make} {self.model} engine is off.")


class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.doors}")


class Truck(Vehicle):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)
        self.capacity = capacity

    def display_info(self):
        super().display_info()
        print(f"Cargo Capacity: {self.capacity} tons")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, drive_type):
        super().__init__(make, model, year)
        self.drive_type = drive_type

    def display_info(self):
        super().display_info()
        print(f"Drive Type: {self.drive_type}")


# Demo
vehicles = [
    Car("Toyota", "Camry", 2022, 4),
    Truck("Volvo", "FH16", 2021, 20),
    Motorcycle("Yamaha", "MT-09", 2023, "Chain")
]

for v in vehicles:
    v.display_info()
    v.start_engine()
    v.accelerate()
    v.stop_engine()
    print()

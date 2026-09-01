class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        return f"Brand: {self.brand}"


class ElectricCar(Vehicle):
    def show_battery(self, battery_capacity):
        return f"Battery: {battery_capacity} kWh"


brand = input()
battery_capacity = int(input())

car = ElectricCar(brand)

print(car.show_brand())
print(car.show_battery(battery_capacity))
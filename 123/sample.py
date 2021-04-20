class cars(object):

    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price


first_car = car("Mercedes", "red", 250000)
second_car = car("BMW", "blue", 200000)

print(second_car.color)
print(first_car.brand)
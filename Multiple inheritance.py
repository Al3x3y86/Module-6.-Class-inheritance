# Ваша задача:
# Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
# которая возвращает количество лошидиных сил для автомобиля
# Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type,
# а также переопределите функцию horse_powers
# Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price

class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 1000000

    def horse_powers(self):
        return

class Nissan(Car):
    def __init__(self):
        super().__init__()
        self.vehicle_type = "SUV" # переопределение типа
        self.price = 1200000 # переопределение цены

    def horse_powers(self):
        return 150 # переопределение количества лошадиных сил

nissan_car = Nissan()
print("Тип транспорта -", nissan_car.vehicle_type)
print("Стоимость транспорта -", nissan_car.price)

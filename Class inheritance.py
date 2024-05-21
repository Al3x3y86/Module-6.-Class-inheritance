# Ваша задача:
# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию
# def horse_powers, которая возвращает количество лошидиных сил для автомобиля
# Создайте наследника класса Car - класс Nissan и переопределите свойство price,
# а также переопределите функцию horse_powers
# Дополнительно создайте класс Kia, который также будет наследником класса Car и переопределите также свойство price,
# а также переопределите функцию horse_powers

class Car:
    price = 1000000

    def horse_powers(self):
        return

class Nissan(Car):
    price = 1100000

    def horse_powers(self):
        return 100

class Kia(Car):
    price = 1200000

    def horse_powers(self):
        return 200

# Пример использования
nissan_car = Nissan()
print(f"Nissan car price: {nissan_car.price} \nNissan car horse powers: {nissan_car.horse_powers()}")

kia_car = Kia()
print(f"Kia car price: {kia_car.price} \nKia car horse powers: {kia_car.horse_powers()}")


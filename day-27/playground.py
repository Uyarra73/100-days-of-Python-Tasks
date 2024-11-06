# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     print(total)
#
# add(1, 2, 3, 4, 5)

# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2,add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.brand = kw.get("brand")
        self.model = kw.get("model")

my_car = Car(brand="Mazda")
print(my_car.brand, my_car.model)



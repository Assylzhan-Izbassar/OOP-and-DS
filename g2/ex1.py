class Car:
    wheel = 4

    def __init__(self, model):
        self.model = model # instance value / member


class Laptop:
    def __init__(self):
        self._accounts = []

# set
# subset

# Laptop (_chips, __keyboard_std) <- HP (_chips)

# World




# set <- subset
# set1, set2
#


car1 = Car('Toyota')
car2 = Car('KIA')

print(car1.model, car2.model)
print(car1.wheel, car2.wheel)
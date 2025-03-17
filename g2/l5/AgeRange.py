# It will be the descriptor for validating an age.
class AgeRange:
    def __init__(self, attr_name: int):
        self.attr_name = attr_name

    def __get__(self, instance, owner):
        if instance is not None:
            return instance.__dict__[self.attr_name]

    def __set__(self, instance, value):
        if instance is not None and (18 <= value <= 63):
            instance.__dict__[self.attr_name] = value
        else:
            raise ValueError(f'Age={value} is not in a valid age range')


class SocialMediaUser:
    age = AgeRange('age')

    def __init__(self, name, age):
        self.__name = name
        self.age = age

u1 = SocialMediaUser('user1', 17)
# u1.age = 64
print(u1.age)
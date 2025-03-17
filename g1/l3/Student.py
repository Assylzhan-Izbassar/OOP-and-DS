from Person import Person

class Student(Person):
    def __init__(self, name, age, gender, gpa):
        super().__init__(name, age, gender)
        self.gpa = gpa

    def learning(self):
        print(f'{self.name} is learning')

    def sleep(self):
        print(f'{self.name} is sleeping in the lecture OOP')

    def __repr__(self):
        return f'Student({self.name!r}, {self.age!r}, {self.gender!r}, {self.gpa!r})'

    def __str__(self):
        return self.name + ' ' + str(self.age) + ' ' + self.gender

person = Person('Sanzhar', 20, 'male')
student1 = Student('Alinur', 20, 'male', 3.5)

print(student1)
student1.eat()
print(student1.gpa)
student1.sleep()
person.sleep()
student1.learning()

student1.introduce('Kaly', 19)
student1.introduce('Alina')

print(repr(student1))
print(student1)


from Person import Person

class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        self.gpa = gpa

    def go_to_lunch(self):
        print('Lunch at 2:00 PM')
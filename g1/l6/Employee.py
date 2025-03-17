from Person import Person

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def go_to_lunch(self):
        print('Lunch at 1:00 PM to 2:00 PM')

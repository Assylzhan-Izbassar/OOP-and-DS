from MaxHeap import MaxHeap, print_heap
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, grade):
        self._name = name
        self.__grade = grade

    @property
    def name(self):
        return self._name

    @property
    def grade(self):
        return self.__grade

    def __hash__(self):
        return hash(self.grade)

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.grade == other.grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            return False
        return self.grade < other.grade

    def __str__(self):
        return self.name + ' ' + str(self.grade)

s1 = Student('AAA', 5)
s2 = Student('BBB', 4.56)
s3 = Student('CCC', 4.14)
s4 = Student('DCC', 3.94)

priority_queue = MaxHeap()
priority_queue.insert(s1)
priority_queue.insert(s2)
priority_queue.insert(s3)
priority_queue.insert(s4)

print_heap(priority_queue.heap)

print(priority_queue.extract_top())

print_heap(priority_queue.heap)

print(priority_queue.extract_top())

print_heap(priority_queue.heap)
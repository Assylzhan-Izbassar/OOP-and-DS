# from Person import *
# from Student import *
# from Employee import *
# from g3.l4.decor import say_hello
#
# p1 = Person('John', 20)
# p2 = Student('Asan', 20, 3.5)
# p3 = Employee('Zhandos', 20, 400000)
#
# people = [p1, p2, p3]
#
# for p in people:
#     p.go_to_lunch()
#
#


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print('Hello, world!')

@repeat(3)
def say_goodbye():
    print('Goodbye!')

@repeat(3)
def greeting():
    print('Hello!')

# for i in range(3):
#     say_hello()
#
# for i in range(3):
#     say_goodbye()
#
# for i in range(3):
#     greeting()

# say_hello()
# say_goodbye()
# greeting()









# Example 2
import time

def time_it(unit='s'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()

            delta = end - start

            if unit == 'ms':
                delta *= 1000
                print(f'{delta} ms')
            else:
                print(f'{delta} s')

            return result
        return wrapper
    return decorator


@time_it('ms')
def sum(arr):
    s = 0
    for i in arr:
        s += i
    return s

# start = time.time() # current time
print(sum([1, 2, 3, 4, 5, 4, 5, 1, 2, 3, 4, 5]))
# end = time.time() # current time

# print(end - start)

# start = time.time()
a = [1, 3, 4, 5, 7]

reversed(a)
# end = time.time()
# print(list(a))
# print(end - start)







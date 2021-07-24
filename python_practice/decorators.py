import time
import math
import functools


# Simple decorator
def calculate_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time() - start_time
        print("Total time is %s" %end_time)

@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))


# Chaim decorators
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decor1
@decor
def num():
    return 10


# Decorator with input arguments
def decorator(*args, **kwargs):
    print("Inside decorator")
    def inner(func):
        print("Inside inner function")
        if kwargs['like'] == 'geeksforgeeks':
            print("I like", kwargs['like'])
            func()
        else:
            func()

    return inner

@decorator(like = "geeksforgeeks")
def func_with_input():
    print("Inside actual function")


# Decorator with functools
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        value = func(*args, **kwargs)
        return value
    return wrapper_decorator


if __name__ == '__main__':
    factorial(10)
    print(num())
    func_with_input()

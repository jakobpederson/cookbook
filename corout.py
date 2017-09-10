from functools import wraps
import random

def prime(func):
    def wrapper(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return wrapper

def add_seventeen(func):
    def wrapper(*args, **kwargs):
        old = func(*args, **kwargs)
        return old + 17
    return wrapper

@prime
def method():
    x = yield
    print('{} received'.format(x))

@add_seventeen
def get_number():
    return random.randint(0, 9)

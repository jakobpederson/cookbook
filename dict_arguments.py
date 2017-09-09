#!python

def basic_example(dog, cat):
    return (dog, cat)


def args(*args):
    return [x*2 for x in args]

def kwargs(**kwargs):
    return [(k, v) for k, v in kwargs.items()]



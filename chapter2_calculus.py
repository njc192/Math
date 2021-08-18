from math import *

""" 2.1 Rates of Changes and tangents to curves """


def average_rate_of_change_using_x1_x2(f, x1, x2):
    return (f(x2) - f(x1)) / (x2 - x1)


def derivative(f, x1, h):
    return (f(x1 + h) - f(x1)) / h


""" Limit of a Function and Limit Laws """


def get_limit_values():
    arr = []
    for i in range(1, 10):
        arr.append(1 / pow(10, i))

    return arr


def limit_above(function, x):
    for i in get_limit_values():
        print(function(x + i))


def limit_below(function, x):
    for i in get_limit_values():
        print(function(x - i))


def function(x):
    return (pow(x, 2) - 1) / (x - 1)


# limit_above(function, 1)
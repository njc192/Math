from tkinter import *
from math import *
import numpy as np
import matplotlib.pyplot as plt
from chapter2_calculus import derivative

#
root = Tk()

root.title("Testing")
root.geometry("500x500")


def function(x):
    return pow(x, 2)


def get_x_arr(x1, x2):
    x = []
    for i in range(x1, x2 + 1):
        x.append(i)
    return x


def get_x_arr1(x1, x2, step):
    """

    :param x1: start
    :param x2: stop
    :param step: increment
    :return: array of x values
    """
    return np.linspace(x1, x2, step)


def get_output(f, x_array):
    y = []
    for i in x_array:
        y.append(f(i))

    return y


def get_derivative_output(f, x_array):
    return "hello :3"


def graph(x, y):
    plt.plot(x, y)
    plt.show()


x_arr = get_x_arr1(0, 10, 100)
y_arr = get_output(function, x_arr)
graph(x_arr, y_arr)

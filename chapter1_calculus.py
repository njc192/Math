from math import *

'''1.1 Functions and their graphs'''


def binomial_theorem():
    return "No idea"


# ax^2+bx+c
def quadratic_formula(a, b, c):  # ax^2 + bx + c
    square_root = sqrt(pow(b, 2) - 4 * a * c)

    # return a tuple that contains both possible solutions
    return (((-1) * b + square_root) / 2 * a), (((-1) * b - square_root) / 2 * a)


def is_even_function(f, x):
    return f(x) == f((-1) * x)


def test_function_f(x):
    return 1 / (x - 1)


def increasing_or_decreasing(f, i1, i2):
    if f(i2) > f(i1):
        return "increasing"
    if f(i2) < f(i1):
        return "decreasing"


# print(is_even_function(test_function_f, 1))


'''1.3 Trigonometric Functions '''


def get_theta(s, r):
    """/
    s - arc s
    r - radius r
    theta in radians
    """

    return s / r


def get_arc(r, theta):
    """/
    theta in radians
    """
    return r * theta


def get_radians(deg):
    return (deg * pi) / 180


def get_degrees(rads):
    return (rads * 180) / pi


# print(get_degrees(0.523599))

'''trig identities'''


def sec_squared(theta):
    return 1 + pow(tan(theta), 2)


def cosecant_squared(theta):
    return 1 + pow(cot(theta), 2)


def cot(theta):
    """cotangent"""
    return 1 / tan(theta)


""" addition formulas """


def cos_a_plus_b(a, b):
    return (cos(a) * cos(b)) - (sin(a) * sin(b))


def sin_a_plus_b(a, b):
    return sin(a) * cos(b) + cos(a) * sin(b)


""" double angle formula """


def cos_2(theta):
    return pow(cos(theta), 2) - pow(sin(theta), 2)


def sin_2(theta):
    return 2 * sin(theta) * cos(theta)


""" half angle formula """


def half_angle_cos_squared(theta):
    return (1 + cos_2(theta)) / 2


def half_angle_sin_squared(theta):
    return (1 - cos_2(theta)) / 2


""" law of cosines """


def law_of_cosines(a, b, theta):
    """

    :param a: side of triangle
    :param b: side of triangle
    :param theta: in radians angle opposite c
    :return: c^2 third side of triangle
    """
    return pow(a, 2) + pow(b, 2) - (2 * a * b * cos(theta))


def sinusoid(a, b, c, d, x):
    """

    :param a: |A| Amplitude
    :param b: |B| Period
    :param c: |C| Horizontal Shift
    :param d: Vertical Shift
    :param x: location on sin graph
    :return: y value of function
    """
    return a * sin(((2 * pi) / b)(x - c)) + d

print(round(get_degrees(cos_a_plus_b(get_radians(36), -(pi/2))), 7))
print(round(get_degrees(sin(get_radians(36))), 7))
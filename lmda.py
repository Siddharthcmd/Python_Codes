import math

from typing import Any, Callable


def g(x, y): return x * (x + y)  # type: Callable[[Any, Any], Any]


print(g(8, 2))


def s(x): return math.factorial(x)


print(s(5))


def h(x): return x > 40 and x < 50


print(h(45))


def k(x): return x > 10


if (k(50)):
    print("The number is greater than 10")
else:
    print("The number is less than 10")


def m(x, y, z): return x + y


print(m(1, 2, 3) + g(2, 3))

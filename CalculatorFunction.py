"""
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
"""


def zero(v=None):
    return 0 if v is None else v(0)


def one(v=None):
    return 1 if v is None else v(1)


def two(v=None):
    return 2 if v is None else v(2)


def three(v=None):
    return 3 if v is None else v(3)


def four(v=None):
    return 4 if v is None else v(4)


def five(v=None):
    return 5 if v is None else v(5)


def six(v=None):
    return 6 if v is None else v(6)


def seven(v=None):
    return 7 if v is None else v(7)


def eight(v=None):
    return 8 if v is None else v(8)


def nine(v=None):
    return 9 if v is None else v(9)


def minus(y):
    return lambda x: x-y


def times(y):
    return lambda x: x*y


def plus(y):
    return lambda x: x+y


def divided_by(y):
    return lambda x: x//y


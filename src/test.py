# -*- coding: utf-8 -*-
# author: Markus Franke
# project: condatest
# file: test.py
# created: 19.12.2019

import math

__version__ = '1.0'


def do_something():
    print("This is a TEST on how to build conda packages.")
    # Using an imported package
    print("Pi is {:3.4f}".format(math.pi))


if __name__ == "__main__":

    do_something()

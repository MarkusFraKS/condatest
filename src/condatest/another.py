# -*- coding: utf-8 -*-
# author: Markus Franke
# project: condatest
# file: another.py
# created: 29.01.2020

import numpy as np


class Different:

    def huhu(self):
        print("This is a method of a class in another module")
        print("Try using numy:")
        print("Pi is approx.: {}".format(np.pi))


if __name__ == "__main__":
    pass

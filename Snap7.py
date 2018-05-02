#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@license: No
@contact: dave-lvxudong@outlook.com
@site: http://www.ilearning.com
@software: PyCharm
@file: Snap7.py
@time: 2018/5/3 0:20
"""
import snap7.client as client
from snap7.util import *
from snap7.snap7types import *



def readMemory(plc, byte, bit, dataType):
    result = plc.read_area(areas['MK'], 0, byte, dataType)


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass
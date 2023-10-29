#!/usr/bin/env python3
# Pre-defined blockId definitions
NOR = 0
AND = 1
OR = 2
XOR = 3
BUTTON = 4
FLIPFLOP = 5
LED = 6
SOUND = 7
CONDUCTOR = 8
CUSTOM = 9
NAND = 10
XNOR = 11
RANDOM = 12
TEXT = 13
TILE = 14

NORTH = [0, 0, -1, 0, 1, 0, 1, 0, 0]

EAST = [-1, 0, 0, 0, 1, 0, 0, 0, -1]

SOUTH = [0, 0, 1, 0, 1, -0, -1, 0, 0]

WEST = [1, 0, 0, 0, 1, 0, 0, 0, 1]


from .cm2py import *

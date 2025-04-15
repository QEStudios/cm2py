#!/usr/bin/env python3

from .enums import BlockType, Direction, BuildingType

# Explicitly expose BlockTypes so that linters can see them
NOR = BlockType.NOR
AND = BlockType.AND
OR = BlockType.OR
XOR = BlockType.XOR
BUTTON = BlockType.BUTTON
FLIPFLOP = BlockType.FLIPFLOP
LED = BlockType.LED
SOUND = BlockType.SOUND
CONDUCTOR = BlockType.CONDUCTOR
CUSTOM = BlockType.CUSTOM
NAND = BlockType.NAND
XNOR = BlockType.XNOR
RANDOM = BlockType.RANDOM
TEXT = BlockType.TEXT
TILE = BlockType.TILE
NODE = BlockType.NODE
DELAY = BlockType.DELAY
ANTENNA = BlockType.ANTENNA
CONDUCTOR_V2 = BlockType.CONDUCTOR_V2
LED_MIXER = BlockType.LED_MIXER

# Also expose directions
NORTH = Direction.NORTH
EAST = Direction.EAST
SOUTH = Direction.SOUTH
WEST = Direction.WEST

from .cm2py import *

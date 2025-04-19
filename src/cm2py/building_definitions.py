from .enums import BuildingType, IOType
from dataclasses import dataclass

##### IMPORTANT #####
# This file contains the information unique to each building.
# This includes the position of every block, in order, that the building has.
# BUILDING BLOCKS ARE NOT ORDERED LOGICALLY IN THE SAVESTRING!!
# For some buildings, they appear in the savestring in strange orders.
# All of these block positions were manually entered to preserve the strange ordering,
# the order shouldn't need to be changed!
# Circuit Maker 2 savestrings truly are a curious thing.


@dataclass
class BlockProperties:
    pos: tuple[int, int, int]
    ioType: IOType


@dataclass
class BuildingProperties:
    blocks: list[BlockProperties]


# Aliases to make definitions easier to read
BP = BlockProperties
INPUT = IOType.INPUT
OUTPUT = IOType.OUTPUT
BIDIRECTIONAL = IOType.BIDIRECTIONAL

definitions = {
    BuildingType.ASCII_KEY_INPUT: BuildingProperties(
        blocks=[
            BP((7, 0, -3), OUTPUT),  # Ctrl
            BP((-6, 0, -3), OUTPUT),  # ASCII [bit 7]
            BP((-5, 0, -3), OUTPUT),  # ASCII [bit 6]
            BP((-4, 0, -3), OUTPUT),  # ASCII [bit 5]
            BP((-3, 0, -3), OUTPUT),  # ASCII [bit 4]
            BP((-2, 0, -3), OUTPUT),  # ASCII [bit 3]
            BP((-1, 0, -3), OUTPUT),  # ASCII [bit 2]
            BP((0, 0, -3), OUTPUT),  # ASCII [bit 1]
            BP((1, 0, -3), OUTPUT),  # ASCII [bit 0]
            BP((3, 0, -3), OUTPUT),  # Pressed
            BP((5, 0, -3), OUTPUT),  # Shift
        ],
    ),
    BuildingType.ASSEMBLER: BuildingProperties(
        blocks=[
            BP((-17, 0, 4), INPUT),  # address [bit 11]
            BP((-8, 0, 4), INPUT),  # address [bit 2]
            BP((-7, 0, 4), INPUT),  # address [bit 1]
            BP((-6, 0, 4), INPUT),  # address [bit 0]
            BP((-16, 0, 4), INPUT),  # address [bit 10]
            BP((-15, 0, 4), INPUT),  # address [bit 9]
            BP((-14, 0, 4), INPUT),  # address [bit 8]
            BP((-13, 0, 4), INPUT),  # address [bit 7]
            BP((-12, 0, 4), INPUT),  # address [bit 6]
            BP((-11, 0, 4), INPUT),  # address [bit 5]
            BP((-10, 0, 4), INPUT),  # address [bit 4]
            BP((-9, 0, 4), INPUT),  # address [bit 3]
            BP((-17, 0, -4), OUTPUT),  # Byte 1 [bit 7]
            BP((-16, 0, -4), OUTPUT),  # Byte 1 [bit 6]
            BP((-15, 0, -4), OUTPUT),  # Byte 1 [bit 5]
            BP((-14, 0, -4), OUTPUT),  # Byte 1 [bit 4]
            BP((-13, 0, -4), OUTPUT),  # Byte 1 [bit 3]
            BP((-12, 0, -4), OUTPUT),  # Byte 1 [bit 2]
            BP((-11, 0, -4), OUTPUT),  # Byte 1 [bit 1]
            BP((-10, 0, -4), OUTPUT),  # Byte 1 [bit 0]
            BP((-8, 0, -4), OUTPUT),  # Byte 2 [bit 7]
            BP((-7, 0, -4), OUTPUT),  # Byte 2 [bit 6]
            BP((-6, 0, -4), OUTPUT),  # Byte 2 [bit 5]
            BP((-5, 0, -4), OUTPUT),  # Byte 2 [bit 4]
            BP((-4, 0, -4), OUTPUT),  # Byte 2 [bit 3]
            BP((-3, 0, -4), OUTPUT),  # Byte 2 [bit 2]
            BP((-2, 0, -4), OUTPUT),  # Byte 2 [bit 1]
            BP((-1, 0, -4), OUTPUT),  # Byte 2 [bit 0]
            BP((1, 0, -4), OUTPUT),  # Byte 3 [bit 7]
            BP((2, 0, -4), OUTPUT),  # Byte 3 [bit 6]
            BP((3, 0, -4), OUTPUT),  # Byte 3 [bit 5]
            BP((4, 0, -4), OUTPUT),  # Byte 3 [bit 4]
            BP((5, 0, -4), OUTPUT),  # Byte 3 [bit 3]
            BP((6, 0, -4), OUTPUT),  # Byte 3 [bit 2]
            BP((7, 0, -4), OUTPUT),  # Byte 3 [bit 1]
            BP((8, 0, -4), OUTPUT),  # Byte 3 [bit 0]
            BP((10, 0, -4), OUTPUT),  # Byte 4 [bit 7]
            BP((11, 0, -4), OUTPUT),  # Byte 4 [bit 6]
            BP((12, 0, -4), OUTPUT),  # Byte 4 [bit 5]
            BP((13, 0, -4), OUTPUT),  # Byte 4 [bit 4]
            BP((14, 0, -4), OUTPUT),  # Byte 4 [bit 3]
            BP((15, 0, -4), OUTPUT),  # Byte 4 [bit 2]
            BP((16, 0, -4), OUTPUT),  # Byte 4 [bit 1]
            BP((17, 0, -4), OUTPUT),  # Byte 4 [bit 0]
        ]
    ),
    BuildingType.DIVIDER: BuildingProperties(
        blocks=[
            BP((-1, 0, 7), INPUT),  # A [bit 15]
            BP((7, 0, 7), INPUT),  # A [bit 6]
            BP((8, 0, 7), INPUT),  # A [bit 5]
            BP((9, 0, 7), INPUT),  # A [bit 4]
            BP((10, 0, 7), INPUT),  # A [bit 3]
            BP((11, 0, 7), INPUT),  # A [bit 2]
            BP((12, 0, 7), INPUT),  # A [bit 1]
            BP((13, 0, 7), INPUT),  # A [bit 0]
            BP((0, 0, 7), INPUT),  # A [bit 14]
            BP((1, 0, 7), INPUT),  # A [bit 13]
            BP((2, 0, 7), INPUT),  # A [bit 12]
            BP((3, 0, 7), INPUT),  # A [bit 11]
            BP((3, 0, 7), INPUT),  # A [bit 10]
            BP((4, 0, 7), INPUT),  # A [bit 9]
            BP((5, 0, 7), INPUT),  # A [bit 8]
            BP((6, 0, 7), INPUT),  # A [bit 7]
            BP((16, 0, 7), INPUT),  # B [bit 15]
            BP((25, 0, 7), INPUT),  # B [bit 6]
            BP((26, 0, 7), INPUT),  # B [bit 5]
            BP((27, 0, 7), INPUT),  # B [bit 4]
            BP((28, 0, 7), INPUT),  # B [bit 3]
            BP((29, 0, 7), INPUT),  # B [bit 2]
            BP((30, 0, 7), INPUT),  # B [bit 1]
            BP((31, 0, 7), INPUT),  # B [bit 0]
            BP((17, 0, 7), INPUT),  # B [bit 14]
            BP((18, 0, 7), INPUT),  # B [bit 13]
            BP((19, 0, 7), INPUT),  # B [bit 12]
            BP((20, 0, 7), INPUT),  # B [bit 11]
            BP((21, 0, 7), INPUT),  # B [bit 10]
            BP((22, 0, 7), INPUT),  # B [bit 9]
            BP((23, 0, 7), INPUT),  # B [bit 8]
            BP((24, 0, 7), INPUT),  # B [bit 7]
            BP((-1, 0, -1), OUTPUT),  # Quotient [bit 15]
            BP((7, 0, -1), OUTPUT),  # Quotient [bit 6]
            BP((8, 0, -1), OUTPUT),  # Quotient [bit 5]
            BP((9, 0, -1), OUTPUT),  # Quotient [bit 4]
            BP((10, 0, -1), OUTPUT),  # Quotient [bit 3]
            BP((11, 0, -1), OUTPUT),  # Quotient [bit 2]
            BP((12, 0, -1), OUTPUT),  # Quotient [bit 1]
            BP((13, 0, -1), OUTPUT),  # Quotient [bit 0]
            BP((0, 0, -1), OUTPUT),  # Quotient [bit 14]
            BP((1, 0, -1), OUTPUT),  # Quotient [bit 13]
            BP((2, 0, -1), OUTPUT),  # Quotient [bit 12]
            BP((3, 0, -1), OUTPUT),  # Quotient [bit 11]
            BP((3, 0, -1), OUTPUT),  # Quotient [bit 10]
            BP((4, 0, -1), OUTPUT),  # Quotient [bit 9]
            BP((5, 0, -1), OUTPUT),  # Quotient [bit 8]
            BP((6, 0, -1), OUTPUT),  # Quotient [bit 7]
            BP((16, 0, -1), OUTPUT),  # Remainder [bit 15]
            BP((25, 0, -1), OUTPUT),  # Remainder [bit 6]
            BP((26, 0, -1), OUTPUT),  # Remainder [bit 5]
            BP((27, 0, -1), OUTPUT),  # Remainder [bit 4]
            BP((28, 0, -1), OUTPUT),  # Remainder [bit 3]
            BP((29, 0, -1), OUTPUT),  # Remainder [bit 2]
            BP((30, 0, -1), OUTPUT),  # Remainder [bit 1]
            BP((31, 0, -1), OUTPUT),  # Remainder [bit 0]
            BP((17, 0, -1), OUTPUT),  # Remainder [bit 14]
            BP((18, 0, -1), OUTPUT),  # Remainder [bit 13]
            BP((19, 0, -1), OUTPUT),  # Remainder [bit 12]
            BP((20, 0, -1), OUTPUT),  # Remainder [bit 11]
            BP((21, 0, -1), OUTPUT),  # Remainder [bit 10]
            BP((22, 0, -1), OUTPUT),  # Remainder [bit 9]
            BP((23, 0, -1), OUTPUT),  # Remainder [bit 8]
            BP((24, 0, -1), OUTPUT),  # Remainder [bit 7]
        ]
    ),
    BuildingType.DOOR: BuildingProperties(
        blocks=[
            BP((0, 7, 0), INPUT),
        ]
    ),
    BuildingType.DUAL_MEMORY: BuildingProperties(
        blocks=[
            BP((-4, 0, 2), INPUT),  # Save Address [bit 7]
            BP((-3, 0, 2), INPUT),  # Save Address [bit 6]
            BP((-2, 0, 2), INPUT),  # Save Address [bit 5]
            BP((-1, 0, 2), INPUT),  # Save Address [bit 4]
            BP((0, 0, 2), INPUT),  # Save Address [bit 3]
            BP((1, 0, 2), INPUT),  # Save Address [bit 2]
            BP((2, 0, 2), INPUT),  # Save Address [bit 1]
            BP((3, 0, 2), INPUT),  # Save Address [bit 0]
            BP((-13, 0, 2), INPUT),  # Load Address [bit 7]
            BP((-12, 0, 2), INPUT),  # Load Address [bit 6]
            BP((-11, 0, 2), INPUT),  # Load Address [bit 5]
            BP((-10, 0, 2), INPUT),  # Load Address [bit 4]
            BP((-9, 0, 2), INPUT),  # Load Address [bit 3]
            BP((-8, 0, 2), INPUT),  # Load Address [bit 2]
            BP((-7, 0, 2), INPUT),  # Load Address [bit 1]
            BP((-6, 0, 2), INPUT),  # Load Address [bit 0]
            BP((-13, 0, -2), OUTPUT),  # Output [bit 7]
            BP((-12, 0, -2), OUTPUT),  # Output [bit 6]
            BP((-11, 0, -2), OUTPUT),  # Output [bit 5]
            BP((-10, 0, -2), OUTPUT),  # Output [bit 4]
            BP((-9, 0, -2), OUTPUT),  # Output [bit 3]
            BP((-8, 0, -2), OUTPUT),  # Output [bit 2]
            BP((-7, 0, -2), OUTPUT),  # Output [bit 1]
            BP((-6, 0, -2), OUTPUT),  # Output [bit 0]
            BP((5, 0, 2), INPUT),  # Value [bit 7]
            BP((6, 0, 2), INPUT),  # Value [bit 6]
            BP((7, 0, 2), INPUT),  # Value [bit 5]
            BP((8, 0, 2), INPUT),  # Value [bit 4]
            BP((9, 0, 2), INPUT),  # Value [bit 3]
            BP((10, 0, 2), INPUT),  # Value [bit 2]
            BP((11, 0, 2), INPUT),  # Value [bit 1]
            BP((12, 0, 2), INPUT),  # Value [bit 0]
            BP((14, 0, 2), INPUT),  # write
        ]
    ),
    BuildingType.FUNCTION_GENERATOR: BuildingProperties(
        blocks=[
            BP((8, 0, 3), INPUT),  # Func [bit 1]
            BP((9, 0, 3), INPUT),  # Func [bit 0]
            BP((-1, 0, -2), OUTPUT),  # Output [bit 7]
            BP((0, 0, -2), OUTPUT),  # Output [bit 6]
            BP((1, 0, -2), OUTPUT),  # Output [bit 5]
            BP((2, 0, -2), OUTPUT),  # Output [bit 4]
            BP((3, 0, -2), OUTPUT),  # Output [bit 3]
            BP((4, 0, -2), OUTPUT),  # Output [bit 2]
            BP((5, 0, -2), OUTPUT),  # Output [bit 1]
            BP((6, 0, -2), OUTPUT),  # Output [bit 0]
            BP((-1, 0, 3), INPUT),  # X [bit 7]
            BP((0, 0, 3), INPUT),  # X [bit 6]
            BP((1, 0, 3), INPUT),  # X [bit 5]
            BP((2, 0, 3), INPUT),  # X [bit 4]
            BP((3, 0, 3), INPUT),  # X [bit 3]
            BP((4, 0, 3), INPUT),  # X [bit 2]
            BP((5, 0, 3), INPUT),  # X [bit 1]
            BP((6, 0, 3), INPUT),  # X [bit 0]
        ]
    ),
    BuildingType.GRAPH: BuildingProperties(
        blocks=[
            BP((-4, 0, 4), INPUT),  # Input [bit 7]
            BP((-3, 0, 4), INPUT),  # Input [bit 7]
            BP((-2, 0, 4), INPUT),  # Input [bit 7]
            BP((-1, 0, 4), INPUT),  # Input [bit 7]
            BP((0, 0, 4), INPUT),  # Input [bit 7]
            BP((1, 0, 4), INPUT),  # Input [bit 7]
            BP((2, 0, 4), INPUT),  # Input [bit 7]
            BP((3, 0, 4), INPUT),  # Input [bit 7]
        ]
    ),
    BuildingType.HUGE_MEMORY: BuildingProperties(
        blocks=[
            BP((-17, 0, 3), INPUT),  # address [bit 15]
            BP((-8, 0, 3), INPUT),  # address [bit 6]
            BP((-7, 0, 3), INPUT),  # address [bit 5]
            BP((-6, 0, 3), INPUT),  # address [bit 4]
            BP((-5, 0, 3), INPUT),  # address [bit 3]
            BP((-4, 0, 3), INPUT),  # address [bit 2]
            BP((-3, 0, 3), INPUT),  # address [bit 1]
            BP((-2, 0, 3), INPUT),  # address [bit 0]
            BP((-16, 0, 3), INPUT),  # address [bit 14]
            BP((-15, 0, 3), INPUT),  # address [bit 13]
            BP((-14, 0, 3), INPUT),  # address [bit 12]
            BP((-13, 0, 3), INPUT),  # address [bit 11]
            BP((-12, 0, 3), INPUT),  # address [bit 10]
            BP((-11, 0, 3), INPUT),  # address [bit 9]
            BP((-10, 0, 3), INPUT),  # address [bit 8]
            BP((-9, 0, 3), INPUT),  # address [bit 7]
            BP((-17, 0, -3), OUTPUT),  # output [bit 15]
            BP((-8, 0, -3), OUTPUT),  # output [bit 6]
            BP((-7, 0, -3), OUTPUT),  # output [bit 5]
            BP((-6, 0, -3), OUTPUT),  # output [bit 4]
            BP((-5, 0, -3), OUTPUT),  # output [bit 3]
            BP((-4, 0, -3), OUTPUT),  # output [bit 2]
            BP((-3, 0, -3), OUTPUT),  # output [bit 1]
            BP((-2, 0, -3), OUTPUT),  # output [bit 0]
            BP((-16, 0, -3), OUTPUT),  # output [bit 14]
            BP((-15, 0, -3), OUTPUT),  # output [bit 13]
            BP((-14, 0, -3), OUTPUT),  # output [bit 12]
            BP((-13, 0, -3), OUTPUT),  # output [bit 11]
            BP((-12, 0, -3), OUTPUT),  # output [bit 10]
            BP((-11, 0, -3), OUTPUT),  # output [bit 9]
            BP((-10, 0, -3), OUTPUT),  # output [bit 8]
            BP((-9, 0, -3), OUTPUT),  # output [bit 7]
            BP((1, 0, 3), INPUT),  # value [bit 15]
            BP((10, 0, 3), INPUT),  # value [bit 6]
            BP((11, 0, 3), INPUT),  # value [bit 5]
            BP((12, 0, 3), INPUT),  # value [bit 4]
            BP((13, 0, 3), INPUT),  # value [bit 3]
            BP((14, 0, 3), INPUT),  # value [bit 2]
            BP((15, 0, 3), INPUT),  # value [bit 1]
            BP((16, 0, 3), INPUT),  # value [bit 0]
            BP((2, 0, 3), INPUT),  # value [bit 14]
            BP((3, 0, 3), INPUT),  # value [bit 13]
            BP((4, 0, 3), INPUT),  # value [bit 12]
            BP((5, 0, 3), INPUT),  # value [bit 11]
            BP((6, 0, 3), INPUT),  # value [bit 10]
            BP((7, 0, 3), INPUT),  # value [bit 9]
            BP((8, 0, 3), INPUT),  # value [bit 8]
            BP((9, 0, 3), INPUT),  # value [bit 7]
            BP((18, 0, 3), INPUT),  # write
        ]
    ),
    BuildingType.INTEGRATED_CIRCUIT: BuildingProperties(
        blocks=[
            BP((0, 0, 7), INPUT),  # input [bit 31]
            BP((9, 0, 7), INPUT),  # input [bit 22]
            BP((10, 0, 7), INPUT),  # input [bit 21]
            BP((11, 0, 7), INPUT),  # input [bit 20]
            BP((12, 0, 7), INPUT),  # input [bit 19]
            BP((13, 0, 7), INPUT),  # input [bit 18]
            BP((14, 0, 7), INPUT),  # input [bit 17]
            BP((15, 0, 7), INPUT),  # input [bit 16]
            BP((16, 0, 7), INPUT),  # input [bit 15]
            BP((17, 0, 7), INPUT),  # input [bit 14]
            BP((18, 0, 7), INPUT),  # input [bit 13]
            BP((1, 0, 7), INPUT),  # input [bit 30]
            BP((19, 0, 7), INPUT),  # input [bit 12]
            BP((20, 0, 7), INPUT),  # input [bit 11]
            BP((21, 0, 7), INPUT),  # input [bit 10]
            BP((22, 0, 7), INPUT),  # input [bit 9]
            BP((23, 0, 7), INPUT),  # input [bit 8]
            BP((24, 0, 7), INPUT),  # input [bit 7]
            BP((25, 0, 7), INPUT),  # input [bit 6]
            BP((26, 0, 7), INPUT),  # input [bit 5]
            BP((27, 0, 7), INPUT),  # input [bit 4]
            BP((28, 0, 7), INPUT),  # input [bit 3]
            BP((2, 0, 7), INPUT),  # input [bit 29]
            BP((29, 0, 7), INPUT),  # input [bit 2]
            BP((30, 0, 7), INPUT),  # input [bit 1]
            BP((31, 0, 7), INPUT),  # input [bit 0]
            BP((3, 0, 7), INPUT),  # input [bit 28]
            BP((4, 0, 7), INPUT),  # input [bit 27]
            BP((5, 0, 7), INPUT),  # input [bit 26]
            BP((6, 0, 7), INPUT),  # input [bit 25]
            BP((7, 0, 7), INPUT),  # input [bit 24]
            BP((8, 0, 7), INPUT),  # input [bit 23]
            BP((0, 0, -1), OUTPUT),  # output [bit 31]
            BP((9, 0, -1), OUTPUT),  # output [bit 22]
            BP((10, 0, -1), OUTPUT),  # output [bit 21]
            BP((11, 0, -1), OUTPUT),  # output [bit 20]
            BP((12, 0, -1), OUTPUT),  # output [bit 19]
            BP((13, 0, -1), OUTPUT),  # output [bit 18]
            BP((14, 0, -1), OUTPUT),  # output [bit 17]
            BP((15, 0, -1), OUTPUT),  # output [bit 16]
            BP((16, 0, -1), OUTPUT),  # output [bit 15]
            BP((17, 0, -1), OUTPUT),  # output [bit 14]
            BP((18, 0, -1), OUTPUT),  # output [bit 13]
            BP((1, 0, -1), OUTPUT),  # output [bit 30]
            BP((19, 0, -1), OUTPUT),  # output [bit 12]
            BP((20, 0, -1), OUTPUT),  # output [bit 11]
            BP((21, 0, -1), OUTPUT),  # output [bit 10]
            BP((22, 0, -1), OUTPUT),  # output [bit 9]
            BP((23, 0, -1), OUTPUT),  # output [bit 8]
            BP((24, 0, -1), OUTPUT),  # output [bit 7]
            BP((25, 0, -1), OUTPUT),  # output [bit 6]
            BP((26, 0, -1), OUTPUT),  # output [bit 5]
            BP((27, 0, -1), OUTPUT),  # output [bit 4]
            BP((28, 0, -1), OUTPUT),  # output [bit 3]
            BP((2, 0, -1), OUTPUT),  # output [bit 29]
            BP((29, 0, -1), OUTPUT),  # output [bit 2]
            BP((30, 0, -1), OUTPUT),  # output [bit 1]
            BP((31, 0, -1), OUTPUT),  # output [bit 0]
            BP((3, 0, -1), OUTPUT),  # output [bit 28]
            BP((4, 0, -1), OUTPUT),  # output [bit 27]
            BP((5, 0, -1), OUTPUT),  # output [bit 26]
            BP((6, 0, -1), OUTPUT),  # output [bit 25]
            BP((7, 0, -1), OUTPUT),  # output [bit 24]
            BP((8, 0, -1), OUTPUT),  # output [bit 23]
        ]
    ),
    BuildingType.KEY_INPUT: BuildingProperties(
        blocks=[
            BP((-18, 0, -4), OUTPUT),  # A
            BP((-9, 0, -4), OUTPUT),  # J
            BP((-8, 0, -4), OUTPUT),  # K
            BP((-7, 0, -4), OUTPUT),  # L
            BP((-6, 0, -4), OUTPUT),  # M
            BP((-5, 0, -4), OUTPUT),  # N
            BP((-4, 0, -4), OUTPUT),  # O
            BP((-3, 0, -4), OUTPUT),  # P
            BP((-2, 0, -4), OUTPUT),  # Q
            BP((-1, 0, -4), OUTPUT),  # R
            BP((0, 0, -4), OUTPUT),  # S
            BP((-17, 0, -4), OUTPUT),  # B
            BP((1, 0, -4), OUTPUT),  # T
            BP((2, 0, -4), OUTPUT),  # U
            BP((3, 0, -4), OUTPUT),  # V
            BP((4, 0, -4), OUTPUT),  # W
            BP((5, 0, -4), OUTPUT),  # X
            BP((6, 0, -4), OUTPUT),  # Y
            BP((7, 0, -4), OUTPUT),  # Z
            BP((8, 0, -4), OUTPUT),  # 1
            BP((9, 0, -4), OUTPUT),  # 2
            BP((-16, 0, -4), OUTPUT),  # C
            BP((10, 0, -4), OUTPUT),  # 3
            BP((11, 0, -4), OUTPUT),  # 4
            BP((12, 0, -4), OUTPUT),  # 5
            BP((13, 0, -4), OUTPUT),  # 6
            BP((14, 0, -4), OUTPUT),  # 7
            BP((15, 0, -4), OUTPUT),  # 8
            BP((16, 0, -4), OUTPUT),  # 9
            BP((17, 0, -4), OUTPUT),  # 0
            BP((18, 0, -4), OUTPUT),  # space
            BP((-15, 0, -4), OUTPUT),  # D
            BP((-14, 0, -4), OUTPUT),  # E
            BP((-13, 0, -4), OUTPUT),  # F
            BP((-12, 0, -4), OUTPUT),  # G
            BP((-11, 0, -4), OUTPUT),  # H
            BP((-10, 0, -4), OUTPUT),  # I
        ]
    ),
    BuildingType.LARGE_RGB_DISPLAY: BuildingProperties(
        blocks=[
            BP((10, 0, 18), INPUT),  # B [bit 5]
            BP((11, 0, 18), INPUT),  # B [bit 4]
            BP((12, 0, 18), INPUT),  # B [bit 3]
            BP((13, 0, 18), INPUT),  # B [bit 2]
            BP((14, 0, 18), INPUT),  # B [bit 1]
            BP((15, 0, 18), INPUT),  # B [bit 0]
            BP((3, 0, 18), INPUT),  # G [bit 5]
            BP((4, 0, 18), INPUT),  # G [bit 4]
            BP((5, 0, 18), INPUT),  # G [bit 3]
            BP((6, 0, 18), INPUT),  # G [bit 2]
            BP((7, 0, 18), INPUT),  # G [bit 1]
            BP((8, 0, 18), INPUT),  # G [bit 0]
            BP((-4, 0, 18), INPUT),  # R [bit 5]
            BP((-3, 0, 18), INPUT),  # R [bit 4]
            BP((-2, 0, 18), INPUT),  # R [bit 3]
            BP((-1, 0, 18), INPUT),  # R [bit 2]
            BP((0, 0, 18), INPUT),  # R [bit 1]
            BP((1, 0, 18), INPUT),  # R [bit 0]
            BP((17, 0, 18), INPUT),  # Reset
            BP((19, 0, 18), INPUT),  # Write
            BP((-20, 0, 18), INPUT),  # X [bit 6]
            BP((-19, 0, 18), INPUT),  # X [bit 5]
            BP((-18, 0, 18), INPUT),  # X [bit 4]
            BP((-17, 0, 18), INPUT),  # X [bit 3]
            BP((-16, 0, 18), INPUT),  # X [bit 2]
            BP((-15, 0, 18), INPUT),  # X [bit 1]
            BP((-14, 0, 18), INPUT),  # X [bit 0]
            BP((-12, 0, 18), INPUT),  # Y [bit 6]
            BP((-11, 0, 18), INPUT),  # Y [bit 5]
            BP((-10, 0, 18), INPUT),  # Y [bit 4]
            BP((-9, 0, 18), INPUT),  # Y [bit 3]
            BP((-8, 0, 18), INPUT),  # Y [bit 2]
            BP((-7, 0, 18), INPUT),  # Y [bit 1]
            BP((-6, 0, 18), INPUT),  # Y [bit 0]
        ]
    ),
    BuildingType.MASS_MEMORY: BuildingProperties(
        blocks=[
            BP((-11, 0, 2), INPUT),  # address [bit 11]
            BP((-2, 0, 2), INPUT),  # address [bit 2]
            BP((-1, 0, 2), INPUT),  # address [bit 1]
            BP((0, 0, 2), INPUT),  # address [bit 0]
            BP((-10, 0, 2), INPUT),  # address [bit 10]
            BP((-9, 0, 2), INPUT),  # address [bit 9]
            BP((-8, 0, 2), INPUT),  # address [bit 8]
            BP((-7, 0, 2), INPUT),  # address [bit 7]
            BP((-6, 0, 2), INPUT),  # address [bit 6]
            BP((-5, 0, 2), INPUT),  # address [bit 5]
            BP((-4, 0, 2), INPUT),  # address [bit 4]
            BP((-3, 0, 2), INPUT),  # address [bit 3]
            BP((-11, 0, -2), OUTPUT),  # output [bit 7]
            BP((-10, 0, -2), OUTPUT),  # output [bit 6]
            BP((-9, 0, -2), OUTPUT),  # output [bit 5]
            BP((-8, 0, -2), OUTPUT),  # output [bit 4]
            BP((-7, 0, -2), OUTPUT),  # output [bit 3]
            BP((-6, 0, -2), OUTPUT),  # output [bit 2]
            BP((-5, 0, -2), OUTPUT),  # output [bit 1]
            BP((-4, 0, -2), OUTPUT),  # output [bit 0]
            BP((2, 0, 2), INPUT),  # value [bit 7]
            BP((3, 0, 2), INPUT),  # value [bit 6]
            BP((4, 0, 2), INPUT),  # value [bit 5]
            BP((5, 0, 2), INPUT),  # value [bit 4]
            BP((6, 0, 2), INPUT),  # value [bit 3]
            BP((7, 0, 2), INPUT),  # value [bit 2]
            BP((8, 0, 2), INPUT),  # value [bit 1]
            BP((9, 0, 2), INPUT),  # value [bit 0]
            BP((11, 0, 2), INPUT),  # write
        ]
    ),
    BuildingType.MASSIVE_MEMORY: BuildingProperties(
        blocks=[
            BP((-15, 0, 2), INPUT),  # address [bit 11]
            BP((-6, 0, 2), INPUT),  # address [bit 2]
            BP((-5, 0, 2), INPUT),  # address [bit 1]
            BP((-4, 0, 2), INPUT),  # address [bit 0]
            BP((-14, 0, 2), INPUT),  # address [bit 10]
            BP((-13, 0, 2), INPUT),  # address [bit 9]
            BP((-12, 0, 2), INPUT),  # address [bit 8]
            BP((-11, 0, 2), INPUT),  # address [bit 7]
            BP((-10, 0, 2), INPUT),  # address [bit 6]
            BP((-9, 0, 2), INPUT),  # address [bit 5]
            BP((-8, 0, 2), INPUT),  # address [bit 4]
            BP((-7, 0, 2), INPUT),  # address [bit 3]
            BP((-15, 0, -2), OUTPUT),  # output [bit 15]
            BP((-6, 0, -2), OUTPUT),  # output [bit 6]
            BP((-5, 0, -2), OUTPUT),  # output [bit 5]
            BP((-4, 0, -2), OUTPUT),  # output [bit 4]
            BP((-3, 0, -2), OUTPUT),  # output [bit 3]
            BP((-2, 0, -2), OUTPUT),  # output [bit 2]
            BP((-1, 0, -2), OUTPUT),  # output [bit 1]
            BP((0, 0, -2), OUTPUT),  # output [bit 0]
            BP((-14, 0, -2), OUTPUT),  # output [bit 14]
            BP((-13, 0, -2), OUTPUT),  # output [bit 13]
            BP((-12, 0, -2), OUTPUT),  # output [bit 12]
            BP((-11, 0, -2), OUTPUT),  # output [bit 11]
            BP((-10, 0, -2), OUTPUT),  # output [bit 10]
            BP((-9, 0, -2), OUTPUT),  # output [bit 9]
            BP((-8, 0, -2), OUTPUT),  # output [bit 8]
            BP((-7, 0, -2), OUTPUT),  # output [bit 7]
            BP((-2, 0, 2), INPUT),  # value [bit 15]
            BP((7, 0, 2), INPUT),  # value [bit 6]
            BP((8, 0, 2), INPUT),  # value [bit 5]
            BP((9, 0, 2), INPUT),  # value [bit 4]
            BP((10, 0, 2), INPUT),  # value [bit 3]
            BP((11, 0, 2), INPUT),  # value [bit 2]
            BP((12, 0, 2), INPUT),  # value [bit 1]
            BP((13, 0, 2), INPUT),  # value [bit 0]
            BP((-1, 0, 2), INPUT),  # value [bit 14]
            BP((0, 0, 2), INPUT),  # value [bit 13]
            BP((1, 0, 2), INPUT),  # value [bit 12]
            BP((2, 0, 2), INPUT),  # value [bit 11]
            BP((3, 0, 2), INPUT),  # value [bit 10]
            BP((4, 0, 2), INPUT),  # value [bit 9]
            BP((5, 0, 2), INPUT),  # value [bit 8]
            BP((6, 0, 2), INPUT),  # value [bit 7]
            BP((15, 0, 2), INPUT),  # write
        ]
    ),
    BuildingType.MULTIPLIER: BuildingProperties(
        blocks=[
            BP((-1, 0, 7), INPUT),  # A [bit 15]
            BP((7, 0, 7), INPUT),  # A [bit 6]
            BP((8, 0, 7), INPUT),  # A [bit 5]
            BP((9, 0, 7), INPUT),  # A [bit 4]
            BP((10, 0, 7), INPUT),  # A [bit 3]
            BP((11, 0, 7), INPUT),  # A [bit 2]
            BP((12, 0, 7), INPUT),  # A [bit 1]
            BP((13, 0, 7), INPUT),  # A [bit 0]
            BP((0, 0, 7), INPUT),  # A [bit 14]
            BP((1, 0, 7), INPUT),  # A [bit 13]
            BP((2, 0, 7), INPUT),  # A [bit 12]
            BP((3, 0, 7), INPUT),  # A [bit 11]
            BP((3, 0, 7), INPUT),  # A [bit 10]
            BP((4, 0, 7), INPUT),  # A [bit 9]
            BP((5, 0, 7), INPUT),  # A [bit 8]
            BP((6, 0, 7), INPUT),  # A [bit 7]
            BP((16, 0, 7), INPUT),  # B [bit 15]
            BP((25, 0, 7), INPUT),  # B [bit 6]
            BP((26, 0, 7), INPUT),  # B [bit 5]
            BP((27, 0, 7), INPUT),  # B [bit 4]
            BP((28, 0, 7), INPUT),  # B [bit 3]
            BP((29, 0, 7), INPUT),  # B [bit 2]
            BP((30, 0, 7), INPUT),  # B [bit 1]
            BP((31, 0, 7), INPUT),  # B [bit 0]
            BP((17, 0, 7), INPUT),  # B [bit 14]
            BP((18, 0, 7), INPUT),  # B [bit 13]
            BP((19, 0, 7), INPUT),  # B [bit 12]
            BP((20, 0, 7), INPUT),  # B [bit 11]
            BP((21, 0, 7), INPUT),  # B [bit 10]
            BP((22, 0, 7), INPUT),  # B [bit 9]
            BP((23, 0, 7), INPUT),  # B [bit 8]
            BP((24, 0, 7), INPUT),  # B [bit 7]
            BP((-1, 0, -1), OUTPUT),  # Output [bit 31]
            BP((7, 0, -1), OUTPUT),  # Output [bit 22]
            BP((8, 0, -1), OUTPUT),  # Output [bit 21]
            BP((9, 0, -1), OUTPUT),  # Output [bit 20]
            BP((10, 0, -1), OUTPUT),  # Output [bit 19]
            BP((11, 0, -1), OUTPUT),  # Output [bit 18]
            BP((12, 0, -1), OUTPUT),  # Output [bit 17]
            BP((13, 0, -1), OUTPUT),  # Output [bit 16]
            BP((16, 0, -1), OUTPUT),  # Output [bit 15]
            BP((17, 0, -1), OUTPUT),  # Output [bit 14]
            BP((18, 0, -1), OUTPUT),  # Output [bit 13]
            BP((0, 0, -1), OUTPUT),  # Output [bit 30]
            BP((19, 0, -1), OUTPUT),  # Output [bit 12]
            BP((20, 0, -1), OUTPUT),  # Output [bit 11]
            BP((21, 0, -1), OUTPUT),  # Output [bit 10]
            BP((22, 0, -1), OUTPUT),  # Output [bit 9]
            BP((23, 0, -1), OUTPUT),  # Output [bit 8]
            BP((24, 0, -1), OUTPUT),  # Output [bit 7]
            BP((25, 0, -1), OUTPUT),  # Output [bit 6]
            BP((26, 0, -1), OUTPUT),  # Output [bit 5]
            BP((27, 0, -1), OUTPUT),  # Output [bit 4]
            BP((28, 0, -1), OUTPUT),  # Output [bit 3]
            BP((1, 0, -1), OUTPUT),  # Output [bit 29]
            BP((29, 0, -1), OUTPUT),  # Output [bit 2]
            BP((30, 0, -1), OUTPUT),  # Output [bit 1]
            BP((31, 0, -1), OUTPUT),  # Output [bit 0]
            BP((2, 0, -1), OUTPUT),  # Output [bit 28]
            BP((3, 0, -1), OUTPUT),  # Output [bit 27]
            BP((3, 0, -1), OUTPUT),  # Output [bit 26]
            BP((4, 0, -1), OUTPUT),  # Output [bit 25]
            BP((5, 0, -1), OUTPUT),  # Output [bit 24]
            BP((6, 0, -1), OUTPUT),  # Output [bit 23]
        ]
    ),
    BuildingType.N_TRANSISTOR: BuildingProperties(
        blocks=[
            BP((1, 0, 0), BIDIRECTIONAL),  # Right
            BP((0, 0, 1), INPUT),  # Bottom
            BP((-1, 0, 0), BIDIRECTIONAL),  # Left
        ]
    ),
    BuildingType.P_TRANSISTOR: BuildingProperties(
        blocks=[
            BP((1, 0, 0), BIDIRECTIONAL),  # Right
            BP((0, 0, 1), INPUT),  # Bottom
            BP((-1, 0, 0), BIDIRECTIONAL),  # Left
        ]
    ),
    BuildingType.PIXEL_DISPLAY: BuildingProperties(
        blocks=[
            BP((4, 0, 10), INPUT),  # Pixel
            BP((6, 0, 10), INPUT),  # Reset
            BP((8, 0, 10), INPUT),  # Write
            BP((-8, 0, 10), INPUT),  # X [bit 4]
            BP((-7, 0, 10), INPUT),  # X [bit 3]
            BP((-6, 0, 10), INPUT),  # X [bit 2]
            BP((-5, 0, 10), INPUT),  # X [bit 1]
            BP((-4, 0, 10), INPUT),  # X [bit 0]
            BP((-2, 0, 10), INPUT),  # Y [bit 4]
            BP((-1, 0, 10), INPUT),  # Y [bit 3]
            BP((0, 0, 10), INPUT),  # Y [bit 2]
            BP((1, 0, 10), INPUT),  # Y [bit 1]
            BP((2, 0, 10), INPUT),  # Y [bit 0]
        ]
    ),
    BuildingType.QWERTY_KEY_INPUT: BuildingProperties(
        blocks=[
            BP((2, 1, -4), OUTPUT),  # 0
            BP((-7, 1, -4), OUTPUT),  # 1
            BP((-6, 1, -4), OUTPUT),  # 2
            BP((-5, 1, -4), OUTPUT),  # 3
            BP((-4, 1, -4), OUTPUT),  # 4
            BP((-3, 1, -4), OUTPUT),  # 5
            BP((-2, 1, -4), OUTPUT),  # 6
            BP((-1, 1, -4), OUTPUT),  # 7
            BP((0, 1, -4), OUTPUT),  # 8
            BP((1, 1, -4), OUTPUT),  # 9
            BP((-7, 1, -2), OUTPUT),  # A
            BP((-7, 1, 0), OUTPUT),  # left alt
            BP((2, 1, 0), OUTPUT),  # right alt
            BP((3, 1, -2), OUTPUT),  # '
            BP((-3, 1, -1), OUTPUT),  # B
            BP((5, 1, -3), OUTPUT),  # \
            BP((5, 1, -4), OUTPUT),  # backspace
            BP((-5, 1, -1), OUTPUT),  # C
            BP((-8, 1, -2), OUTPUT),  # caps lock
            BP((0, 1, -1), OUTPUT),  # ,
            BP((-8, 1, 0), OUTPUT),  # left ctrl
            BP((3, 1, 0), OUTPUT),  # right ctrl
            BP((-5, 1, -2), OUTPUT),  # D
            BP((7, 1, 0), OUTPUT),  # down
            BP((-5, 1, -3), OUTPUT),  # E
            BP((4, 1, -2), OUTPUT),  # enter
            BP((4, 1, -4), OUTPUT),  # =
            BP((-4, 1, -2), OUTPUT),  # F
            BP((-3, 1, -2), OUTPUT),  # G
            BP((-2, 1, -2), OUTPUT),  # H
            BP((0, 1, -3), OUTPUT),  # I
            BP((-1, 1, -2), OUTPUT),  # J
            BP((0, 1, -2), OUTPUT),  # K
            BP((1, 1, -2), OUTPUT),  # L
            BP((6, 1, 0), OUTPUT),  # left
            BP((-1, 1, -1), OUTPUT),  # M
            BP((3, 1, -4), OUTPUT),  # -
            BP((-2, 1, -1), OUTPUT),  # N
            BP((1, 1, -3), OUTPUT),  # O
            BP((2, 1, -3), OUTPUT),  # P
            BP((1, 1, -1), OUTPUT),  # .
            BP((-7, 1, -3), OUTPUT),  # Q
            BP((-4, 1, -3), OUTPUT),  # R
            BP((8, 1, 0), OUTPUT),  # right
            BP((-6, 1, -2), OUTPUT),  # S
            BP((2, 1, -2), OUTPUT),  # ;
            BP((-8, 1, -1), OUTPUT),  # left shift
            BP((3, 1, -1), OUTPUT),  # right shift
            BP((2, 1, -1), OUTPUT),  # /
            BP((-2, 1, 0), OUTPUT),  # space
            BP((3, 1, -3), OUTPUT),  # [
            BP((4, 1, -3), OUTPUT),  # ]
            BP((-3, 1, -3), OUTPUT),  # T
            BP((-8, 1, -3), OUTPUT),  # tab
            BP((-8, 1, -4), OUTPUT),  # `
            BP((-1, 1, -3), OUTPUT),  # U
            BP((7, 1, -1), OUTPUT),  # up
            BP((-4, 1, -1), OUTPUT),  # V
            BP((-6, 1, -3), OUTPUT),  # W
            BP((-6, 1, -1), OUTPUT),  # X
            BP((-2, 1, -3), OUTPUT),  # Y
            BP((-7, 1, -1), OUTPUT),  # Z
        ]
    ),
    BuildingType.RGB_DISPLAY: BuildingProperties(
        blocks=[
            BP((8, 0, 18), INPUT),  # B [bit 3]
            BP((9, 0, 18), INPUT),  # B [bit 2]
            BP((10, 0, 18), INPUT),  # B [bit 1]
            BP((11, 0, 18), INPUT),  # B [bit 0]
            BP((3, 0, 18), INPUT),  # G [bit 3]
            BP((4, 0, 18), INPUT),  # G [bit 2]
            BP((5, 0, 18), INPUT),  # G [bit 1]
            BP((6, 0, 18), INPUT),  # G [bit 0]
            BP((-2, 0, 18), INPUT),  # R [bit 3]
            BP((-1, 0, 18), INPUT),  # R [bit 2]
            BP((0, 0, 18), INPUT),  # R [bit 1]
            BP((1, 0, 18), INPUT),  # R [bit 0]
            BP((13, 0, 18), INPUT),  # Reset
            BP((14, 0, 18), INPUT),  # Write
            BP((-14, 0, 18), INPUT),  # X [bit 4]
            BP((-13, 0, 18), INPUT),  # X [bit 3]
            BP((-12, 0, 18), INPUT),  # X [bit 2]
            BP((-11, 0, 18), INPUT),  # X [bit 1]
            BP((-10, 0, 18), INPUT),  # X [bit 0]
            BP((-8, 0, 18), INPUT),  # Y [bit 4]
            BP((-7, 0, 18), INPUT),  # Y [bit 3]
            BP((-6, 0, 18), INPUT),  # Y [bit 2]
            BP((-5, 0, 18), INPUT),  # Y [bit 1]
            BP((-4, 0, 18), INPUT),  # Y [bit 0]
        ]
    ),
    BuildingType.REAL_TIME_CLOCK: BuildingProperties(
        blocks=[
            BP((9, 0, -1), INPUT),  # CHG
            BP((0, 0, -1), INPUT),  # +/-
            BP((12, 0, -1), INPUT),  # HOL
            BP((10, 0, -1), INPUT),  # RST
            BP((11, 0, -1), INPUT),  # SYN
            BP((5, 0, -1), INPUT),  # 1D input
            BP((4, 0, -1), INPUT),  # 1h input
            BP((3, 0, -1), INPUT),  # 1m input
            BP((2, 0, -1), INPUT),  # 1s input
            BP((31, 0, -1), OUTPUT),  # 1D output
            BP((30, 0, -1), OUTPUT),  # 1h output
            BP((29, 0, -1), OUTPUT),  # 1m output
            BP((28, 0, -1), OUTPUT),  # 1s output
            BP((31, 0, 4), OUTPUT),  # Timestamp [bit 0]
            BP((22, 0, 4), OUTPUT),  # Timestamp [bit 9]
            BP((21, 0, 4), OUTPUT),  # Timestamp [bit 10]
            BP((20, 0, 4), OUTPUT),  # Timestamp [bit 11]
            BP((19, 0, 4), OUTPUT),  # Timestamp [bit 12]
            BP((18, 0, 4), OUTPUT),  # Timestamp [bit 13]
            BP((17, 0, 4), OUTPUT),  # Timestamp [bit 14]
            BP((16, 0, 4), OUTPUT),  # Timestamp [bit 15]
            BP((15, 0, 4), OUTPUT),  # Timestamp [bit 16]
            BP((14, 0, 4), OUTPUT),  # Timestamp [bit 17]
            BP((13, 0, 4), OUTPUT),  # Timestamp [bit 18]
            BP((30, 0, 4), OUTPUT),  # Timestamp [bit 1]
            BP((12, 0, 4), OUTPUT),  # Timestamp [bit 19]
            BP((11, 0, 4), OUTPUT),  # Timestamp [bit 20]
            BP((10, 0, 4), OUTPUT),  # Timestamp [bit 21]
            BP((9, 0, 4), OUTPUT),  # Timestamp [bit 22]
            BP((8, 0, 4), OUTPUT),  # Timestamp [bit 23]
            BP((7, 0, 4), OUTPUT),  # Timestamp [bit 24]
            BP((6, 0, 4), OUTPUT),  # Timestamp [bit 25]
            BP((5, 0, 4), OUTPUT),  # Timestamp [bit 26]
            BP((4, 0, 4), OUTPUT),  # Timestamp [bit 27]
            BP((3, 0, 4), OUTPUT),  # Timestamp [bit 28]
            BP((29, 0, 4), OUTPUT),  # Timestamp [bit 2]
            BP((2, 0, 4), OUTPUT),  # Timestamp [bit 29]
            BP((1, 0, 4), OUTPUT),  # Timestamp [bit 30]
            BP((0, 0, 4), OUTPUT),  # Timestamp [bit 31]
            BP((28, 0, 4), OUTPUT),  # Timestamp [bit 3]
            BP((27, 0, 4), OUTPUT),  # Timestamp [bit 4]
            BP((26, 0, 4), OUTPUT),  # Timestamp [bit 5]
            BP((25, 0, 4), OUTPUT),  # Timestamp [bit 6]
            BP((24, 0, 4), OUTPUT),  # Timestamp [bit 7]
            BP((23, 0, 4), OUTPUT),  # Timestamp [bit 8]
        ]
    ),
    BuildingType.SIGN: BuildingProperties(
        blocks=[
            BP((-4, 0, -4), INPUT),
        ]
    ),
    BuildingType.TEXT_CONSOLE: BuildingProperties(
        blocks=[
            BP((-1, 0, 9), INPUT),  # Char [bit 7]
            BP((0, 0, 9), INPUT),  # Char [bit 6]
            BP((1, 0, 9), INPUT),  # Char [bit 5]
            BP((2, 0, 9), INPUT),  # Char [bit 4]
            BP((3, 0, 9), INPUT),  # Char [bit 3]
            BP((4, 0, 9), INPUT),  # Char [bit 2]
            BP((5, 0, 9), INPUT),  # Char [bit 1]
            BP((6, 0, 9), INPUT),  # Char [bit 0]
            BP((8, 0, 9), INPUT),  # Clear
            BP((9, 0, 9), INPUT),  # Cursor
            BP((-10, 0, 9), INPUT),  # Location [bit 7]
            BP((-9, 0, 9), INPUT),  # Location [bit 6]
            BP((-8, 0, 9), INPUT),  # Location [bit 5]
            BP((-7, 0, 9), INPUT),  # Location [bit 4]
            BP((-6, 0, 9), INPUT),  # Location [bit 3]
            BP((-5, 0, 9), INPUT),  # Location [bit 2]
            BP((-4, 0, 9), INPUT),  # Location [bit 1]
            BP((-3, 0, 9), INPUT),  # Location [bit 0]
            BP((10, 0, 9), INPUT),  # Write
        ]
    ),
    BuildingType.DIVIDER_32_BIT: BuildingProperties(
        blocks=[
            BP((-1, 0, 7), INPUT),  # A [bit 31]
            BP((8, 0, 7), INPUT),  # A [bit 22]
            BP((9, 0, 7), INPUT),  # A [bit 21]
            BP((10, 0, 7), INPUT),  # A [bit 20]
            BP((11, 0, 7), INPUT),  # A [bit 19]
            BP((12, 0, 7), INPUT),  # A [bit 18]
            BP((13, 0, 7), INPUT),  # A [bit 17]
            BP((14, 0, 7), INPUT),  # A [bit 16]
            BP((15, 0, 7), INPUT),  # A [bit 15]
            BP((16, 0, 7), INPUT),  # A [bit 14]
            BP((17, 0, 7), INPUT),  # A [bit 13]
            BP((0, 0, 7), INPUT),  # A [bit 30]
            BP((1, 0, 7), INPUT),  # A [bit 29]
            BP((18, 0, 7), INPUT),  # A [bit 12]
            BP((19, 0, 7), INPUT),  # A [bit 11]
            BP((20, 0, 7), INPUT),  # A [bit 10]
            BP((21, 0, 7), INPUT),  # A [bit 9]
            BP((22, 0, 7), INPUT),  # A [bit 8]
            BP((23, 0, 7), INPUT),  # A [bit 7]
            BP((24, 0, 7), INPUT),  # A [bit 6]
            BP((25, 0, 7), INPUT),  # A [bit 5]
            BP((26, 0, 7), INPUT),  # A [bit 4]
            BP((27, 0, 7), INPUT),  # A [bit 3]
            BP((2, 0, 7), INPUT),  # A [bit 28]
            BP((28, 0, 7), INPUT),  # A [bit 2]
            BP((29, 0, 7), INPUT),  # A [bit 1]
            BP((30, 0, 7), INPUT),  # A [bit 0]
            BP((3, 0, 7), INPUT),  # A [bit 27]
            BP((4, 0, 7), INPUT),  # A [bit 26]
            BP((5, 0, 7), INPUT),  # A [bit 25]
            BP((6, 0, 7), INPUT),  # A [bit 24]
            BP((7, 0, 7), INPUT),  # A [bit 23]
            BP((33, 0, 7), INPUT),  # B [bit 31]
            BP((42, 0, 7), INPUT),  # B [bit 22]
            BP((43, 0, 7), INPUT),  # B [bit 21]
            BP((44, 0, 7), INPUT),  # B [bit 20]
            BP((45, 0, 7), INPUT),  # B [bit 19]
            BP((46, 0, 7), INPUT),  # B [bit 18]
            BP((47, 0, 7), INPUT),  # B [bit 17]
            BP((48, 0, 7), INPUT),  # B [bit 16]
            BP((49, 0, 7), INPUT),  # B [bit 15]
            BP((50, 0, 7), INPUT),  # B [bit 14]
            BP((51, 0, 7), INPUT),  # B [bit 13]
            BP((34, 0, 7), INPUT),  # B [bit 30]
            BP((52, 0, 7), INPUT),  # B [bit 12]
            BP((53, 0, 7), INPUT),  # B [bit 11]
            BP((54, 0, 7), INPUT),  # B [bit 10]
            BP((55, 0, 7), INPUT),  # B [bit 9]
            BP((56, 0, 7), INPUT),  # B [bit 8]
            BP((57, 0, 7), INPUT),  # B [bit 7]
            BP((58, 0, 7), INPUT),  # B [bit 6]
            BP((59, 0, 7), INPUT),  # B [bit 5]
            BP((60, 0, 7), INPUT),  # B [bit 4]
            BP((61, 0, 7), INPUT),  # B [bit 3]
            BP((35, 0, 7), INPUT),  # B [bit 29]
            BP((62, 0, 7), INPUT),  # B [bit 2]
            BP((63, 0, 7), INPUT),  # B [bit 1]
            BP((64, 0, 7), INPUT),  # B [bit 0]
            BP((36, 0, 7), INPUT),  # B [bit 28]
            BP((37, 0, 7), INPUT),  # B [bit 27]
            BP((38, 0, 7), INPUT),  # B [bit 26]
            BP((39, 0, 7), INPUT),  # B [bit 25]
            BP((40, 0, 7), INPUT),  # B [bit 24]
            BP((41, 0, 7), INPUT),  # B [bit 23]
            BP((-1, 0, -1), OUTPUT),  # Quotient [bit 31]
            BP((8, 0, -1), OUTPUT),  # Quotient [bit 22]
            BP((9, 0, -1), OUTPUT),  # Quotient [bit 21]
            BP((10, 0, -1), OUTPUT),  # Quotient [bit 20]
            BP((11, 0, -1), OUTPUT),  # Quotient [bit 19]
            BP((12, 0, -1), OUTPUT),  # Quotient [bit 18]
            BP((13, 0, -1), OUTPUT),  # Quotient [bit 17]
            BP((14, 0, -1), OUTPUT),  # Quotient [bit 16]
            BP((15, 0, -1), OUTPUT),  # Quotient [bit 15]
            BP((16, 0, -1), OUTPUT),  # Quotient [bit 14]
            BP((17, 0, -1), OUTPUT),  # Quotient [bit 13]
            BP((0, 0, -1), OUTPUT),  # Quotient [bit 30]
            BP((18, 0, -1), OUTPUT),  # Quotient [bit 12]
            BP((19, 0, -1), OUTPUT),  # Quotient [bit 11]
            BP((20, 0, -1), OUTPUT),  # Quotient [bit 10]
            BP((21, 0, -1), OUTPUT),  # Quotient [bit 9]
            BP((22, 0, -1), OUTPUT),  # Quotient [bit 8]
            BP((23, 0, -1), OUTPUT),  # Quotient [bit 7]
            BP((24, 0, -1), OUTPUT),  # Quotient [bit 6]
            BP((25, 0, -1), OUTPUT),  # Quotient [bit 5]
            BP((26, 0, -1), OUTPUT),  # Quotient [bit 4]
            BP((27, 0, -1), OUTPUT),  # Quotient [bit 3]
            BP((1, 0, -1), OUTPUT),  # Quotient [bit 29]
            BP((28, 0, -1), OUTPUT),  # Quotient [bit 2]
            BP((29, 0, -1), OUTPUT),  # Quotient [bit 1]
            BP((30, 0, -1), OUTPUT),  # Quotient [bit 0]
            BP((2, 0, -1), OUTPUT),  # Quotient [bit 28]
            BP((3, 0, -1), OUTPUT),  # Quotient [bit 27]
            BP((4, 0, -1), OUTPUT),  # Quotient [bit 26]
            BP((5, 0, -1), OUTPUT),  # Quotient [bit 25]
            BP((6, 0, -1), OUTPUT),  # Quotient [bit 24]
            BP((7, 0, -1), OUTPUT),  # Quotient [bit 23]
            BP((33, 0, -1), OUTPUT),  # Remainder [bit 31]
            BP((42, 0, -1), OUTPUT),  # Remainder [bit 22]
            BP((43, 0, -1), OUTPUT),  # Remainder [bit 21]
            BP((44, 0, -1), OUTPUT),  # Remainder [bit 20]
            BP((45, 0, -1), OUTPUT),  # Remainder [bit 19]
            BP((46, 0, -1), OUTPUT),  # Remainder [bit 18]
            BP((47, 0, -1), OUTPUT),  # Remainder [bit 17]
            BP((48, 0, -1), OUTPUT),  # Remainder [bit 16]
            BP((49, 0, -1), OUTPUT),  # Remainder [bit 15]
            BP((50, 0, -1), OUTPUT),  # Remainder [bit 14]
            BP((51, 0, -1), OUTPUT),  # Remainder [bit 13]
            BP((34, 0, -1), OUTPUT),  # Remainder [bit 30]
            BP((52, 0, -1), OUTPUT),  # Remainder [bit 12]
            BP((53, 0, -1), OUTPUT),  # Remainder [bit 11]
            BP((54, 0, -1), OUTPUT),  # Remainder [bit 10]
            BP((55, 0, -1), OUTPUT),  # Remainder [bit 9]
            BP((56, 0, -1), OUTPUT),  # Remainder [bit 8]
            BP((57, 0, -1), OUTPUT),  # Remainder [bit 7]
            BP((58, 0, -1), OUTPUT),  # Remainder [bit 6]
            BP((59, 0, -1), OUTPUT),  # Remainder [bit 5]
            BP((60, 0, -1), OUTPUT),  # Remainder [bit 4]
            BP((61, 0, -1), OUTPUT),  # Remainder [bit 3]
            BP((35, 0, -1), OUTPUT),  # Remainder [bit 29]
            BP((62, 0, -1), OUTPUT),  # Remainder [bit 2]
            BP((63, 0, -1), OUTPUT),  # Remainder [bit 1]
            BP((64, 0, -1), OUTPUT),  # Remainder [bit 0]
            BP((36, 0, -1), OUTPUT),  # Remainder [bit 28]
            BP((37, 0, -1), OUTPUT),  # Remainder [bit 27]
            BP((38, 0, -1), OUTPUT),  # Remainder [bit 26]
            BP((39, 0, -1), OUTPUT),  # Remainder [bit 25]
            BP((40, 0, -1), OUTPUT),  # Remainder [bit 24]
            BP((41, 0, -1), OUTPUT),  # Remainder [bit 23]
        ]
    ),
    BuildingType.DIVIDER_32_BIT: BuildingProperties(
        blocks=[
            BP((-1, 0, 7), INPUT),  # A [bit 31]
            BP((8, 0, 7), INPUT),  # A [bit 22]
            BP((9, 0, 7), INPUT),  # A [bit 21]
            BP((10, 0, 7), INPUT),  # A [bit 20]
            BP((11, 0, 7), INPUT),  # A [bit 19]
            BP((12, 0, 7), INPUT),  # A [bit 18]
            BP((13, 0, 7), INPUT),  # A [bit 17]
            BP((14, 0, 7), INPUT),  # A [bit 16]
            BP((15, 0, 7), INPUT),  # A [bit 15]
            BP((16, 0, 7), INPUT),  # A [bit 14]
            BP((17, 0, 7), INPUT),  # A [bit 13]
            BP((0, 0, 7), INPUT),  # A [bit 30]
            BP((1, 0, 7), INPUT),  # A [bit 29]
            BP((18, 0, 7), INPUT),  # A [bit 12]
            BP((19, 0, 7), INPUT),  # A [bit 11]
            BP((20, 0, 7), INPUT),  # A [bit 10]
            BP((21, 0, 7), INPUT),  # A [bit 9]
            BP((22, 0, 7), INPUT),  # A [bit 8]
            BP((23, 0, 7), INPUT),  # A [bit 7]
            BP((24, 0, 7), INPUT),  # A [bit 6]
            BP((25, 0, 7), INPUT),  # A [bit 5]
            BP((26, 0, 7), INPUT),  # A [bit 4]
            BP((27, 0, 7), INPUT),  # A [bit 3]
            BP((2, 0, 7), INPUT),  # A [bit 28]
            BP((28, 0, 7), INPUT),  # A [bit 2]
            BP((29, 0, 7), INPUT),  # A [bit 1]
            BP((30, 0, 7), INPUT),  # A [bit 0]
            BP((3, 0, 7), INPUT),  # A [bit 27]
            BP((4, 0, 7), INPUT),  # A [bit 26]
            BP((5, 0, 7), INPUT),  # A [bit 25]
            BP((6, 0, 7), INPUT),  # A [bit 24]
            BP((7, 0, 7), INPUT),  # A [bit 23]
            BP((33, 0, 7), INPUT),  # B [bit 31]
            BP((42, 0, 7), INPUT),  # B [bit 22]
            BP((43, 0, 7), INPUT),  # B [bit 21]
            BP((44, 0, 7), INPUT),  # B [bit 20]
            BP((45, 0, 7), INPUT),  # B [bit 19]
            BP((46, 0, 7), INPUT),  # B [bit 18]
            BP((47, 0, 7), INPUT),  # B [bit 17]
            BP((48, 0, 7), INPUT),  # B [bit 16]
            BP((49, 0, 7), INPUT),  # B [bit 15]
            BP((50, 0, 7), INPUT),  # B [bit 14]
            BP((51, 0, 7), INPUT),  # B [bit 13]
            BP((34, 0, 7), INPUT),  # B [bit 30]
            BP((52, 0, 7), INPUT),  # B [bit 12]
            BP((53, 0, 7), INPUT),  # B [bit 11]
            BP((54, 0, 7), INPUT),  # B [bit 10]
            BP((55, 0, 7), INPUT),  # B [bit 9]
            BP((56, 0, 7), INPUT),  # B [bit 8]
            BP((57, 0, 7), INPUT),  # B [bit 7]
            BP((58, 0, 7), INPUT),  # B [bit 6]
            BP((59, 0, 7), INPUT),  # B [bit 5]
            BP((60, 0, 7), INPUT),  # B [bit 4]
            BP((61, 0, 7), INPUT),  # B [bit 3]
            BP((35, 0, 7), INPUT),  # B [bit 29]
            BP((62, 0, 7), INPUT),  # B [bit 2]
            BP((63, 0, 7), INPUT),  # B [bit 1]
            BP((64, 0, 7), INPUT),  # B [bit 0]
            BP((36, 0, 7), INPUT),  # B [bit 28]
            BP((37, 0, 7), INPUT),  # B [bit 27]
            BP((38, 0, 7), INPUT),  # B [bit 26]
            BP((39, 0, 7), INPUT),  # B [bit 25]
            BP((40, 0, 7), INPUT),  # B [bit 24]
            BP((41, 0, 7), INPUT),  # B [bit 23]
            BP((-1, 0, -1), OUTPUT),  # Output [bit 63]
            BP((8, 0, -1), OUTPUT),  # Output [bit 54]
            BP((9, 0, -1), OUTPUT),  # Output [bit 53]
            BP((10, 0, -1), OUTPUT),  # Output [bit 52]
            BP((11, 0, -1), OUTPUT),  # Output [bit 51]
            BP((12, 0, -1), OUTPUT),  # Output [bit 50]
            BP((13, 0, -1), OUTPUT),  # Output [bit 49]
            BP((14, 0, -1), OUTPUT),  # Output [bit 48]
            BP((15, 0, -1), OUTPUT),  # Output [bit 47]
            BP((16, 0, -1), OUTPUT),  # Output [bit 46]
            BP((17, 0, -1), OUTPUT),  # Output [bit 45]
            BP((0, 0, -1), OUTPUT),  # Output [bit 62]
            BP((18, 0, -1), OUTPUT),  # Output [bit 44]
            BP((19, 0, -1), OUTPUT),  # Output [bit 43]
            BP((20, 0, -1), OUTPUT),  # Output [bit 42]
            BP((21, 0, -1), OUTPUT),  # Output [bit 41]
            BP((22, 0, -1), OUTPUT),  # Output [bit 40]
            BP((23, 0, -1), OUTPUT),  # Output [bit 39]
            BP((24, 0, -1), OUTPUT),  # Output [bit 38]
            BP((25, 0, -1), OUTPUT),  # Output [bit 37]
            BP((26, 0, -1), OUTPUT),  # Output [bit 36]
            BP((27, 0, -1), OUTPUT),  # Output [bit 35]
            BP((1, 0, -1), OUTPUT),  # Output [bit 61]
            BP((28, 0, -1), OUTPUT),  # Output [bit 34]
            BP((29, 0, -1), OUTPUT),  # Output [bit 33]
            BP((30, 0, -1), OUTPUT),  # Output [bit 32]
            BP((33, 0, -1), OUTPUT),  # Output [bit 31]
            BP((34, 0, -1), OUTPUT),  # Output [bit 30]
            BP((35, 0, -1), OUTPUT),  # Output [bit 29]
            BP((36, 0, -1), OUTPUT),  # Output [bit 28]
            BP((37, 0, -1), OUTPUT),  # Output [bit 27]
            BP((38, 0, -1), OUTPUT),  # Output [bit 26]
            BP((39, 0, -1), OUTPUT),  # Output [bit 25]
            BP((2, 0, -1), OUTPUT),  # Output [bit 60]
            BP((40, 0, -1), OUTPUT),  # Output [bit 24]
            BP((41, 0, -1), OUTPUT),  # Output [bit 23]
            BP((42, 0, -1), OUTPUT),  # Output [bit 22]
            BP((43, 0, -1), OUTPUT),  # Output [bit 21]
            BP((44, 0, -1), OUTPUT),  # Output [bit 20]
            BP((45, 0, -1), OUTPUT),  # Output [bit 19]
            BP((46, 0, -1), OUTPUT),  # Output [bit 18]
            BP((47, 0, -1), OUTPUT),  # Output [bit 17]
            BP((48, 0, -1), OUTPUT),  # Output [bit 16]
            BP((49, 0, -1), OUTPUT),  # Output [bit 15]
            BP((3, 0, -1), OUTPUT),  # Output [bit 59]
            BP((50, 0, -1), OUTPUT),  # Output [bit 14]
            BP((51, 0, -1), OUTPUT),  # Output [bit 13]
            BP((52, 0, -1), OUTPUT),  # Output [bit 12]
            BP((53, 0, -1), OUTPUT),  # Output [bit 11]
            BP((54, 0, -1), OUTPUT),  # Output [bit 10]
            BP((55, 0, -1), OUTPUT),  # Output [bit 9]
            BP((56, 0, -1), OUTPUT),  # Output [bit 8]
            BP((57, 0, -1), OUTPUT),  # Output [bit 7]
            BP((58, 0, -1), OUTPUT),  # Output [bit 6]
            BP((59, 0, -1), OUTPUT),  # Output [bit 5]
            BP((4, 0, -1), OUTPUT),  # Output [bit 58]
            BP((60, 0, -1), OUTPUT),  # Output [bit 4]
            BP((61, 0, -1), OUTPUT),  # Output [bit 3]
            BP((62, 0, -1), OUTPUT),  # Output [bit 2]
            BP((63, 0, -1), OUTPUT),  # Output [bit 1]
            BP((64, 0, -1), OUTPUT),  # Output [bit 0]
            BP((5, 0, -1), OUTPUT),  # Output [bit 57]
            BP((6, 0, -1), OUTPUT),  # Output [bit 56]
            BP((7, 0, -1), OUTPUT),  # Output [bit 55]
        ]
    ),
}

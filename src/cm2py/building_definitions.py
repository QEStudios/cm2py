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
class BuildingProperties:
    blocks: list[tuple[tuple[int, int, int], IOType]]


definitions = {
    BuildingType.ASCII_KEY_INPUT: BuildingProperties(
        blocks=[
            ((7, 0, -3), IOType.OUTPUT),  # Ctrl
            ((-6, 0, -3), IOType.OUTPUT),  # ASCII [bit 7]
            ((-5, 0, -3), IOType.OUTPUT),  # ASCII [bit 6]
            ((-4, 0, -3), IOType.OUTPUT),  # ASCII [bit 5]
            ((-3, 0, -3), IOType.OUTPUT),  # ASCII [bit 4]
            ((-2, 0, -3), IOType.OUTPUT),  # ASCII [bit 3]
            ((-1, 0, -3), IOType.OUTPUT),  # ASCII [bit 2]
            ((0, 0, -3), IOType.OUTPUT),  # ASCII [bit 1]
            ((1, 0, -3), IOType.OUTPUT),  # ASCII [bit 0]
            ((3, 0, -3), IOType.OUTPUT),  # Pressed
            ((5, 0, -3), IOType.OUTPUT),  # Shift
        ],
    ),
    BuildingType.ASSEMBLER: BuildingProperties(
        blocks=[
            ((-17, 0, 4), IOType.INPUT),  # address [bit 11]
            ((-8, 0, 4), IOType.INPUT),  # address [bit 2]
            ((-7, 0, 4), IOType.INPUT),  # address [bit 1]
            ((-6, 0, 4), IOType.INPUT),  # address [bit 0]
            ((-16, 0, 4), IOType.INPUT),  # address [bit 10]
            ((-15, 0, 4), IOType.INPUT),  # address [bit 9]
            ((-14, 0, 4), IOType.INPUT),  # address [bit 8]
            ((-13, 0, 4), IOType.INPUT),  # address [bit 7]
            ((-12, 0, 4), IOType.INPUT),  # address [bit 6]
            ((-11, 0, 4), IOType.INPUT),  # address [bit 5]
            ((-10, 0, 4), IOType.INPUT),  # address [bit 4]
            ((-9, 0, 4), IOType.INPUT),  # address [bit 3]
            ((-17, 0, -4), IOType.OUTPUT),  # Byte 1 [bit 7]
            ((-16, 0, -4), IOType.OUTPUT),  # Byte 1 [bit 6]
            ((-15, 0, -4), IOType.OUTPUT),  # Byte 1 [bit 5]
            ((-14, 0, -4), IOType.OUTPUT),  # Byte 1 [bit 4]
            ((-13, 0, -4), IOType.OUTPUT),  # Byte 1 [bit 3]
            ((-12, 0, -4), IOType.OUTPUT),  # Byte 1 [bit 2]
            ((-11, 0, -4), IOType.OUTPUT),  # Byte 1 [bit 1]
            ((-10, 0, -4), IOType.OUTPUT),  # Byte 1 [bit 0]
            ((-8, 0, -4), IOType.OUTPUT),  # Byte 2 [bit 7]
            ((-7, 0, -4), IOType.OUTPUT),  # Byte 2 [bit 6]
            ((-6, 0, -4), IOType.OUTPUT),  # Byte 2 [bit 5]
            ((-5, 0, -4), IOType.OUTPUT),  # Byte 2 [bit 4]
            ((-4, 0, -4), IOType.OUTPUT),  # Byte 2 [bit 3]
            ((-3, 0, -4), IOType.OUTPUT),  # Byte 2 [bit 2]
            ((-2, 0, -4), IOType.OUTPUT),  # Byte 2 [bit 1]
            ((-1, 0, -4), IOType.OUTPUT),  # Byte 2 [bit 0]
            ((1, 0, -4), IOType.OUTPUT),  # Byte 3 [bit 7]
            ((2, 0, -4), IOType.OUTPUT),  # Byte 3 [bit 6]
            ((3, 0, -4), IOType.OUTPUT),  # Byte 3 [bit 5]
            ((4, 0, -4), IOType.OUTPUT),  # Byte 3 [bit 4]
            ((5, 0, -4), IOType.OUTPUT),  # Byte 3 [bit 3]
            ((6, 0, -4), IOType.OUTPUT),  # Byte 3 [bit 2]
            ((7, 0, -4), IOType.OUTPUT),  # Byte 3 [bit 1]
            ((8, 0, -4), IOType.OUTPUT),  # Byte 3 [bit 0]
            ((10, 0, -4), IOType.OUTPUT),  # Byte 4 [bit 7]
            ((11, 0, -4), IOType.OUTPUT),  # Byte 4 [bit 6]
            ((12, 0, -4), IOType.OUTPUT),  # Byte 4 [bit 5]
            ((13, 0, -4), IOType.OUTPUT),  # Byte 4 [bit 4]
            ((14, 0, -4), IOType.OUTPUT),  # Byte 4 [bit 3]
            ((15, 0, -4), IOType.OUTPUT),  # Byte 4 [bit 2]
            ((16, 0, -4), IOType.OUTPUT),  # Byte 4 [bit 1]
            ((17, 0, -4), IOType.OUTPUT),  # Byte 4 [bit 0]
        ]
    ),
    BuildingType.DIVIDER: BuildingProperties(
        blocks=[
            ((-1, 0, 7), IOType.INPUT),  # A [bit 15]
            ((7, 0, 7), IOType.INPUT),  # A [bit 6]
            ((8, 0, 7), IOType.INPUT),  # A [bit 5]
            ((9, 0, 7), IOType.INPUT),  # A [bit 4]
            ((10, 0, 7), IOType.INPUT),  # A [bit 3]
            ((11, 0, 7), IOType.INPUT),  # A [bit 2]
            ((12, 0, 7), IOType.INPUT),  # A [bit 1]
            ((13, 0, 7), IOType.INPUT),  # A [bit 0]
            ((0, 0, 7), IOType.INPUT),  # A [bit 14]
            ((1, 0, 7), IOType.INPUT),  # A [bit 13]
            ((2, 0, 7), IOType.INPUT),  # A [bit 12]
            ((3, 0, 7), IOType.INPUT),  # A [bit 11]
            ((3, 0, 7), IOType.INPUT),  # A [bit 10]
            ((4, 0, 7), IOType.INPUT),  # A [bit 9]
            ((5, 0, 7), IOType.INPUT),  # A [bit 8]
            ((6, 0, 7), IOType.INPUT),  # A [bit 7]
            ((16, 0, 7), IOType.INPUT),  # B [bit 15]
            ((25, 0, 7), IOType.INPUT),  # B [bit 6]
            ((26, 0, 7), IOType.INPUT),  # B [bit 5]
            ((27, 0, 7), IOType.INPUT),  # B [bit 4]
            ((28, 0, 7), IOType.INPUT),  # B [bit 3]
            ((29, 0, 7), IOType.INPUT),  # B [bit 2]
            ((30, 0, 7), IOType.INPUT),  # B [bit 1]
            ((31, 0, 7), IOType.INPUT),  # B [bit 0]
            ((17, 0, 7), IOType.INPUT),  # B [bit 14]
            ((18, 0, 7), IOType.INPUT),  # B [bit 13]
            ((19, 0, 7), IOType.INPUT),  # B [bit 12]
            ((20, 0, 7), IOType.INPUT),  # B [bit 11]
            ((21, 0, 7), IOType.INPUT),  # B [bit 10]
            ((22, 0, 7), IOType.INPUT),  # B [bit 9]
            ((23, 0, 7), IOType.INPUT),  # B [bit 8]
            ((24, 0, 7), IOType.INPUT),  # B [bit 7]
            ((-1, 0, -1), IOType.OUTPUT),  # Quotient [bit 15]
            ((7, 0, -1), IOType.OUTPUT),  # Quotient [bit 6]
            ((8, 0, -1), IOType.OUTPUT),  # Quotient [bit 5]
            ((9, 0, -1), IOType.OUTPUT),  # Quotient [bit 4]
            ((10, 0, -1), IOType.OUTPUT),  # Quotient [bit 3]
            ((11, 0, -1), IOType.OUTPUT),  # Quotient [bit 2]
            ((12, 0, -1), IOType.OUTPUT),  # Quotient [bit 1]
            ((13, 0, -1), IOType.OUTPUT),  # Quotient [bit 0]
            ((0, 0, -1), IOType.OUTPUT),  # Quotient [bit 14]
            ((1, 0, -1), IOType.OUTPUT),  # Quotient [bit 13]
            ((2, 0, -1), IOType.OUTPUT),  # Quotient [bit 12]
            ((3, 0, -1), IOType.OUTPUT),  # Quotient [bit 11]
            ((3, 0, -1), IOType.OUTPUT),  # Quotient [bit 10]
            ((4, 0, -1), IOType.OUTPUT),  # Quotient [bit 9]
            ((5, 0, -1), IOType.OUTPUT),  # Quotient [bit 8]
            ((6, 0, -1), IOType.OUTPUT),  # Quotient [bit 7]
            ((16, 0, -1), IOType.OUTPUT),  # Remainder [bit 15]
            ((25, 0, -1), IOType.OUTPUT),  # Remainder [bit 6]
            ((26, 0, -1), IOType.OUTPUT),  # Remainder [bit 5]
            ((27, 0, -1), IOType.OUTPUT),  # Remainder [bit 4]
            ((28, 0, -1), IOType.OUTPUT),  # Remainder [bit 3]
            ((29, 0, -1), IOType.OUTPUT),  # Remainder [bit 2]
            ((30, 0, -1), IOType.OUTPUT),  # Remainder [bit 1]
            ((31, 0, -1), IOType.OUTPUT),  # Remainder [bit 0]
            ((17, 0, -1), IOType.OUTPUT),  # Remainder [bit 14]
            ((18, 0, -1), IOType.OUTPUT),  # Remainder [bit 13]
            ((19, 0, -1), IOType.OUTPUT),  # Remainder [bit 12]
            ((20, 0, -1), IOType.OUTPUT),  # Remainder [bit 11]
            ((21, 0, -1), IOType.OUTPUT),  # Remainder [bit 10]
            ((22, 0, -1), IOType.OUTPUT),  # Remainder [bit 9]
            ((23, 0, -1), IOType.OUTPUT),  # Remainder [bit 8]
            ((24, 0, -1), IOType.OUTPUT),  # Remainder [bit 7]
        ]
    ),
    BuildingType.DOOR: BuildingProperties(
        blocks=[
            ((0, 7, 0), IOType.INPUT),
        ]
    ),
    BuildingType.DUAL_MEMORY: BuildingProperties(
        blocks=[
            ((-4, 0, 2), IOType.INPUT),  # Save Address [bit 7]
            ((-3, 0, 2), IOType.INPUT),  # Save Address [bit 6]
            ((-2, 0, 2), IOType.INPUT),  # Save Address [bit 5]
            ((-1, 0, 2), IOType.INPUT),  # Save Address [bit 4]
            ((0, 0, 2), IOType.INPUT),  # Save Address [bit 3]
            ((1, 0, 2), IOType.INPUT),  # Save Address [bit 2]
            ((2, 0, 2), IOType.INPUT),  # Save Address [bit 1]
            ((3, 0, 2), IOType.INPUT),  # Save Address [bit 0]
            ((-13, 0, 2), IOType.INPUT),  # Load Address [bit 7]
            ((-12, 0, 2), IOType.INPUT),  # Load Address [bit 6]
            ((-11, 0, 2), IOType.INPUT),  # Load Address [bit 5]
            ((-10, 0, 2), IOType.INPUT),  # Load Address [bit 4]
            ((-9, 0, 2), IOType.INPUT),  # Load Address [bit 3]
            ((-8, 0, 2), IOType.INPUT),  # Load Address [bit 2]
            ((-7, 0, 2), IOType.INPUT),  # Load Address [bit 1]
            ((-6, 0, 2), IOType.INPUT),  # Load Address [bit 0]
            ((-13, 0, -2), IOType.OUTPUT),  # Output [bit 7]
            ((-12, 0, -2), IOType.OUTPUT),  # Output [bit 6]
            ((-11, 0, -2), IOType.OUTPUT),  # Output [bit 5]
            ((-10, 0, -2), IOType.OUTPUT),  # Output [bit 4]
            ((-9, 0, -2), IOType.OUTPUT),  # Output [bit 3]
            ((-8, 0, -2), IOType.OUTPUT),  # Output [bit 2]
            ((-7, 0, -2), IOType.OUTPUT),  # Output [bit 1]
            ((-6, 0, -2), IOType.OUTPUT),  # Output [bit 0]
            ((5, 0, 2), IOType.INPUT),  # Value [bit 7]
            ((6, 0, 2), IOType.INPUT),  # Value [bit 6]
            ((7, 0, 2), IOType.INPUT),  # Value [bit 5]
            ((8, 0, 2), IOType.INPUT),  # Value [bit 4]
            ((9, 0, 2), IOType.INPUT),  # Value [bit 3]
            ((10, 0, 2), IOType.INPUT),  # Value [bit 2]
            ((11, 0, 2), IOType.INPUT),  # Value [bit 1]
            ((12, 0, 2), IOType.INPUT),  # Value [bit 0]
            ((14, 0, 2), IOType.INPUT),  # write
        ]
    ),
    BuildingType.FUNCTION_GENERATOR: BuildingProperties(
        blocks=[
            ((8, 0, 3), IOType.INPUT),  # Func [bit 1]
            ((9, 0, 3), IOType.INPUT),  # Func [bit 0]
            ((-1, 0, -2), IOType.OUTPUT),  # Output [bit 7]
            ((0, 0, -2), IOType.OUTPUT),  # Output [bit 6]
            ((1, 0, -2), IOType.OUTPUT),  # Output [bit 5]
            ((2, 0, -2), IOType.OUTPUT),  # Output [bit 4]
            ((3, 0, -2), IOType.OUTPUT),  # Output [bit 3]
            ((4, 0, -2), IOType.OUTPUT),  # Output [bit 2]
            ((5, 0, -2), IOType.OUTPUT),  # Output [bit 1]
            ((6, 0, -2), IOType.OUTPUT),  # Output [bit 0]
            ((-1, 0, 3), IOType.INPUT),  # X [bit 7]
            ((0, 0, 3), IOType.INPUT),  # X [bit 6]
            ((1, 0, 3), IOType.INPUT),  # X [bit 5]
            ((2, 0, 3), IOType.INPUT),  # X [bit 4]
            ((3, 0, 3), IOType.INPUT),  # X [bit 3]
            ((4, 0, 3), IOType.INPUT),  # X [bit 2]
            ((5, 0, 3), IOType.INPUT),  # X [bit 1]
            ((6, 0, 3), IOType.INPUT),  # X [bit 0]
        ]
    ),
    BuildingType.GRAPH: BuildingProperties(
        blocks=[
            ((-4, 0, 4), IOType.INPUT),  # Input [bit 7]
            ((-3, 0, 4), IOType.INPUT),  # Input [bit 7]
            ((-2, 0, 4), IOType.INPUT),  # Input [bit 7]
            ((-1, 0, 4), IOType.INPUT),  # Input [bit 7]
            ((0, 0, 4), IOType.INPUT),  # Input [bit 7]
            ((1, 0, 4), IOType.INPUT),  # Input [bit 7]
            ((2, 0, 4), IOType.INPUT),  # Input [bit 7]
            ((3, 0, 4), IOType.INPUT),  # Input [bit 7]
        ]
    ),
    BuildingType.HUGE_MEMORY: BuildingProperties(
        blocks=[
            ((-17, 0, 3), IOType.INPUT),  # address [bit 15]
            ((-8, 0, 3), IOType.INPUT),  # address [bit 6]
            ((-7, 0, 3), IOType.INPUT),  # address [bit 5]
            ((-6, 0, 3), IOType.INPUT),  # address [bit 4]
            ((-5, 0, 3), IOType.INPUT),  # address [bit 3]
            ((-4, 0, 3), IOType.INPUT),  # address [bit 2]
            ((-3, 0, 3), IOType.INPUT),  # address [bit 1]
            ((-2, 0, 3), IOType.INPUT),  # address [bit 0]
            ((-16, 0, 3), IOType.INPUT),  # address [bit 14]
            ((-15, 0, 3), IOType.INPUT),  # address [bit 13]
            ((-14, 0, 3), IOType.INPUT),  # address [bit 12]
            ((-13, 0, 3), IOType.INPUT),  # address [bit 11]
            ((-12, 0, 3), IOType.INPUT),  # address [bit 10]
            ((-11, 0, 3), IOType.INPUT),  # address [bit 9]
            ((-10, 0, 3), IOType.INPUT),  # address [bit 8]
            ((-9, 0, 3), IOType.INPUT),  # address [bit 7]
            ((-17, 0, -3), IOType.OUTPUT),  # output [bit 15]
            ((-8, 0, -3), IOType.OUTPUT),  # output [bit 6]
            ((-7, 0, -3), IOType.OUTPUT),  # output [bit 5]
            ((-6, 0, -3), IOType.OUTPUT),  # output [bit 4]
            ((-5, 0, -3), IOType.OUTPUT),  # output [bit 3]
            ((-4, 0, -3), IOType.OUTPUT),  # output [bit 2]
            ((-3, 0, -3), IOType.OUTPUT),  # output [bit 1]
            ((-2, 0, -3), IOType.OUTPUT),  # output [bit 0]
            ((-16, 0, -3), IOType.OUTPUT),  # output [bit 14]
            ((-15, 0, -3), IOType.OUTPUT),  # output [bit 13]
            ((-14, 0, -3), IOType.OUTPUT),  # output [bit 12]
            ((-13, 0, -3), IOType.OUTPUT),  # output [bit 11]
            ((-12, 0, -3), IOType.OUTPUT),  # output [bit 10]
            ((-11, 0, -3), IOType.OUTPUT),  # output [bit 9]
            ((-10, 0, -3), IOType.OUTPUT),  # output [bit 8]
            ((-9, 0, -3), IOType.OUTPUT),  # output [bit 7]
            ((1, 0, 3), IOType.INPUT),  # value [bit 15]
            ((10, 0, 3), IOType.INPUT),  # value [bit 6]
            ((11, 0, 3), IOType.INPUT),  # value [bit 5]
            ((12, 0, 3), IOType.INPUT),  # value [bit 4]
            ((13, 0, 3), IOType.INPUT),  # value [bit 3]
            ((14, 0, 3), IOType.INPUT),  # value [bit 2]
            ((15, 0, 3), IOType.INPUT),  # value [bit 1]
            ((16, 0, 3), IOType.INPUT),  # value [bit 0]
            ((2, 0, 3), IOType.INPUT),  # value [bit 14]
            ((3, 0, 3), IOType.INPUT),  # value [bit 13]
            ((4, 0, 3), IOType.INPUT),  # value [bit 12]
            ((5, 0, 3), IOType.INPUT),  # value [bit 11]
            ((6, 0, 3), IOType.INPUT),  # value [bit 10]
            ((7, 0, 3), IOType.INPUT),  # value [bit 9]
            ((8, 0, 3), IOType.INPUT),  # value [bit 8]
            ((9, 0, 3), IOType.INPUT),  # value [bit 7]
            ((18, 0, 3), IOType.INPUT),  # write
        ]
    ),
    BuildingType.INTEGRATED_CIRCUIT: BuildingProperties(
        blocks=[
            ((0, 0, 7), IOType.INPUT),  # input [bit 31]
            ((9, 0, 7), IOType.INPUT),  # input [bit 22]
            ((10, 0, 7), IOType.INPUT),  # input [bit 21]
            ((11, 0, 7), IOType.INPUT),  # input [bit 20]
            ((12, 0, 7), IOType.INPUT),  # input [bit 19]
            ((13, 0, 7), IOType.INPUT),  # input [bit 18]
            ((14, 0, 7), IOType.INPUT),  # input [bit 17]
            ((15, 0, 7), IOType.INPUT),  # input [bit 16]
            ((16, 0, 7), IOType.INPUT),  # input [bit 15]
            ((17, 0, 7), IOType.INPUT),  # input [bit 14]
            ((18, 0, 7), IOType.INPUT),  # input [bit 13]
            ((1, 0, 7), IOType.INPUT),  # input [bit 30]
            ((19, 0, 7), IOType.INPUT),  # input [bit 12]
            ((20, 0, 7), IOType.INPUT),  # input [bit 11]
            ((21, 0, 7), IOType.INPUT),  # input [bit 10]
            ((22, 0, 7), IOType.INPUT),  # input [bit 9]
            ((23, 0, 7), IOType.INPUT),  # input [bit 8]
            ((24, 0, 7), IOType.INPUT),  # input [bit 7]
            ((25, 0, 7), IOType.INPUT),  # input [bit 6]
            ((26, 0, 7), IOType.INPUT),  # input [bit 5]
            ((27, 0, 7), IOType.INPUT),  # input [bit 4]
            ((28, 0, 7), IOType.INPUT),  # input [bit 3]
            ((2, 0, 7), IOType.INPUT),  # input [bit 29]
            ((29, 0, 7), IOType.INPUT),  # input [bit 2]
            ((30, 0, 7), IOType.INPUT),  # input [bit 1]
            ((31, 0, 7), IOType.INPUT),  # input [bit 0]
            ((3, 0, 7), IOType.INPUT),  # input [bit 28]
            ((4, 0, 7), IOType.INPUT),  # input [bit 27]
            ((5, 0, 7), IOType.INPUT),  # input [bit 26]
            ((6, 0, 7), IOType.INPUT),  # input [bit 25]
            ((7, 0, 7), IOType.INPUT),  # input [bit 24]
            ((8, 0, 7), IOType.INPUT),  # input [bit 23]
            ((0, 0, -1), IOType.OUTPUT),  # output [bit 31]
            ((9, 0, -1), IOType.OUTPUT),  # output [bit 22]
            ((10, 0, -1), IOType.OUTPUT),  # output [bit 21]
            ((11, 0, -1), IOType.OUTPUT),  # output [bit 20]
            ((12, 0, -1), IOType.OUTPUT),  # output [bit 19]
            ((13, 0, -1), IOType.OUTPUT),  # output [bit 18]
            ((14, 0, -1), IOType.OUTPUT),  # output [bit 17]
            ((15, 0, -1), IOType.OUTPUT),  # output [bit 16]
            ((16, 0, -1), IOType.OUTPUT),  # output [bit 15]
            ((17, 0, -1), IOType.OUTPUT),  # output [bit 14]
            ((18, 0, -1), IOType.OUTPUT),  # output [bit 13]
            ((1, 0, -1), IOType.OUTPUT),  # output [bit 30]
            ((19, 0, -1), IOType.OUTPUT),  # output [bit 12]
            ((20, 0, -1), IOType.OUTPUT),  # output [bit 11]
            ((21, 0, -1), IOType.OUTPUT),  # output [bit 10]
            ((22, 0, -1), IOType.OUTPUT),  # output [bit 9]
            ((23, 0, -1), IOType.OUTPUT),  # output [bit 8]
            ((24, 0, -1), IOType.OUTPUT),  # output [bit 7]
            ((25, 0, -1), IOType.OUTPUT),  # output [bit 6]
            ((26, 0, -1), IOType.OUTPUT),  # output [bit 5]
            ((27, 0, -1), IOType.OUTPUT),  # output [bit 4]
            ((28, 0, -1), IOType.OUTPUT),  # output [bit 3]
            ((2, 0, -1), IOType.OUTPUT),  # output [bit 29]
            ((29, 0, -1), IOType.OUTPUT),  # output [bit 2]
            ((30, 0, -1), IOType.OUTPUT),  # output [bit 1]
            ((31, 0, -1), IOType.OUTPUT),  # output [bit 0]
            ((3, 0, -1), IOType.OUTPUT),  # output [bit 28]
            ((4, 0, -1), IOType.OUTPUT),  # output [bit 27]
            ((5, 0, -1), IOType.OUTPUT),  # output [bit 26]
            ((6, 0, -1), IOType.OUTPUT),  # output [bit 25]
            ((7, 0, -1), IOType.OUTPUT),  # output [bit 24]
            ((8, 0, -1), IOType.OUTPUT),  # output [bit 23]
        ]
    ),
    BuildingType.KEY_INPUT: BuildingProperties(
        blocks=[
            ((-18, 0, -4), IOType.OUTPUT),  # A
            ((-9, 0, -4), IOType.OUTPUT),  # J
            ((-8, 0, -4), IOType.OUTPUT),  # K
            ((-7, 0, -4), IOType.OUTPUT),  # L
            ((-6, 0, -4), IOType.OUTPUT),  # M
            ((-5, 0, -4), IOType.OUTPUT),  # N
            ((-4, 0, -4), IOType.OUTPUT),  # O
            ((-3, 0, -4), IOType.OUTPUT),  # P
            ((-2, 0, -4), IOType.OUTPUT),  # Q
            ((-1, 0, -4), IOType.OUTPUT),  # R
            ((0, 0, -4), IOType.OUTPUT),  # S
            ((-17, 0, -4), IOType.OUTPUT),  # B
            ((1, 0, -4), IOType.OUTPUT),  # T
            ((2, 0, -4), IOType.OUTPUT),  # U
            ((3, 0, -4), IOType.OUTPUT),  # V
            ((4, 0, -4), IOType.OUTPUT),  # W
            ((5, 0, -4), IOType.OUTPUT),  # X
            ((6, 0, -4), IOType.OUTPUT),  # Y
            ((7, 0, -4), IOType.OUTPUT),  # Z
            ((8, 0, -4), IOType.OUTPUT),  # 1
            ((9, 0, -4), IOType.OUTPUT),  # 2
            ((-16, 0, -4), IOType.OUTPUT),  # C
            ((10, 0, -4), IOType.OUTPUT),  # 3
            ((11, 0, -4), IOType.OUTPUT),  # 4
            ((12, 0, -4), IOType.OUTPUT),  # 5
            ((13, 0, -4), IOType.OUTPUT),  # 6
            ((14, 0, -4), IOType.OUTPUT),  # 7
            ((15, 0, -4), IOType.OUTPUT),  # 8
            ((16, 0, -4), IOType.OUTPUT),  # 9
            ((17, 0, -4), IOType.OUTPUT),  # 0
            ((18, 0, -4), IOType.OUTPUT),  # space
            ((-15, 0, -4), IOType.OUTPUT),  # D
            ((-14, 0, -4), IOType.OUTPUT),  # E
            ((-13, 0, -4), IOType.OUTPUT),  # F
            ((-12, 0, -4), IOType.OUTPUT),  # G
            ((-11, 0, -4), IOType.OUTPUT),  # H
            ((-10, 0, -4), IOType.OUTPUT),  # I
        ]
    ),
    BuildingType.LARGE_RGB_DISPLAY: BuildingProperties(
        blocks=[
            ((10, 0, 18), IOType.INPUT),  # B [bit 5]
            ((11, 0, 18), IOType.INPUT),  # B [bit 4]
            ((12, 0, 18), IOType.INPUT),  # B [bit 3]
            ((13, 0, 18), IOType.INPUT),  # B [bit 2]
            ((14, 0, 18), IOType.INPUT),  # B [bit 1]
            ((15, 0, 18), IOType.INPUT),  # B [bit 0]
            ((3, 0, 18), IOType.INPUT),  # G [bit 5]
            ((4, 0, 18), IOType.INPUT),  # G [bit 4]
            ((5, 0, 18), IOType.INPUT),  # G [bit 3]
            ((6, 0, 18), IOType.INPUT),  # G [bit 2]
            ((7, 0, 18), IOType.INPUT),  # G [bit 1]
            ((8, 0, 18), IOType.INPUT),  # G [bit 0]
            ((-4, 0, 18), IOType.INPUT),  # R [bit 5]
            ((-3, 0, 18), IOType.INPUT),  # R [bit 4]
            ((-2, 0, 18), IOType.INPUT),  # R [bit 3]
            ((-1, 0, 18), IOType.INPUT),  # R [bit 2]
            ((0, 0, 18), IOType.INPUT),  # R [bit 1]
            ((1, 0, 18), IOType.INPUT),  # R [bit 0]
            ((17, 0, 18), IOType.INPUT),  # Reset
            ((19, 0, 18), IOType.INPUT),  # Write
            ((-20, 0, 18), IOType.INPUT),  # X [bit 6]
            ((-19, 0, 18), IOType.INPUT),  # X [bit 5]
            ((-18, 0, 18), IOType.INPUT),  # X [bit 4]
            ((-17, 0, 18), IOType.INPUT),  # X [bit 3]
            ((-16, 0, 18), IOType.INPUT),  # X [bit 2]
            ((-15, 0, 18), IOType.INPUT),  # X [bit 1]
            ((-14, 0, 18), IOType.INPUT),  # X [bit 0]
            ((-12, 0, 18), IOType.INPUT),  # Y [bit 6]
            ((-11, 0, 18), IOType.INPUT),  # Y [bit 5]
            ((-10, 0, 18), IOType.INPUT),  # Y [bit 4]
            ((-9, 0, 18), IOType.INPUT),  # Y [bit 3]
            ((-8, 0, 18), IOType.INPUT),  # Y [bit 2]
            ((-7, 0, 18), IOType.INPUT),  # Y [bit 1]
            ((-6, 0, 18), IOType.INPUT),  # Y [bit 0]
        ]
    ),
    BuildingType.MASS_MEMORY: BuildingProperties(
        blocks=[
            ((-11, 0, 2), IOType.INPUT),  # address [bit 11]
            ((-2, 0, 2), IOType.INPUT),  # address [bit 2]
            ((-1, 0, 2), IOType.INPUT),  # address [bit 1]
            ((0, 0, 2), IOType.INPUT),  # address [bit 0]
            ((-10, 0, 2), IOType.INPUT),  # address [bit 10]
            ((-9, 0, 2), IOType.INPUT),  # address [bit 9]
            ((-8, 0, 2), IOType.INPUT),  # address [bit 8]
            ((-7, 0, 2), IOType.INPUT),  # address [bit 7]
            ((-6, 0, 2), IOType.INPUT),  # address [bit 6]
            ((-5, 0, 2), IOType.INPUT),  # address [bit 5]
            ((-4, 0, 2), IOType.INPUT),  # address [bit 4]
            ((-3, 0, 2), IOType.INPUT),  # address [bit 3]
            ((-11, 0, -2), IOType.OUTPUT),  # output [bit 7]
            ((-10, 0, -2), IOType.OUTPUT),  # output [bit 6]
            ((-9, 0, -2), IOType.OUTPUT),  # output [bit 5]
            ((-8, 0, -2), IOType.OUTPUT),  # output [bit 4]
            ((-7, 0, -2), IOType.OUTPUT),  # output [bit 3]
            ((-6, 0, -2), IOType.OUTPUT),  # output [bit 2]
            ((-5, 0, -2), IOType.OUTPUT),  # output [bit 1]
            ((-4, 0, -2), IOType.OUTPUT),  # output [bit 0]
            ((2, 0, 2), IOType.INPUT),  # value [bit 7]
            ((3, 0, 2), IOType.INPUT),  # value [bit 6]
            ((4, 0, 2), IOType.INPUT),  # value [bit 5]
            ((5, 0, 2), IOType.INPUT),  # value [bit 4]
            ((6, 0, 2), IOType.INPUT),  # value [bit 3]
            ((7, 0, 2), IOType.INPUT),  # value [bit 2]
            ((8, 0, 2), IOType.INPUT),  # value [bit 1]
            ((9, 0, 2), IOType.INPUT),  # value [bit 0]
            ((11, 0, 2), IOType.INPUT),  # write
        ]
    ),
    BuildingType.MASSIVE_MEMORY: BuildingProperties(
        blocks=[
            ((-15, 0, 2), IOType.INPUT),  # address [bit 11]
            ((-6, 0, 2), IOType.INPUT),  # address [bit 2]
            ((-5, 0, 2), IOType.INPUT),  # address [bit 1]
            ((-4, 0, 2), IOType.INPUT),  # address [bit 0]
            ((-14, 0, 2), IOType.INPUT),  # address [bit 10]
            ((-13, 0, 2), IOType.INPUT),  # address [bit 9]
            ((-12, 0, 2), IOType.INPUT),  # address [bit 8]
            ((-11, 0, 2), IOType.INPUT),  # address [bit 7]
            ((-10, 0, 2), IOType.INPUT),  # address [bit 6]
            ((-9, 0, 2), IOType.INPUT),  # address [bit 5]
            ((-8, 0, 2), IOType.INPUT),  # address [bit 4]
            ((-7, 0, 2), IOType.INPUT),  # address [bit 3]
            ((-15, 0, -2), IOType.OUTPUT),  # output [bit 15]
            ((-6, 0, -2), IOType.OUTPUT),  # output [bit 6]
            ((-5, 0, -2), IOType.OUTPUT),  # output [bit 5]
            ((-4, 0, -2), IOType.OUTPUT),  # output [bit 4]
            ((-3, 0, -2), IOType.OUTPUT),  # output [bit 3]
            ((-2, 0, -2), IOType.OUTPUT),  # output [bit 2]
            ((-1, 0, -2), IOType.OUTPUT),  # output [bit 1]
            ((0, 0, -2), IOType.OUTPUT),  # output [bit 0]
            ((-14, 0, -2), IOType.OUTPUT),  # output [bit 14]
            ((-13, 0, -2), IOType.OUTPUT),  # output [bit 13]
            ((-12, 0, -2), IOType.OUTPUT),  # output [bit 12]
            ((-11, 0, -2), IOType.OUTPUT),  # output [bit 11]
            ((-10, 0, -2), IOType.OUTPUT),  # output [bit 10]
            ((-9, 0, -2), IOType.OUTPUT),  # output [bit 9]
            ((-8, 0, -2), IOType.OUTPUT),  # output [bit 8]
            ((-7, 0, -2), IOType.OUTPUT),  # output [bit 7]
            ((-2, 0, 2), IOType.INPUT),  # value [bit 15]
            ((7, 0, 2), IOType.INPUT),  # value [bit 6]
            ((8, 0, 2), IOType.INPUT),  # value [bit 5]
            ((9, 0, 2), IOType.INPUT),  # value [bit 4]
            ((10, 0, 2), IOType.INPUT),  # value [bit 3]
            ((11, 0, 2), IOType.INPUT),  # value [bit 2]
            ((12, 0, 2), IOType.INPUT),  # value [bit 1]
            ((13, 0, 2), IOType.INPUT),  # value [bit 0]
            ((-1, 0, 2), IOType.INPUT),  # value [bit 14]
            ((0, 0, 2), IOType.INPUT),  # value [bit 13]
            ((1, 0, 2), IOType.INPUT),  # value [bit 12]
            ((2, 0, 2), IOType.INPUT),  # value [bit 11]
            ((3, 0, 2), IOType.INPUT),  # value [bit 10]
            ((4, 0, 2), IOType.INPUT),  # value [bit 9]
            ((5, 0, 2), IOType.INPUT),  # value [bit 8]
            ((6, 0, 2), IOType.INPUT),  # value [bit 7]
            ((15, 0, 2), IOType.INPUT),  # write
        ]
    ),
    BuildingType.MULTIPLIER: BuildingProperties(
        blocks=[
            ((-1, 0, 7), IOType.INPUT),  # A [bit 15]
            ((7, 0, 7), IOType.INPUT),  # A [bit 6]
            ((8, 0, 7), IOType.INPUT),  # A [bit 5]
            ((9, 0, 7), IOType.INPUT),  # A [bit 4]
            ((10, 0, 7), IOType.INPUT),  # A [bit 3]
            ((11, 0, 7), IOType.INPUT),  # A [bit 2]
            ((12, 0, 7), IOType.INPUT),  # A [bit 1]
            ((13, 0, 7), IOType.INPUT),  # A [bit 0]
            ((0, 0, 7), IOType.INPUT),  # A [bit 14]
            ((1, 0, 7), IOType.INPUT),  # A [bit 13]
            ((2, 0, 7), IOType.INPUT),  # A [bit 12]
            ((3, 0, 7), IOType.INPUT),  # A [bit 11]
            ((3, 0, 7), IOType.INPUT),  # A [bit 10]
            ((4, 0, 7), IOType.INPUT),  # A [bit 9]
            ((5, 0, 7), IOType.INPUT),  # A [bit 8]
            ((6, 0, 7), IOType.INPUT),  # A [bit 7]
            ((16, 0, 7), IOType.INPUT),  # B [bit 15]
            ((25, 0, 7), IOType.INPUT),  # B [bit 6]
            ((26, 0, 7), IOType.INPUT),  # B [bit 5]
            ((27, 0, 7), IOType.INPUT),  # B [bit 4]
            ((28, 0, 7), IOType.INPUT),  # B [bit 3]
            ((29, 0, 7), IOType.INPUT),  # B [bit 2]
            ((30, 0, 7), IOType.INPUT),  # B [bit 1]
            ((31, 0, 7), IOType.INPUT),  # B [bit 0]
            ((17, 0, 7), IOType.INPUT),  # B [bit 14]
            ((18, 0, 7), IOType.INPUT),  # B [bit 13]
            ((19, 0, 7), IOType.INPUT),  # B [bit 12]
            ((20, 0, 7), IOType.INPUT),  # B [bit 11]
            ((21, 0, 7), IOType.INPUT),  # B [bit 10]
            ((22, 0, 7), IOType.INPUT),  # B [bit 9]
            ((23, 0, 7), IOType.INPUT),  # B [bit 8]
            ((24, 0, 7), IOType.INPUT),  # B [bit 7]
            ((-1, 0, -1), IOType.OUTPUT),  # Output [bit 31]
            ((7, 0, -1), IOType.OUTPUT),  # Output [bit 22]
            ((8, 0, -1), IOType.OUTPUT),  # Output [bit 21]
            ((9, 0, -1), IOType.OUTPUT),  # Output [bit 20]
            ((10, 0, -1), IOType.OUTPUT),  # Output [bit 19]
            ((11, 0, -1), IOType.OUTPUT),  # Output [bit 18]
            ((12, 0, -1), IOType.OUTPUT),  # Output [bit 17]
            ((13, 0, -1), IOType.OUTPUT),  # Output [bit 16]
            ((16, 0, -1), IOType.OUTPUT),  # Output [bit 15]
            ((17, 0, -1), IOType.OUTPUT),  # Output [bit 14]
            ((18, 0, -1), IOType.OUTPUT),  # Output [bit 13]
            ((0, 0, -1), IOType.OUTPUT),  # Output [bit 30]
            ((19, 0, -1), IOType.OUTPUT),  # Output [bit 12]
            ((20, 0, -1), IOType.OUTPUT),  # Output [bit 11]
            ((21, 0, -1), IOType.OUTPUT),  # Output [bit 10]
            ((22, 0, -1), IOType.OUTPUT),  # Output [bit 9]
            ((23, 0, -1), IOType.OUTPUT),  # Output [bit 8]
            ((24, 0, -1), IOType.OUTPUT),  # Output [bit 7]
            ((25, 0, -1), IOType.OUTPUT),  # Output [bit 6]
            ((26, 0, -1), IOType.OUTPUT),  # Output [bit 5]
            ((27, 0, -1), IOType.OUTPUT),  # Output [bit 4]
            ((28, 0, -1), IOType.OUTPUT),  # Output [bit 3]
            ((1, 0, -1), IOType.OUTPUT),  # Output [bit 29]
            ((29, 0, -1), IOType.OUTPUT),  # Output [bit 2]
            ((30, 0, -1), IOType.OUTPUT),  # Output [bit 1]
            ((31, 0, -1), IOType.OUTPUT),  # Output [bit 0]
            ((2, 0, -1), IOType.OUTPUT),  # Output [bit 28]
            ((3, 0, -1), IOType.OUTPUT),  # Output [bit 27]
            ((3, 0, -1), IOType.OUTPUT),  # Output [bit 26]
            ((4, 0, -1), IOType.OUTPUT),  # Output [bit 25]
            ((5, 0, -1), IOType.OUTPUT),  # Output [bit 24]
            ((6, 0, -1), IOType.OUTPUT),  # Output [bit 23]
        ]
    ),
    BuildingType.N_TRANSISTOR: BuildingProperties(
        blocks=[
            ((1, 0, 0), IOType.BIDIRECTIONAL),  # Right
            ((0, 0, 1), IOType.INPUT),  # Bottom
            ((-1, 0, 0), IOType.BIDIRECTIONAL),  # Left
        ]
    ),
    BuildingType.P_TRANSISTOR: BuildingProperties(
        blocks=[
            ((1, 0, 0), IOType.BIDIRECTIONAL),  # Right
            ((0, 0, 1), IOType.INPUT),  # Bottom
            ((-1, 0, 0), IOType.BIDIRECTIONAL),  # Left
        ]
    ),
    BuildingType.PIXEL_DISPLAY: BuildingProperties(
        blocks=[
            ((4, 0, 10), IOType.INPUT),  # Pixel
            ((6, 0, 10), IOType.INPUT),  # Reset
            ((8, 0, 10), IOType.INPUT),  # Write
            ((-8, 0, 10), IOType.INPUT),  # X [bit 4]
            ((-7, 0, 10), IOType.INPUT),  # X [bit 3]
            ((-6, 0, 10), IOType.INPUT),  # X [bit 2]
            ((-5, 0, 10), IOType.INPUT),  # X [bit 1]
            ((-4, 0, 10), IOType.INPUT),  # X [bit 0]
            ((-2, 0, 10), IOType.INPUT),  # Y [bit 4]
            ((-1, 0, 10), IOType.INPUT),  # Y [bit 3]
            ((0, 0, 10), IOType.INPUT),  # Y [bit 2]
            ((1, 0, 10), IOType.INPUT),  # Y [bit 1]
            ((2, 0, 10), IOType.INPUT),  # Y [bit 0]
        ]
    ),
    BuildingType.QWERTY_KEY_INPUT: BuildingProperties(
        blocks=[
            ((2, 1, -4), IOType.OUTPUT),  # 0
            ((-7, 1, -4), IOType.OUTPUT),  # 1
            ((-6, 1, -4), IOType.OUTPUT),  # 2
            ((-5, 1, -4), IOType.OUTPUT),  # 3
            ((-4, 1, -4), IOType.OUTPUT),  # 4
            ((-3, 1, -4), IOType.OUTPUT),  # 5
            ((-2, 1, -4), IOType.OUTPUT),  # 6
            ((-1, 1, -4), IOType.OUTPUT),  # 7
            ((0, 1, -4), IOType.OUTPUT),  # 8
            ((1, 1, -4), IOType.OUTPUT),  # 9
            ((-7, 1, -2), IOType.OUTPUT),  # A
            ((-7, 1, 0), IOType.OUTPUT),  # left alt
            ((2, 1, 0), IOType.OUTPUT),  # right alt
            ((3, 1, -2), IOType.OUTPUT),  # '
            ((-3, 1, -1), IOType.OUTPUT),  # B
            ((5, 1, -3), IOType.OUTPUT),  # \
            ((5, 1, -4), IOType.OUTPUT),  # backspace
            ((-5, 1, -1), IOType.OUTPUT),  # C
            ((-8, 1, -2), IOType.OUTPUT),  # caps lock
            ((0, 1, -1), IOType.OUTPUT),  # ,
            ((-8, 1, 0), IOType.OUTPUT),  # left ctrl
            ((3, 1, 0), IOType.OUTPUT),  # right ctrl
            ((-5, 1, -2), IOType.OUTPUT),  # D
            ((7, 1, 0), IOType.OUTPUT),  # down
            ((-5, 1, -3), IOType.OUTPUT),  # E
            ((4, 1, -2), IOType.OUTPUT),  # enter
            ((4, 1, -4), IOType.OUTPUT),  # =
            ((-4, 1, -2), IOType.OUTPUT),  # F
            ((-3, 1, -2), IOType.OUTPUT),  # G
            ((-2, 1, -2), IOType.OUTPUT),  # H
            ((0, 1, -3), IOType.OUTPUT),  # I
            ((-1, 1, -2), IOType.OUTPUT),  # J
            ((0, 1, -2), IOType.OUTPUT),  # K
            ((1, 1, -2), IOType.OUTPUT),  # L
            ((6, 1, 0), IOType.OUTPUT),  # left
            ((-1, 1, -1), IOType.OUTPUT),  # M
            ((3, 1, -4), IOType.OUTPUT),  # -
            ((-2, 1, -1), IOType.OUTPUT),  # N
            ((1, 1, -3), IOType.OUTPUT),  # O
            ((2, 1, -3), IOType.OUTPUT),  # P
            ((1, 1, -1), IOType.OUTPUT),  # .
            ((-7, 1, -3), IOType.OUTPUT),  # Q
            ((-4, 1, -3), IOType.OUTPUT),  # R
            ((8, 1, 0), IOType.OUTPUT),  # right
            ((-6, 1, -2), IOType.OUTPUT),  # S
            ((2, 1, -2), IOType.OUTPUT),  # ;
            ((-8, 1, -1), IOType.OUTPUT),  # left shift
            ((3, 1, -1), IOType.OUTPUT),  # right shift
            ((2, 1, -1), IOType.OUTPUT),  # /
            ((-2, 1, 0), IOType.OUTPUT),  # space
            ((3, 1, -3), IOType.OUTPUT),  # [
            ((4, 1, -3), IOType.OUTPUT),  # ]
            ((-3, 1, -3), IOType.OUTPUT),  # T
            ((-8, 1, -3), IOType.OUTPUT),  # tab
            ((-8, 1, -4), IOType.OUTPUT),  # `
            ((-1, 1, -3), IOType.OUTPUT),  # U
            ((7, 1, -1), IOType.OUTPUT),  # up
            ((-4, 1, -1), IOType.OUTPUT),  # V
            ((-6, 1, -3), IOType.OUTPUT),  # W
            ((-6, 1, -1), IOType.OUTPUT),  # X
            ((-2, 1, -3), IOType.OUTPUT),  # Y
            ((-7, 1, -1), IOType.OUTPUT),  # Z
        ]
    ),
    BuildingType.RGB_DISPLAY: BuildingProperties(
        blocks=[
            ((8, 0, 18), IOType.INPUT),  # B [bit 3]
            ((9, 0, 18), IOType.INPUT),  # B [bit 2]
            ((10, 0, 18), IOType.INPUT),  # B [bit 1]
            ((11, 0, 18), IOType.INPUT),  # B [bit 0]
            ((3, 0, 18), IOType.INPUT),  # G [bit 3]
            ((4, 0, 18), IOType.INPUT),  # G [bit 2]
            ((5, 0, 18), IOType.INPUT),  # G [bit 1]
            ((6, 0, 18), IOType.INPUT),  # G [bit 0]
            ((-2, 0, 18), IOType.INPUT),  # R [bit 3]
            ((-1, 0, 18), IOType.INPUT),  # R [bit 2]
            ((0, 0, 18), IOType.INPUT),  # R [bit 1]
            ((1, 0, 18), IOType.INPUT),  # R [bit 0]
            ((3, 0, 18), IOType.INPUT),  # G [bit 3]
            ((4, 0, 18), IOType.INPUT),  # G [bit 2]
            ((5, 0, 18), IOType.INPUT),  # G [bit 1]
            ((6, 0, 18), IOType.INPUT),  # G [bit 0]
            ((13, 0, 18), IOType.INPUT),  # Reset
            ((14, 0, 18), IOType.INPUT),  # Write
            ((-14, 0, 18), IOType.INPUT),  # X [bit 4]
            ((-13, 0, 18), IOType.INPUT),  # X [bit 3]
            ((-12, 0, 18), IOType.INPUT),  # X [bit 2]
            ((-11, 0, 18), IOType.INPUT),  # X [bit 1]
            ((-10, 0, 18), IOType.INPUT),  # X [bit 0]
            ((-8, 0, 18), IOType.INPUT),  # Y [bit 4]
            ((-7, 0, 18), IOType.INPUT),  # Y [bit 3]
            ((-6, 0, 18), IOType.INPUT),  # Y [bit 2]
            ((-5, 0, 18), IOType.INPUT),  # Y [bit 1]
            ((-4, 0, 18), IOType.INPUT),  # Y [bit 0]
        ]
    ),
    BuildingType.REAL_TIME_CLOCK: BuildingProperties(
        blocks=[
            ((9, 0, -1), IOType.INPUT),  # CHG
            ((0, 0, -1), IOType.INPUT),  # +/-
            ((12, 0, -1), IOType.INPUT),  # HOL
            ((10, 0, -1), IOType.INPUT),  # RST
            ((11, 0, -1), IOType.INPUT),  # SYN
            ((5, 0, -1), IOType.INPUT),  # 1D input
            ((4, 0, -1), IOType.INPUT),  # 1h input
            ((3, 0, -1), IOType.INPUT),  # 1m input
            ((2, 0, -1), IOType.INPUT),  # 1s input
            ((31, 0, -1), IOType.OUTPUT),  # 1D output
            ((30, 0, -1), IOType.OUTPUT),  # 1h output
            ((29, 0, -1), IOType.OUTPUT),  # 1m output
            ((28, 0, -1), IOType.OUTPUT),  # 1s output
            ((31, 0, 4), IOType.OUTPUT),  # Timestamp [bit 0]
            ((22, 0, 4), IOType.OUTPUT),  # Timestamp [bit 9]
            ((21, 0, 4), IOType.OUTPUT),  # Timestamp [bit 10]
            ((20, 0, 4), IOType.OUTPUT),  # Timestamp [bit 11]
            ((19, 0, 4), IOType.OUTPUT),  # Timestamp [bit 12]
            ((18, 0, 4), IOType.OUTPUT),  # Timestamp [bit 13]
            ((17, 0, 4), IOType.OUTPUT),  # Timestamp [bit 14]
            ((16, 0, 4), IOType.OUTPUT),  # Timestamp [bit 15]
            ((15, 0, 4), IOType.OUTPUT),  # Timestamp [bit 16]
            ((14, 0, 4), IOType.OUTPUT),  # Timestamp [bit 17]
            ((13, 0, 4), IOType.OUTPUT),  # Timestamp [bit 18]
            ((30, 0, 4), IOType.OUTPUT),  # Timestamp [bit 1]
            ((12, 0, 4), IOType.OUTPUT),  # Timestamp [bit 19]
            ((11, 0, 4), IOType.OUTPUT),  # Timestamp [bit 20]
            ((10, 0, 4), IOType.OUTPUT),  # Timestamp [bit 21]
            ((9, 0, 4), IOType.OUTPUT),  # Timestamp [bit 22]
            ((8, 0, 4), IOType.OUTPUT),  # Timestamp [bit 23]
            ((7, 0, 4), IOType.OUTPUT),  # Timestamp [bit 24]
            ((6, 0, 4), IOType.OUTPUT),  # Timestamp [bit 25]
            ((5, 0, 4), IOType.OUTPUT),  # Timestamp [bit 26]
            ((4, 0, 4), IOType.OUTPUT),  # Timestamp [bit 27]
            ((3, 0, 4), IOType.OUTPUT),  # Timestamp [bit 28]
            ((29, 0, 4), IOType.OUTPUT),  # Timestamp [bit 2]
            ((2, 0, 4), IOType.OUTPUT),  # Timestamp [bit 29]
            ((1, 0, 4), IOType.OUTPUT),  # Timestamp [bit 30]
            ((0, 0, 4), IOType.OUTPUT),  # Timestamp [bit 31]
            ((28, 0, 4), IOType.OUTPUT),  # Timestamp [bit 3]
            ((27, 0, 4), IOType.OUTPUT),  # Timestamp [bit 4]
            ((26, 0, 4), IOType.OUTPUT),  # Timestamp [bit 5]
            ((25, 0, 4), IOType.OUTPUT),  # Timestamp [bit 6]
            ((24, 0, 4), IOType.OUTPUT),  # Timestamp [bit 7]
            ((23, 0, 4), IOType.OUTPUT),  # Timestamp [bit 8]
        ]
    ),
    BuildingType.SIGN: BuildingProperties(
        blocks=[
            ((-4, 0, -4), IOType.INPUT),
        ]
    ),
    BuildingType.TEXT_CONSOLE: BuildingProperties(
        blocks=[
            ((-1, 0, 9), IOType.INPUT),  # Char [bit 7]
            ((0, 0, 9), IOType.INPUT),  # Char [bit 6]
            ((1, 0, 9), IOType.INPUT),  # Char [bit 5]
            ((2, 0, 9), IOType.INPUT),  # Char [bit 4]
            ((3, 0, 9), IOType.INPUT),  # Char [bit 3]
            ((4, 0, 9), IOType.INPUT),  # Char [bit 2]
            ((5, 0, 9), IOType.INPUT),  # Char [bit 1]
            ((6, 0, 9), IOType.INPUT),  # Char [bit 0]
            ((8, 0, 9), IOType.INPUT),  # Clear
            ((9, 0, 9), IOType.INPUT),  # Cursor
            ((-10, 0, 9), IOType.INPUT),  # Location [bit 7]
            ((-9, 0, 9), IOType.INPUT),  # Location [bit 6]
            ((-8, 0, 9), IOType.INPUT),  # Location [bit 5]
            ((-7, 0, 9), IOType.INPUT),  # Location [bit 4]
            ((-6, 0, 9), IOType.INPUT),  # Location [bit 3]
            ((-5, 0, 9), IOType.INPUT),  # Location [bit 2]
            ((-4, 0, 9), IOType.INPUT),  # Location [bit 1]
            ((-3, 0, 9), IOType.INPUT),  # Location [bit 0]
            ((10, 0, 9), IOType.INPUT),  # Write
        ]
    ),
    BuildingType.DIVIDER_32_BIT: BuildingProperties(
        blocks=[
            ((-1, 0, 7), IOType.INPUT),  # A [bit 31]
            ((8, 0, 7), IOType.INPUT),  # A [bit 22]
            ((9, 0, 7), IOType.INPUT),  # A [bit 21]
            ((10, 0, 7), IOType.INPUT),  # A [bit 20]
            ((11, 0, 7), IOType.INPUT),  # A [bit 19]
            ((12, 0, 7), IOType.INPUT),  # A [bit 18]
            ((13, 0, 7), IOType.INPUT),  # A [bit 17]
            ((14, 0, 7), IOType.INPUT),  # A [bit 16]
            ((15, 0, 7), IOType.INPUT),  # A [bit 15]
            ((16, 0, 7), IOType.INPUT),  # A [bit 14]
            ((17, 0, 7), IOType.INPUT),  # A [bit 13]
            ((0, 0, 7), IOType.INPUT),  # A [bit 30]
            ((1, 0, 7), IOType.INPUT),  # A [bit 29]
            ((18, 0, 7), IOType.INPUT),  # A [bit 12]
            ((19, 0, 7), IOType.INPUT),  # A [bit 11]
            ((20, 0, 7), IOType.INPUT),  # A [bit 10]
            ((21, 0, 7), IOType.INPUT),  # A [bit 9]
            ((22, 0, 7), IOType.INPUT),  # A [bit 8]
            ((23, 0, 7), IOType.INPUT),  # A [bit 7]
            ((24, 0, 7), IOType.INPUT),  # A [bit 6]
            ((25, 0, 7), IOType.INPUT),  # A [bit 5]
            ((26, 0, 7), IOType.INPUT),  # A [bit 4]
            ((27, 0, 7), IOType.INPUT),  # A [bit 3]
            ((2, 0, 7), IOType.INPUT),  # A [bit 28]
            ((28, 0, 7), IOType.INPUT),  # A [bit 2]
            ((29, 0, 7), IOType.INPUT),  # A [bit 1]
            ((30, 0, 7), IOType.INPUT),  # A [bit 0]
            ((3, 0, 7), IOType.INPUT),  # A [bit 27]
            ((4, 0, 7), IOType.INPUT),  # A [bit 26]
            ((5, 0, 7), IOType.INPUT),  # A [bit 25]
            ((6, 0, 7), IOType.INPUT),  # A [bit 24]
            ((7, 0, 7), IOType.INPUT),  # A [bit 23]
            ((33, 0, 7), IOType.INPUT),  # B [bit 31]
            ((42, 0, 7), IOType.INPUT),  # B [bit 22]
            ((43, 0, 7), IOType.INPUT),  # B [bit 21]
            ((44, 0, 7), IOType.INPUT),  # B [bit 20]
            ((45, 0, 7), IOType.INPUT),  # B [bit 19]
            ((46, 0, 7), IOType.INPUT),  # B [bit 18]
            ((47, 0, 7), IOType.INPUT),  # B [bit 17]
            ((48, 0, 7), IOType.INPUT),  # B [bit 16]
            ((49, 0, 7), IOType.INPUT),  # B [bit 15]
            ((50, 0, 7), IOType.INPUT),  # B [bit 14]
            ((51, 0, 7), IOType.INPUT),  # B [bit 13]
            ((34, 0, 7), IOType.INPUT),  # B [bit 30]
            ((52, 0, 7), IOType.INPUT),  # B [bit 12]
            ((53, 0, 7), IOType.INPUT),  # B [bit 11]
            ((54, 0, 7), IOType.INPUT),  # B [bit 10]
            ((55, 0, 7), IOType.INPUT),  # B [bit 9]
            ((56, 0, 7), IOType.INPUT),  # B [bit 8]
            ((57, 0, 7), IOType.INPUT),  # B [bit 7]
            ((58, 0, 7), IOType.INPUT),  # B [bit 6]
            ((59, 0, 7), IOType.INPUT),  # B [bit 5]
            ((60, 0, 7), IOType.INPUT),  # B [bit 4]
            ((61, 0, 7), IOType.INPUT),  # B [bit 3]
            ((35, 0, 7), IOType.INPUT),  # B [bit 29]
            ((62, 0, 7), IOType.INPUT),  # B [bit 2]
            ((63, 0, 7), IOType.INPUT),  # B [bit 1]
            ((64, 0, 7), IOType.INPUT),  # B [bit 0]
            ((36, 0, 7), IOType.INPUT),  # B [bit 28]
            ((37, 0, 7), IOType.INPUT),  # B [bit 27]
            ((38, 0, 7), IOType.INPUT),  # B [bit 26]
            ((39, 0, 7), IOType.INPUT),  # B [bit 25]
            ((40, 0, 7), IOType.INPUT),  # B [bit 24]
            ((41, 0, 7), IOType.INPUT),  # B [bit 23]
            ((-1, 0, -1), IOType.OUTPUT),  # Quotient [bit 31]
            ((8, 0, -1), IOType.OUTPUT),  # Quotient [bit 22]
            ((9, 0, -1), IOType.OUTPUT),  # Quotient [bit 21]
            ((10, 0, -1), IOType.OUTPUT),  # Quotient [bit 20]
            ((11, 0, -1), IOType.OUTPUT),  # Quotient [bit 19]
            ((12, 0, -1), IOType.OUTPUT),  # Quotient [bit 18]
            ((13, 0, -1), IOType.OUTPUT),  # Quotient [bit 17]
            ((14, 0, -1), IOType.OUTPUT),  # Quotient [bit 16]
            ((15, 0, -1), IOType.OUTPUT),  # Quotient [bit 15]
            ((16, 0, -1), IOType.OUTPUT),  # Quotient [bit 14]
            ((17, 0, -1), IOType.OUTPUT),  # Quotient [bit 13]
            ((0, 0, -1), IOType.OUTPUT),  # Quotient [bit 30]
            ((18, 0, -1), IOType.OUTPUT),  # Quotient [bit 12]
            ((19, 0, -1), IOType.OUTPUT),  # Quotient [bit 11]
            ((20, 0, -1), IOType.OUTPUT),  # Quotient [bit 10]
            ((21, 0, -1), IOType.OUTPUT),  # Quotient [bit 9]
            ((22, 0, -1), IOType.OUTPUT),  # Quotient [bit 8]
            ((23, 0, -1), IOType.OUTPUT),  # Quotient [bit 7]
            ((24, 0, -1), IOType.OUTPUT),  # Quotient [bit 6]
            ((25, 0, -1), IOType.OUTPUT),  # Quotient [bit 5]
            ((26, 0, -1), IOType.OUTPUT),  # Quotient [bit 4]
            ((27, 0, -1), IOType.OUTPUT),  # Quotient [bit 3]
            ((1, 0, -1), IOType.OUTPUT),  # Quotient [bit 29]
            ((28, 0, -1), IOType.OUTPUT),  # Quotient [bit 2]
            ((29, 0, -1), IOType.OUTPUT),  # Quotient [bit 1]
            ((30, 0, -1), IOType.OUTPUT),  # Quotient [bit 0]
            ((2, 0, -1), IOType.OUTPUT),  # Quotient [bit 28]
            ((3, 0, -1), IOType.OUTPUT),  # Quotient [bit 27]
            ((4, 0, -1), IOType.OUTPUT),  # Quotient [bit 26]
            ((5, 0, -1), IOType.OUTPUT),  # Quotient [bit 25]
            ((6, 0, -1), IOType.OUTPUT),  # Quotient [bit 24]
            ((7, 0, -1), IOType.OUTPUT),  # Quotient [bit 23]
            ((33, 0, -1), IOType.OUTPUT),  # Remainder [bit 31]
            ((42, 0, -1), IOType.OUTPUT),  # Remainder [bit 22]
            ((43, 0, -1), IOType.OUTPUT),  # Remainder [bit 21]
            ((44, 0, -1), IOType.OUTPUT),  # Remainder [bit 20]
            ((45, 0, -1), IOType.OUTPUT),  # Remainder [bit 19]
            ((46, 0, -1), IOType.OUTPUT),  # Remainder [bit 18]
            ((47, 0, -1), IOType.OUTPUT),  # Remainder [bit 17]
            ((48, 0, -1), IOType.OUTPUT),  # Remainder [bit 16]
            ((49, 0, -1), IOType.OUTPUT),  # Remainder [bit 15]
            ((50, 0, -1), IOType.OUTPUT),  # Remainder [bit 14]
            ((51, 0, -1), IOType.OUTPUT),  # Remainder [bit 13]
            ((34, 0, -1), IOType.OUTPUT),  # Remainder [bit 30]
            ((52, 0, -1), IOType.OUTPUT),  # Remainder [bit 12]
            ((53, 0, -1), IOType.OUTPUT),  # Remainder [bit 11]
            ((54, 0, -1), IOType.OUTPUT),  # Remainder [bit 10]
            ((55, 0, -1), IOType.OUTPUT),  # Remainder [bit 9]
            ((56, 0, -1), IOType.OUTPUT),  # Remainder [bit 8]
            ((57, 0, -1), IOType.OUTPUT),  # Remainder [bit 7]
            ((58, 0, -1), IOType.OUTPUT),  # Remainder [bit 6]
            ((59, 0, -1), IOType.OUTPUT),  # Remainder [bit 5]
            ((60, 0, -1), IOType.OUTPUT),  # Remainder [bit 4]
            ((61, 0, -1), IOType.OUTPUT),  # Remainder [bit 3]
            ((35, 0, -1), IOType.OUTPUT),  # Remainder [bit 29]
            ((62, 0, -1), IOType.OUTPUT),  # Remainder [bit 2]
            ((63, 0, -1), IOType.OUTPUT),  # Remainder [bit 1]
            ((64, 0, -1), IOType.OUTPUT),  # Remainder [bit 0]
            ((36, 0, -1), IOType.OUTPUT),  # Remainder [bit 28]
            ((37, 0, -1), IOType.OUTPUT),  # Remainder [bit 27]
            ((38, 0, -1), IOType.OUTPUT),  # Remainder [bit 26]
            ((39, 0, -1), IOType.OUTPUT),  # Remainder [bit 25]
            ((40, 0, -1), IOType.OUTPUT),  # Remainder [bit 24]
            ((41, 0, -1), IOType.OUTPUT),  # Remainder [bit 23]
        ]
    ),
    BuildingType.DIVIDER_32_BIT: BuildingProperties(
        blocks=[
            ((-1, 0, 7), IOType.INPUT),  # A [bit 31]
            ((8, 0, 7), IOType.INPUT),  # A [bit 22]
            ((9, 0, 7), IOType.INPUT),  # A [bit 21]
            ((10, 0, 7), IOType.INPUT),  # A [bit 20]
            ((11, 0, 7), IOType.INPUT),  # A [bit 19]
            ((12, 0, 7), IOType.INPUT),  # A [bit 18]
            ((13, 0, 7), IOType.INPUT),  # A [bit 17]
            ((14, 0, 7), IOType.INPUT),  # A [bit 16]
            ((15, 0, 7), IOType.INPUT),  # A [bit 15]
            ((16, 0, 7), IOType.INPUT),  # A [bit 14]
            ((17, 0, 7), IOType.INPUT),  # A [bit 13]
            ((0, 0, 7), IOType.INPUT),  # A [bit 30]
            ((1, 0, 7), IOType.INPUT),  # A [bit 29]
            ((18, 0, 7), IOType.INPUT),  # A [bit 12]
            ((19, 0, 7), IOType.INPUT),  # A [bit 11]
            ((20, 0, 7), IOType.INPUT),  # A [bit 10]
            ((21, 0, 7), IOType.INPUT),  # A [bit 9]
            ((22, 0, 7), IOType.INPUT),  # A [bit 8]
            ((23, 0, 7), IOType.INPUT),  # A [bit 7]
            ((24, 0, 7), IOType.INPUT),  # A [bit 6]
            ((25, 0, 7), IOType.INPUT),  # A [bit 5]
            ((26, 0, 7), IOType.INPUT),  # A [bit 4]
            ((27, 0, 7), IOType.INPUT),  # A [bit 3]
            ((2, 0, 7), IOType.INPUT),  # A [bit 28]
            ((28, 0, 7), IOType.INPUT),  # A [bit 2]
            ((29, 0, 7), IOType.INPUT),  # A [bit 1]
            ((30, 0, 7), IOType.INPUT),  # A [bit 0]
            ((3, 0, 7), IOType.INPUT),  # A [bit 27]
            ((4, 0, 7), IOType.INPUT),  # A [bit 26]
            ((5, 0, 7), IOType.INPUT),  # A [bit 25]
            ((6, 0, 7), IOType.INPUT),  # A [bit 24]
            ((7, 0, 7), IOType.INPUT),  # A [bit 23]
            ((33, 0, 7), IOType.INPUT),  # B [bit 31]
            ((42, 0, 7), IOType.INPUT),  # B [bit 22]
            ((43, 0, 7), IOType.INPUT),  # B [bit 21]
            ((44, 0, 7), IOType.INPUT),  # B [bit 20]
            ((45, 0, 7), IOType.INPUT),  # B [bit 19]
            ((46, 0, 7), IOType.INPUT),  # B [bit 18]
            ((47, 0, 7), IOType.INPUT),  # B [bit 17]
            ((48, 0, 7), IOType.INPUT),  # B [bit 16]
            ((49, 0, 7), IOType.INPUT),  # B [bit 15]
            ((50, 0, 7), IOType.INPUT),  # B [bit 14]
            ((51, 0, 7), IOType.INPUT),  # B [bit 13]
            ((34, 0, 7), IOType.INPUT),  # B [bit 30]
            ((52, 0, 7), IOType.INPUT),  # B [bit 12]
            ((53, 0, 7), IOType.INPUT),  # B [bit 11]
            ((54, 0, 7), IOType.INPUT),  # B [bit 10]
            ((55, 0, 7), IOType.INPUT),  # B [bit 9]
            ((56, 0, 7), IOType.INPUT),  # B [bit 8]
            ((57, 0, 7), IOType.INPUT),  # B [bit 7]
            ((58, 0, 7), IOType.INPUT),  # B [bit 6]
            ((59, 0, 7), IOType.INPUT),  # B [bit 5]
            ((60, 0, 7), IOType.INPUT),  # B [bit 4]
            ((61, 0, 7), IOType.INPUT),  # B [bit 3]
            ((35, 0, 7), IOType.INPUT),  # B [bit 29]
            ((62, 0, 7), IOType.INPUT),  # B [bit 2]
            ((63, 0, 7), IOType.INPUT),  # B [bit 1]
            ((64, 0, 7), IOType.INPUT),  # B [bit 0]
            ((36, 0, 7), IOType.INPUT),  # B [bit 28]
            ((37, 0, 7), IOType.INPUT),  # B [bit 27]
            ((38, 0, 7), IOType.INPUT),  # B [bit 26]
            ((39, 0, 7), IOType.INPUT),  # B [bit 25]
            ((40, 0, 7), IOType.INPUT),  # B [bit 24]
            ((41, 0, 7), IOType.INPUT),  # B [bit 23]
            ((-1, 0, -1), IOType.OUTPUT),  # Output [bit 63]
            ((8, 0, -1), IOType.OUTPUT),  # Output [bit 54]
            ((9, 0, -1), IOType.OUTPUT),  # Output [bit 53]
            ((10, 0, -1), IOType.OUTPUT),  # Output [bit 52]
            ((11, 0, -1), IOType.OUTPUT),  # Output [bit 51]
            ((12, 0, -1), IOType.OUTPUT),  # Output [bit 50]
            ((13, 0, -1), IOType.OUTPUT),  # Output [bit 49]
            ((14, 0, -1), IOType.OUTPUT),  # Output [bit 48]
            ((15, 0, -1), IOType.OUTPUT),  # Output [bit 47]
            ((16, 0, -1), IOType.OUTPUT),  # Output [bit 46]
            ((17, 0, -1), IOType.OUTPUT),  # Output [bit 45]
            ((0, 0, -1), IOType.OUTPUT),  # Output [bit 62]
            ((18, 0, -1), IOType.OUTPUT),  # Output [bit 44]
            ((19, 0, -1), IOType.OUTPUT),  # Output [bit 43]
            ((20, 0, -1), IOType.OUTPUT),  # Output [bit 42]
            ((21, 0, -1), IOType.OUTPUT),  # Output [bit 41]
            ((22, 0, -1), IOType.OUTPUT),  # Output [bit 40]
            ((23, 0, -1), IOType.OUTPUT),  # Output [bit 39]
            ((24, 0, -1), IOType.OUTPUT),  # Output [bit 38]
            ((25, 0, -1), IOType.OUTPUT),  # Output [bit 37]
            ((26, 0, -1), IOType.OUTPUT),  # Output [bit 36]
            ((27, 0, -1), IOType.OUTPUT),  # Output [bit 35]
            ((1, 0, -1), IOType.OUTPUT),  # Output [bit 61]
            ((28, 0, -1), IOType.OUTPUT),  # Output [bit 34]
            ((29, 0, -1), IOType.OUTPUT),  # Output [bit 33]
            ((30, 0, -1), IOType.OUTPUT),  # Output [bit 32]
            ((33, 0, -1), IOType.OUTPUT),  # Output [bit 31]
            ((34, 0, -1), IOType.OUTPUT),  # Output [bit 30]
            ((35, 0, -1), IOType.OUTPUT),  # Output [bit 29]
            ((36, 0, -1), IOType.OUTPUT),  # Output [bit 28]
            ((37, 0, -1), IOType.OUTPUT),  # Output [bit 27]
            ((38, 0, -1), IOType.OUTPUT),  # Output [bit 26]
            ((39, 0, -1), IOType.OUTPUT),  # Output [bit 25]
            ((2, 0, -1), IOType.OUTPUT),  # Output [bit 60]
            ((40, 0, -1), IOType.OUTPUT),  # Output [bit 24]
            ((41, 0, -1), IOType.OUTPUT),  # Output [bit 23]
            ((42, 0, -1), IOType.OUTPUT),  # Output [bit 22]
            ((43, 0, -1), IOType.OUTPUT),  # Output [bit 21]
            ((44, 0, -1), IOType.OUTPUT),  # Output [bit 20]
            ((45, 0, -1), IOType.OUTPUT),  # Output [bit 19]
            ((46, 0, -1), IOType.OUTPUT),  # Output [bit 18]
            ((47, 0, -1), IOType.OUTPUT),  # Output [bit 17]
            ((48, 0, -1), IOType.OUTPUT),  # Output [bit 16]
            ((49, 0, -1), IOType.OUTPUT),  # Output [bit 15]
            ((3, 0, -1), IOType.OUTPUT),  # Output [bit 59]
            ((50, 0, -1), IOType.OUTPUT),  # Output [bit 14]
            ((51, 0, -1), IOType.OUTPUT),  # Output [bit 13]
            ((52, 0, -1), IOType.OUTPUT),  # Output [bit 12]
            ((53, 0, -1), IOType.OUTPUT),  # Output [bit 11]
            ((54, 0, -1), IOType.OUTPUT),  # Output [bit 10]
            ((55, 0, -1), IOType.OUTPUT),  # Output [bit 9]
            ((56, 0, -1), IOType.OUTPUT),  # Output [bit 8]
            ((57, 0, -1), IOType.OUTPUT),  # Output [bit 7]
            ((58, 0, -1), IOType.OUTPUT),  # Output [bit 6]
            ((59, 0, -1), IOType.OUTPUT),  # Output [bit 5]
            ((4, 0, -1), IOType.OUTPUT),  # Output [bit 58]
            ((60, 0, -1), IOType.OUTPUT),  # Output [bit 4]
            ((61, 0, -1), IOType.OUTPUT),  # Output [bit 3]
            ((62, 0, -1), IOType.OUTPUT),  # Output [bit 2]
            ((63, 0, -1), IOType.OUTPUT),  # Output [bit 1]
            ((64, 0, -1), IOType.OUTPUT),  # Output [bit 0]
            ((5, 0, -1), IOType.OUTPUT),  # Output [bit 57]
            ((6, 0, -1), IOType.OUTPUT),  # Output [bit 56]
            ((7, 0, -1), IOType.OUTPUT),  # Output [bit 55]
        ]
    ),
}

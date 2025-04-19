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
    attrPath: str


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
            BP((7, 0, -3), OUTPUT, "ctrl"),  # Ctrl
            BP((-6, 0, -3), OUTPUT, "ascii[7]"),  # ASCII [bit 7]
            BP((-5, 0, -3), OUTPUT, "ascii[6]"),  # ASCII [bit 6]
            BP((-4, 0, -3), OUTPUT, "ascii[5]"),  # ASCII [bit 5]
            BP((-3, 0, -3), OUTPUT, "ascii[4]"),  # ASCII [bit 4]
            BP((-2, 0, -3), OUTPUT, "ascii[3]"),  # ASCII [bit 3]
            BP((-1, 0, -3), OUTPUT, "ascii[2]"),  # ASCII [bit 2]
            BP((0, 0, -3), OUTPUT, "ascii[1]"),  # ASCII [bit 1]
            BP((1, 0, -3), OUTPUT, "ascii[0]"),  # ASCII [bit 0]
            BP((3, 0, -3), OUTPUT, "pressed"),  # Pressed
            BP((5, 0, -3), OUTPUT, "shift"),  # Shift
        ],
    ),
    BuildingType.ASSEMBLER: BuildingProperties(
        blocks=[
            BP((-17, 0, 4), INPUT, "address[11]"),  # address [bit 11]
            BP((-8, 0, 4), INPUT, "address[2]"),  # address [bit 2]
            BP((-7, 0, 4), INPUT, "address[1]"),  # address [bit 1]
            BP((-6, 0, 4), INPUT, "address[0]"),  # address [bit 0]
            BP((-16, 0, 4), INPUT, "address[10]"),  # address [bit 10]
            BP((-15, 0, 4), INPUT, "address[9]"),  # address [bit 9]
            BP((-14, 0, 4), INPUT, "address[8]"),  # address [bit 8]
            BP((-13, 0, 4), INPUT, "address[7]"),  # address [bit 7]
            BP((-12, 0, 4), INPUT, "address[6]"),  # address [bit 6]
            BP((-11, 0, 4), INPUT, "address[5]"),  # address [bit 5]
            BP((-10, 0, 4), INPUT, "address[4]"),  # address [bit 4]
            BP((-9, 0, 4), INPUT, "address[3]"),  # address [bit 3]
            BP((-17, 0, -4), OUTPUT, "byte1[7]"),  # Byte 1 [bit 7]
            BP((-16, 0, -4), OUTPUT, "byte1[6]"),  # Byte 1 [bit 6]
            BP((-15, 0, -4), OUTPUT, "byte1[5]"),  # Byte 1 [bit 5]
            BP((-14, 0, -4), OUTPUT, "byte1[4]"),  # Byte 1 [bit 4]
            BP((-13, 0, -4), OUTPUT, "byte1[3]"),  # Byte 1 [bit 3]
            BP((-12, 0, -4), OUTPUT, "byte1[2]"),  # Byte 1 [bit 2]
            BP((-11, 0, -4), OUTPUT, "byte1[1]"),  # Byte 1 [bit 1]
            BP((-10, 0, -4), OUTPUT, "byte1[0]"),  # Byte 1 [bit 0]
            BP((-8, 0, -4), OUTPUT, "byte2[7]"),  # Byte 2 [bit 7]
            BP((-7, 0, -4), OUTPUT, "byte2[6]"),  # Byte 2 [bit 6]
            BP((-6, 0, -4), OUTPUT, "byte2[5]"),  # Byte 2 [bit 5]
            BP((-5, 0, -4), OUTPUT, "byte2[4]"),  # Byte 2 [bit 4]
            BP((-4, 0, -4), OUTPUT, "byte2[3]"),  # Byte 2 [bit 3]
            BP((-3, 0, -4), OUTPUT, "byte2[2]"),  # Byte 2 [bit 2]
            BP((-2, 0, -4), OUTPUT, "byte2[1]"),  # Byte 2 [bit 1]
            BP((-1, 0, -4), OUTPUT, "byte2[0]"),  # Byte 2 [bit 0]
            BP((1, 0, -4), OUTPUT, "byte3[7]"),  # Byte 3 [bit 7]
            BP((2, 0, -4), OUTPUT, "byte3[6]"),  # Byte 3 [bit 6]
            BP((3, 0, -4), OUTPUT, "byte3[5]"),  # Byte 3 [bit 5]
            BP((4, 0, -4), OUTPUT, "byte3[4]"),  # Byte 3 [bit 4]
            BP((5, 0, -4), OUTPUT, "byte3[3]"),  # Byte 3 [bit 3]
            BP((6, 0, -4), OUTPUT, "byte3[2]"),  # Byte 3 [bit 2]
            BP((7, 0, -4), OUTPUT, "byte3[1]"),  # Byte 3 [bit 1]
            BP((8, 0, -4), OUTPUT, "byte3[0]"),  # Byte 3 [bit 0]
            BP((10, 0, -4), OUTPUT, "byte4[7]"),  # Byte 4 [bit 7]
            BP((11, 0, -4), OUTPUT, "byte4[6]"),  # Byte 4 [bit 6]
            BP((12, 0, -4), OUTPUT, "byte4[5]"),  # Byte 4 [bit 5]
            BP((13, 0, -4), OUTPUT, "byte4[4]"),  # Byte 4 [bit 4]
            BP((14, 0, -4), OUTPUT, "byte4[3]"),  # Byte 4 [bit 3]
            BP((15, 0, -4), OUTPUT, "byte4[2]"),  # Byte 4 [bit 2]
            BP((16, 0, -4), OUTPUT, "byte4[1]"),  # Byte 4 [bit 1]
            BP((17, 0, -4), OUTPUT, "byte4[0]"),  # Byte 4 [bit 0]
        ]
    ),
    BuildingType.DIVIDER: BuildingProperties(
        blocks=[
            BP((-1, 0, 7), INPUT, "a[15]"),  # A [bit 15]
            BP((7, 0, 7), INPUT, "a[6]"),  # A [bit 6]
            BP((8, 0, 7), INPUT, "a[5]"),  # A [bit 5]
            BP((9, 0, 7), INPUT, "a[4]"),  # A [bit 4]
            BP((10, 0, 7), INPUT, "a[3]"),  # A [bit 3]
            BP((11, 0, 7), INPUT, "a[2]"),  # A [bit 2]
            BP((12, 0, 7), INPUT, "a[1]"),  # A [bit 1]
            BP((13, 0, 7), INPUT, "a[0]"),  # A [bit 0]
            BP((0, 0, 7), INPUT, "a[14]"),  # A [bit 14]
            BP((1, 0, 7), INPUT, "a[13]"),  # A [bit 13]
            BP((2, 0, 7), INPUT, "a[12]"),  # A [bit 12]
            BP((3, 0, 7), INPUT, "a[11]"),  # A [bit 11]
            BP((3, 0, 7), INPUT, "a[10]"),  # A [bit 10]
            BP((4, 0, 7), INPUT, "a[9]"),  # A [bit 9]
            BP((5, 0, 7), INPUT, "a[8]"),  # A [bit 8]
            BP((6, 0, 7), INPUT, "a[7]"),  # A [bit 7]
            BP((16, 0, 7), INPUT, "b[15]"),  # B [bit 15]
            BP((25, 0, 7), INPUT, "b[6]"),  # B [bit 6]
            BP((26, 0, 7), INPUT, "b[5]"),  # B [bit 5]
            BP((27, 0, 7), INPUT, "b[4]"),  # B [bit 4]
            BP((28, 0, 7), INPUT, "b[3]"),  # B [bit 3]
            BP((29, 0, 7), INPUT, "b[2]"),  # B [bit 2]
            BP((30, 0, 7), INPUT, "b[1]"),  # B [bit 1]
            BP((31, 0, 7), INPUT, "b[0]"),  # B [bit 0]
            BP((17, 0, 7), INPUT, "b[14]"),  # B [bit 14]
            BP((18, 0, 7), INPUT, "b[13]"),  # B [bit 13]
            BP((19, 0, 7), INPUT, "b[12]"),  # B [bit 12]
            BP((20, 0, 7), INPUT, "b[11]"),  # B [bit 11]
            BP((21, 0, 7), INPUT, "b[10]"),  # B [bit 10]
            BP((22, 0, 7), INPUT, "b[9]"),  # B [bit 9]
            BP((23, 0, 7), INPUT, "b[8]"),  # B [bit 8]
            BP((24, 0, 7), INPUT, "b[7]"),  # B [bit 7]
            BP((-1, 0, -1), OUTPUT, "quotient[15]"),  # Quotient [bit 15]
            BP((7, 0, -1), OUTPUT, "quotient[6]"),  # Quotient [bit 6]
            BP((8, 0, -1), OUTPUT, "quotient[5]"),  # Quotient [bit 5]
            BP((9, 0, -1), OUTPUT, "quotient[4]"),  # Quotient [bit 4]
            BP((10, 0, -1), OUTPUT, "quotient[3]"),  # Quotient [bit 3]
            BP((11, 0, -1), OUTPUT, "quotient[2]"),  # Quotient [bit 2]
            BP((12, 0, -1), OUTPUT, "quotient[1]"),  # Quotient [bit 1]
            BP((13, 0, -1), OUTPUT, "quotient[0]"),  # Quotient [bit 0]
            BP((0, 0, -1), OUTPUT, "quotient[14]"),  # Quotient [bit 14]
            BP((1, 0, -1), OUTPUT, "quotient[13]"),  # Quotient [bit 13]
            BP((2, 0, -1), OUTPUT, "quotient[12]"),  # Quotient [bit 12]
            BP((3, 0, -1), OUTPUT, "quotient[11]"),  # Quotient [bit 11]
            BP((3, 0, -1), OUTPUT, "quotient[10]"),  # Quotient [bit 10]
            BP((4, 0, -1), OUTPUT, "quotient[9]"),  # Quotient [bit 9]
            BP((5, 0, -1), OUTPUT, "quotient[8]"),  # Quotient [bit 8]
            BP((6, 0, -1), OUTPUT, "quotient[7]"),  # Quotient [bit 7]
            BP((16, 0, -1), OUTPUT, "remainder[15]"),  # Remainder [bit 15]
            BP((25, 0, -1), OUTPUT, "remainder[6]"),  # Remainder [bit 6]
            BP((26, 0, -1), OUTPUT, "remainder[5]"),  # Remainder [bit 5]
            BP((27, 0, -1), OUTPUT, "remainder[4]"),  # Remainder [bit 4]
            BP((28, 0, -1), OUTPUT, "remainder[3]"),  # Remainder [bit 3]
            BP((29, 0, -1), OUTPUT, "remainder[2]"),  # Remainder [bit 2]
            BP((30, 0, -1), OUTPUT, "remainder[1]"),  # Remainder [bit 1]
            BP((31, 0, -1), OUTPUT, "remainder[0]"),  # Remainder [bit 0]
            BP((17, 0, -1), OUTPUT, "remainder[14]"),  # Remainder [bit 14]
            BP((18, 0, -1), OUTPUT, "remainder[13]"),  # Remainder [bit 13]
            BP((19, 0, -1), OUTPUT, "remainder[12]"),  # Remainder [bit 12]
            BP((20, 0, -1), OUTPUT, "remainder[11]"),  # Remainder [bit 11]
            BP((21, 0, -1), OUTPUT, "remainder[10]"),  # Remainder [bit 10]
            BP((22, 0, -1), OUTPUT, "remainder[9]"),  # Remainder [bit 9]
            BP((23, 0, -1), OUTPUT, "remainder[8]"),  # Remainder [bit 8]
            BP((24, 0, -1), OUTPUT, "remainder[7]"),  # Remainder [bit 7]
        ]
    ),
    BuildingType.DOOR: BuildingProperties(
        blocks=[
            BP((0, 7, 0), INPUT, "input"),
        ]
    ),
    BuildingType.DUAL_MEMORY: BuildingProperties(
        blocks=[
            BP((-4, 0, 2), INPUT, "saveAddress[7]"),  # Save Address [bit 7]
            BP((-3, 0, 2), INPUT, "saveAddress[6]"),  # Save Address [bit 6]
            BP((-2, 0, 2), INPUT, "saveAddress[5]"),  # Save Address [bit 5]
            BP((-1, 0, 2), INPUT, "saveAddress[4]"),  # Save Address [bit 4]
            BP((0, 0, 2), INPUT, "saveAddress[3]"),  # Save Address [bit 3]
            BP((1, 0, 2), INPUT, "saveAddress[2]"),  # Save Address [bit 2]
            BP((2, 0, 2), INPUT, "saveAddress[1]"),  # Save Address [bit 1]
            BP((3, 0, 2), INPUT, "saveAddress[0]"),  # Save Address [bit 0]
            BP((-13, 0, 2), INPUT, "loadAddress[7]"),  # Load Address [bit 7]
            BP((-12, 0, 2), INPUT, "loadAddress[6]"),  # Load Address [bit 6]
            BP((-11, 0, 2), INPUT, "loadAddress[5]"),  # Load Address [bit 5]
            BP((-10, 0, 2), INPUT, "loadAddress[4]"),  # Load Address [bit 4]
            BP((-9, 0, 2), INPUT, "loadAddress[3]"),  # Load Address [bit 3]
            BP((-8, 0, 2), INPUT, "loadAddress[2]"),  # Load Address [bit 2]
            BP((-7, 0, 2), INPUT, "loadAddress[1]"),  # Load Address [bit 1]
            BP((-6, 0, 2), INPUT, "loadAddress[0]"),  # Load Address [bit 0]
            BP((-13, 0, -2), OUTPUT, "output[7]"),  # Output [bit 7]
            BP((-12, 0, -2), OUTPUT, "output[6]"),  # Output [bit 6]
            BP((-11, 0, -2), OUTPUT, "output[5]"),  # Output [bit 5]
            BP((-10, 0, -2), OUTPUT, "output[4]"),  # Output [bit 4]
            BP((-9, 0, -2), OUTPUT, "output[3]"),  # Output [bit 3]
            BP((-8, 0, -2), OUTPUT, "output[2]"),  # Output [bit 2]
            BP((-7, 0, -2), OUTPUT, "output[1]"),  # Output [bit 1]
            BP((-6, 0, -2), OUTPUT, "output[0]"),  # Output [bit 0]
            BP((5, 0, 2), INPUT, "value[7]"),  # Value [bit 7]
            BP((6, 0, 2), INPUT, "value[6]"),  # Value [bit 6]
            BP((7, 0, 2), INPUT, "value[5]"),  # Value [bit 5]
            BP((8, 0, 2), INPUT, "value[4]"),  # Value [bit 4]
            BP((9, 0, 2), INPUT, "value[3]"),  # Value [bit 3]
            BP((10, 0, 2), INPUT, "value[2]"),  # Value [bit 2]
            BP((11, 0, 2), INPUT, "value[1]"),  # Value [bit 1]
            BP((12, 0, 2), INPUT, "value[0]"),  # Value [bit 0]
            BP((14, 0, 2), INPUT, "write"),  # write
        ]
    ),
    BuildingType.FUNCTION_GENERATOR: BuildingProperties(
        blocks=[
            BP((8, 0, 3), INPUT, "func[1]"),  # Func [bit 1]
            BP((9, 0, 3), INPUT, "func[0]"),  # Func [bit 0]
            BP((-1, 0, -2), OUTPUT, "output[7]"),  # Output [bit 7]
            BP((0, 0, -2), OUTPUT, "output[6]"),  # Output [bit 6]
            BP((1, 0, -2), OUTPUT, "output[5]"),  # Output [bit 5]
            BP((2, 0, -2), OUTPUT, "output[4]"),  # Output [bit 4]
            BP((3, 0, -2), OUTPUT, "output[3]"),  # Output [bit 3]
            BP((4, 0, -2), OUTPUT, "output[2]"),  # Output [bit 2]
            BP((5, 0, -2), OUTPUT, "output[1]"),  # Output [bit 1]
            BP((6, 0, -2), OUTPUT, "output[0]"),  # Output [bit 0]
            BP((-1, 0, 3), INPUT, "x[7]"),  # X [bit 7]
            BP((0, 0, 3), INPUT, "x[6]"),  # X [bit 6]
            BP((1, 0, 3), INPUT, "x[5]"),  # X [bit 5]
            BP((2, 0, 3), INPUT, "x[4]"),  # X [bit 4]
            BP((3, 0, 3), INPUT, "x[3]"),  # X [bit 3]
            BP((4, 0, 3), INPUT, "x[2]"),  # X [bit 2]
            BP((5, 0, 3), INPUT, "x[1]"),  # X [bit 1]
            BP((6, 0, 3), INPUT, "x[0]"),  # X [bit 0]
        ]
    ),
    BuildingType.GRAPH: BuildingProperties(
        blocks=[
            BP((-4, 0, 4), INPUT, "input[7]"),  # Input [bit 7]
            BP((-3, 0, 4), INPUT, "input[6]"),  # Input [bit 6]
            BP((-2, 0, 4), INPUT, "input[5]"),  # Input [bit 5]
            BP((-1, 0, 4), INPUT, "input[4]"),  # Input [bit 4]
            BP((0, 0, 4), INPUT, "input[3]"),  # Input [bit 3]
            BP((1, 0, 4), INPUT, "input[2]"),  # Input [bit 2]
            BP((2, 0, 4), INPUT, "input[1]"),  # Input [bit 1]
            BP((3, 0, 4), INPUT, "input[0]"),  # Input [bit 0]
        ]
    ),
    BuildingType.HUGE_MEMORY: BuildingProperties(
        blocks=[
            BP((-17, 0, 3), INPUT, "address[15]"),  # address [bit 15]
            BP((-8, 0, 3), INPUT, "address[6]"),  # address [bit 6]
            BP((-7, 0, 3), INPUT, "address[5]"),  # address [bit 5]
            BP((-6, 0, 3), INPUT, "address[4]"),  # address [bit 4]
            BP((-5, 0, 3), INPUT, "address[3]"),  # address [bit 3]
            BP((-4, 0, 3), INPUT, "address[2]"),  # address [bit 2]
            BP((-3, 0, 3), INPUT, "address[1]"),  # address [bit 1]
            BP((-2, 0, 3), INPUT, "address[0]"),  # address [bit 0]
            BP((-16, 0, 3), INPUT, "address[14]"),  # address [bit 14]
            BP((-15, 0, 3), INPUT, "address[13]"),  # address [bit 13]
            BP((-14, 0, 3), INPUT, "address[12]"),  # address [bit 12]
            BP((-13, 0, 3), INPUT, "address[11]"),  # address [bit 11]
            BP((-12, 0, 3), INPUT, "address[10]"),  # address [bit 10]
            BP((-11, 0, 3), INPUT, "address[9]"),  # address [bit 9]
            BP((-10, 0, 3), INPUT, "address[8]"),  # address [bit 8]
            BP((-9, 0, 3), INPUT, "address[7]"),  # address [bit 7]
            BP((-17, 0, -3), OUTPUT, "output[15]"),  # output [bit 15]
            BP((-8, 0, -3), OUTPUT, "output[6]"),  # output [bit 6]
            BP((-7, 0, -3), OUTPUT, "output[5]"),  # output [bit 5]
            BP((-6, 0, -3), OUTPUT, "output[4]"),  # output [bit 4]
            BP((-5, 0, -3), OUTPUT, "output[3]"),  # output [bit 3]
            BP((-4, 0, -3), OUTPUT, "output[2]"),  # output [bit 2]
            BP((-3, 0, -3), OUTPUT, "output[1]"),  # output [bit 1]
            BP((-2, 0, -3), OUTPUT, "output[0]"),  # output [bit 0]
            BP((-16, 0, -3), OUTPUT, "output[14]"),  # output [bit 14]
            BP((-15, 0, -3), OUTPUT, "output[13]"),  # output [bit 13]
            BP((-14, 0, -3), OUTPUT, "output[12]"),  # output [bit 12]
            BP((-13, 0, -3), OUTPUT, "output[11]"),  # output [bit 11]
            BP((-12, 0, -3), OUTPUT, "output[10]"),  # output [bit 10]
            BP((-11, 0, -3), OUTPUT, "output[9]"),  # output [bit 9]
            BP((-10, 0, -3), OUTPUT, "output[8]"),  # output [bit 8]
            BP((-9, 0, -3), OUTPUT, "output[7]"),  # output [bit 7]
            BP((1, 0, 3), INPUT, "value[15]"),  # value [bit 15]
            BP((10, 0, 3), INPUT, "value[6]"),  # value [bit 6]
            BP((11, 0, 3), INPUT, "value[5]"),  # value [bit 5]
            BP((12, 0, 3), INPUT, "value[4]"),  # value [bit 4]
            BP((13, 0, 3), INPUT, "value[3]"),  # value [bit 3]
            BP((14, 0, 3), INPUT, "value[2]"),  # value [bit 2]
            BP((15, 0, 3), INPUT, "value[1]"),  # value [bit 1]
            BP((16, 0, 3), INPUT, "value[0]"),  # value [bit 0]
            BP((2, 0, 3), INPUT, "value[14]"),  # value [bit 14]
            BP((3, 0, 3), INPUT, "value[13]"),  # value [bit 13]
            BP((4, 0, 3), INPUT, "value[12]"),  # value [bit 12]
            BP((5, 0, 3), INPUT, "value[11]"),  # value [bit 11]
            BP((6, 0, 3), INPUT, "value[10]"),  # value [bit 10]
            BP((7, 0, 3), INPUT, "value[9]"),  # value [bit 9]
            BP((8, 0, 3), INPUT, "value[8]"),  # value [bit 8]
            BP((9, 0, 3), INPUT, "value[7]"),  # value [bit 7]
            BP((18, 0, 3), INPUT, "write"),  # write
        ]
    ),
    BuildingType.INTEGRATED_CIRCUIT: BuildingProperties(
        blocks=[
            BP((0, 0, 7), INPUT, "input[31]"),  # input [bit 31]
            BP((9, 0, 7), INPUT, "input[22]"),  # input [bit 22]
            BP((10, 0, 7), INPUT, "input[21]"),  # input [bit 21]
            BP((11, 0, 7), INPUT, "input[20]"),  # input [bit 20]
            BP((12, 0, 7), INPUT, "input[19]"),  # input [bit 19]
            BP((13, 0, 7), INPUT, "input[18]"),  # input [bit 18]
            BP((14, 0, 7), INPUT, "input[17]"),  # input [bit 17]
            BP((15, 0, 7), INPUT, "input[16]"),  # input [bit 16]
            BP((16, 0, 7), INPUT, "input[15]"),  # input [bit 15]
            BP((17, 0, 7), INPUT, "input[14]"),  # input [bit 14]
            BP((18, 0, 7), INPUT, "input[13]"),  # input [bit 13]
            BP((1, 0, 7), INPUT, "input[30]"),  # input [bit 30]
            BP((19, 0, 7), INPUT, "input[12]"),  # input [bit 12]
            BP((20, 0, 7), INPUT, "input[11]"),  # input [bit 11]
            BP((21, 0, 7), INPUT, "input[10]"),  # input [bit 10]
            BP((22, 0, 7), INPUT, "input[9]"),  # input [bit 9]
            BP((23, 0, 7), INPUT, "input[8]"),  # input [bit 8]
            BP((24, 0, 7), INPUT, "input[7]"),  # input [bit 7]
            BP((25, 0, 7), INPUT, "input[6]"),  # input [bit 6]
            BP((26, 0, 7), INPUT, "input[5]"),  # input [bit 5]
            BP((27, 0, 7), INPUT, "input[4]"),  # input [bit 4]
            BP((28, 0, 7), INPUT, "input[3]"),  # input [bit 3]
            BP((2, 0, 7), INPUT, "input[29]"),  # input [bit 29]
            BP((29, 0, 7), INPUT, "input[2]"),  # input [bit 2]
            BP((30, 0, 7), INPUT, "input[1]"),  # input [bit 1]
            BP((31, 0, 7), INPUT, "input[1]"),  # input [bit 0]
            BP((3, 0, 7), INPUT, "input[28]"),  # input [bit 28]
            BP((4, 0, 7), INPUT, "input[27]"),  # input [bit 27]
            BP((5, 0, 7), INPUT, "input[26]"),  # input [bit 26]
            BP((6, 0, 7), INPUT, "input[25]"),  # input [bit 25]
            BP((7, 0, 7), INPUT, "input[24]"),  # input [bit 24]
            BP((8, 0, 7), INPUT, "input[23]"),  # input [bit 23]
            BP((0, 0, -1), OUTPUT, "output[31]"),  # output [bit 31]
            BP((9, 0, -1), OUTPUT, "output[22]"),  # output [bit 22]
            BP((10, 0, -1), OUTPUT, "output[21]"),  # output [bit 21]
            BP((11, 0, -1), OUTPUT, "output[20]"),  # output [bit 20]
            BP((12, 0, -1), OUTPUT, "output[19]"),  # output [bit 19]
            BP((13, 0, -1), OUTPUT, "output[18]"),  # output [bit 18]
            BP((14, 0, -1), OUTPUT, "output[17]"),  # output [bit 17]
            BP((15, 0, -1), OUTPUT, "output[16]"),  # output [bit 16]
            BP((16, 0, -1), OUTPUT, "output[15]"),  # output [bit 15]
            BP((17, 0, -1), OUTPUT, "output[14]"),  # output [bit 14]
            BP((18, 0, -1), OUTPUT, "output[13]"),  # output [bit 13]
            BP((1, 0, -1), OUTPUT, "output[30]"),  # output [bit 30]
            BP((19, 0, -1), OUTPUT, "output[12]"),  # output [bit 12]
            BP((20, 0, -1), OUTPUT, "output[11]"),  # output [bit 11]
            BP((21, 0, -1), OUTPUT, "output[10]"),  # output [bit 10]
            BP((22, 0, -1), OUTPUT, "output[9]"),  # output [bit 9]
            BP((23, 0, -1), OUTPUT, "output[8]"),  # output [bit 8]
            BP((24, 0, -1), OUTPUT, "output[7]"),  # output [bit 7]
            BP((25, 0, -1), OUTPUT, "output[6]"),  # output [bit 6]
            BP((26, 0, -1), OUTPUT, "output[5]"),  # output [bit 5]
            BP((27, 0, -1), OUTPUT, "output[4]"),  # output [bit 4]
            BP((28, 0, -1), OUTPUT, "output[3]"),  # output [bit 3]
            BP((2, 0, -1), OUTPUT, "output[29]"),  # output [bit 29]
            BP((29, 0, -1), OUTPUT, "output[2]"),  # output [bit 2]
            BP((30, 0, -1), OUTPUT, "output[1]"),  # output [bit 1]
            BP((31, 0, -1), OUTPUT, "output[0]"),  # output [bit 0]
            BP((3, 0, -1), OUTPUT, "output[28]"),  # output [bit 28]
            BP((4, 0, -1), OUTPUT, "output[27]"),  # output [bit 27]
            BP((5, 0, -1), OUTPUT, "output[26]"),  # output [bit 26]
            BP((6, 0, -1), OUTPUT, "output[25]"),  # output [bit 25]
            BP((7, 0, -1), OUTPUT, "output[24]"),  # output [bit 24]
            BP((8, 0, -1), OUTPUT, "output[23]"),  # output [bit 23]
        ]
    ),
    BuildingType.KEY_INPUT: BuildingProperties(
        blocks=[
            BP((-18, 0, -4), OUTPUT, "a"),  # A
            BP((-9, 0, -4), OUTPUT, "j"),  # J
            BP((-8, 0, -4), OUTPUT, "k"),  # K
            BP((-7, 0, -4), OUTPUT, "l"),  # L
            BP((-6, 0, -4), OUTPUT, "m"),  # M
            BP((-5, 0, -4), OUTPUT, "n"),  # N
            BP((-4, 0, -4), OUTPUT, "o"),  # O
            BP((-3, 0, -4), OUTPUT, "p"),  # P
            BP((-2, 0, -4), OUTPUT, "q"),  # Q
            BP((-1, 0, -4), OUTPUT, "r"),  # R
            BP((0, 0, -4), OUTPUT, "s"),  # S
            BP((-17, 0, -4), OUTPUT, "b"),  # B
            BP((1, 0, -4), OUTPUT, "t"),  # T
            BP((2, 0, -4), OUTPUT, "u"),  # U
            BP((3, 0, -4), OUTPUT, "v"),  # V
            BP((4, 0, -4), OUTPUT, "w"),  # W
            BP((5, 0, -4), OUTPUT, "x"),  # X
            BP((6, 0, -4), OUTPUT, "y"),  # Y
            BP((7, 0, -4), OUTPUT, "z"),  # Z
            BP((8, 0, -4), OUTPUT, "one"),  # 1
            BP((9, 0, -4), OUTPUT, "two"),  # 2
            BP((-16, 0, -4), OUTPUT, "c"),  # C
            BP((10, 0, -4), OUTPUT, "three"),  # 3
            BP((11, 0, -4), OUTPUT, "four"),  # 4
            BP((12, 0, -4), OUTPUT, "five"),  # 5
            BP((13, 0, -4), OUTPUT, "six"),  # 6
            BP((14, 0, -4), OUTPUT, "seven"),  # 7
            BP((15, 0, -4), OUTPUT, "eight"),  # 8
            BP((16, 0, -4), OUTPUT, "nine"),  # 9
            BP((17, 0, -4), OUTPUT, "zero"),  # 0
            BP((18, 0, -4), OUTPUT, "space"),  # space
            BP((-15, 0, -4), OUTPUT, "d"),  # D
            BP((-14, 0, -4), OUTPUT, "e"),  # E
            BP((-13, 0, -4), OUTPUT, "f"),  # F
            BP((-12, 0, -4), OUTPUT, "g"),  # G
            BP((-11, 0, -4), OUTPUT, "h"),  # H
            BP((-10, 0, -4), OUTPUT, "i"),  # I
        ]
    ),
    BuildingType.LARGE_RGB_DISPLAY: BuildingProperties(
        blocks=[
            BP((10, 0, 18), INPUT, "b[5]"),  # B [bit 5]
            BP((11, 0, 18), INPUT, "b[4]"),  # B [bit 4]
            BP((12, 0, 18), INPUT, "b[3]"),  # B [bit 3]
            BP((13, 0, 18), INPUT, "b[2]"),  # B [bit 2]
            BP((14, 0, 18), INPUT, "b[1]"),  # B [bit 1]
            BP((15, 0, 18), INPUT, "b[0]"),  # B [bit 0]
            BP((3, 0, 18), INPUT, "g[5]"),  # G [bit 5]
            BP((4, 0, 18), INPUT, "g[4]"),  # G [bit 4]
            BP((5, 0, 18), INPUT, "g[3]"),  # G [bit 3]
            BP((6, 0, 18), INPUT, "g[2]"),  # G [bit 2]
            BP((7, 0, 18), INPUT, "g[1]"),  # G [bit 1]
            BP((8, 0, 18), INPUT, "g[0]"),  # G [bit 0]
            BP((-4, 0, 18), INPUT, "r[5]"),  # R [bit 5]
            BP((-3, 0, 18), INPUT, "r[4]"),  # R [bit 4]
            BP((-2, 0, 18), INPUT, "r[3]"),  # R [bit 3]
            BP((-1, 0, 18), INPUT, "r[2]"),  # R [bit 2]
            BP((0, 0, 18), INPUT, "r[1]"),  # R [bit 1]
            BP((1, 0, 18), INPUT, "r[0]"),  # R [bit 0]
            BP((17, 0, 18), INPUT, "reset"),  # Reset
            BP((19, 0, 18), INPUT, "write"),  # Write
            BP((-20, 0, 18), INPUT, "x[6]"),  # X [bit 6]
            BP((-19, 0, 18), INPUT, "x[5]"),  # X [bit 5]
            BP((-18, 0, 18), INPUT, "x[4]"),  # X [bit 4]
            BP((-17, 0, 18), INPUT, "x[3]"),  # X [bit 3]
            BP((-16, 0, 18), INPUT, "x[2]"),  # X [bit 2]
            BP((-15, 0, 18), INPUT, "x[1]"),  # X [bit 1]
            BP((-14, 0, 18), INPUT, "x[0]"),  # X [bit 0]
            BP((-12, 0, 18), INPUT, "y[6]"),  # Y [bit 6]
            BP((-11, 0, 18), INPUT, "y[5]"),  # Y [bit 5]
            BP((-10, 0, 18), INPUT, "y[4]"),  # Y [bit 4]
            BP((-9, 0, 18), INPUT, "y[3]"),  # Y [bit 3]
            BP((-8, 0, 18), INPUT, "y[2]"),  # Y [bit 2]
            BP((-7, 0, 18), INPUT, "y[1]"),  # Y [bit 1]
            BP((-6, 0, 18), INPUT, "y[0]"),  # Y [bit 0]
        ]
    ),
    BuildingType.MASS_MEMORY: BuildingProperties(
        blocks=[
            BP((-11, 0, 2), INPUT, "address[11]"),  # address [bit 11]
            BP((-2, 0, 2), INPUT, "address[2]"),  # address [bit 2]
            BP((-1, 0, 2), INPUT, "address[1]"),  # address [bit 1]
            BP((0, 0, 2), INPUT, "address[0]"),  # address [bit 0]
            BP((-10, 0, 2), INPUT, "address[10]"),  # address [bit 10]
            BP((-9, 0, 2), INPUT, "address[9]"),  # address [bit 9]
            BP((-8, 0, 2), INPUT, "address[8]"),  # address [bit 8]
            BP((-7, 0, 2), INPUT, "address[7]"),  # address [bit 7]
            BP((-6, 0, 2), INPUT, "address[6]"),  # address [bit 6]
            BP((-5, 0, 2), INPUT, "address[5]"),  # address [bit 5]
            BP((-4, 0, 2), INPUT, "address[4]"),  # address [bit 4]
            BP((-3, 0, 2), INPUT, "address[3]"),  # address [bit 3]
            BP((-11, 0, -2), OUTPUT, "output[7]"),  # output [bit 7]
            BP((-10, 0, -2), OUTPUT, "output[6]"),  # output [bit 6]
            BP((-9, 0, -2), OUTPUT, "output[5]"),  # output [bit 5]
            BP((-8, 0, -2), OUTPUT, "output[4]"),  # output [bit 4]
            BP((-7, 0, -2), OUTPUT, "output[3]"),  # output [bit 3]
            BP((-6, 0, -2), OUTPUT, "output[2]"),  # output [bit 2]
            BP((-5, 0, -2), OUTPUT, "output[1]"),  # output [bit 1]
            BP((-4, 0, -2), OUTPUT, "output[0]"),  # output [bit 0]
            BP((2, 0, 2), INPUT, "value[7]"),  # value [bit 7]
            BP((3, 0, 2), INPUT, "value[6]"),  # value [bit 6]
            BP((4, 0, 2), INPUT, "value[5]"),  # value [bit 5]
            BP((5, 0, 2), INPUT, "value[4]"),  # value [bit 4]
            BP((6, 0, 2), INPUT, "value[3]"),  # value [bit 3]
            BP((7, 0, 2), INPUT, "value[2]"),  # value [bit 2]
            BP((8, 0, 2), INPUT, "value[1]"),  # value [bit 1]
            BP((9, 0, 2), INPUT, "value[0]"),  # value [bit 0]
            BP((11, 0, 2), INPUT, "write"),  # write
        ]
    ),
    BuildingType.MASSIVE_MEMORY: BuildingProperties(
        blocks=[
            BP((-15, 0, 2), INPUT, "input[11]"),  # address [bit 11]
            BP((-6, 0, 2), INPUT, "input[2]"),  # address [bit 2]
            BP((-5, 0, 2), INPUT, "input[1]"),  # address [bit 1]
            BP((-4, 0, 2), INPUT, "input[0]"),  # address [bit 0]
            BP((-14, 0, 2), INPUT, "input[10]"),  # address [bit 10]
            BP((-13, 0, 2), INPUT, "input[9]"),  # address [bit 9]
            BP((-12, 0, 2), INPUT, "input[8]"),  # address [bit 8]
            BP((-11, 0, 2), INPUT, "input[7]"),  # address [bit 7]
            BP((-10, 0, 2), INPUT, "input[6]"),  # address [bit 6]
            BP((-9, 0, 2), INPUT, "input[5]"),  # address [bit 5]
            BP((-8, 0, 2), INPUT, "input[4]"),  # address [bit 4]
            BP((-7, 0, 2), INPUT, "input[3]"),  # address [bit 3]
            BP((-15, 0, -2), OUTPUT, "output[15]"),  # output [bit 15]
            BP((-6, 0, -2), OUTPUT, "output[6]"),  # output [bit 6]
            BP((-5, 0, -2), OUTPUT, "output[5]"),  # output [bit 5]
            BP((-4, 0, -2), OUTPUT, "output[4]"),  # output [bit 4]
            BP((-3, 0, -2), OUTPUT, "output[3]"),  # output [bit 3]
            BP((-2, 0, -2), OUTPUT, "output[2]"),  # output [bit 2]
            BP((-1, 0, -2), OUTPUT, "output[1]"),  # output [bit 1]
            BP((0, 0, -2), OUTPUT, "output[0]"),  # output [bit 0]
            BP((-14, 0, -2), OUTPUT, "output[14]"),  # output [bit 14]
            BP((-13, 0, -2), OUTPUT, "output[13]"),  # output [bit 13]
            BP((-12, 0, -2), OUTPUT, "output[12]"),  # output [bit 12]
            BP((-11, 0, -2), OUTPUT, "output[11]"),  # output [bit 11]
            BP((-10, 0, -2), OUTPUT, "output[10]"),  # output [bit 10]
            BP((-9, 0, -2), OUTPUT, "output[9]"),  # output [bit 9]
            BP((-8, 0, -2), OUTPUT, "output[8]"),  # output [bit 8]
            BP((-7, 0, -2), OUTPUT, "output[7]"),  # output [bit 7]
            BP((-2, 0, 2), INPUT, "value[15]"),  # value [bit 15]
            BP((7, 0, 2), INPUT, "value[6]"),  # value [bit 6]
            BP((8, 0, 2), INPUT, "value[5]"),  # value [bit 5]
            BP((9, 0, 2), INPUT, "value[4]"),  # value [bit 4]
            BP((10, 0, 2), INPUT, "value[3]"),  # value [bit 3]
            BP((11, 0, 2), INPUT, "value[2]"),  # value [bit 2]
            BP((12, 0, 2), INPUT, "value[1]"),  # value [bit 1]
            BP((13, 0, 2), INPUT, "value[0]"),  # value [bit 0]
            BP((-1, 0, 2), INPUT, "value[14]"),  # value [bit 14]
            BP((0, 0, 2), INPUT, "value[13]"),  # value [bit 13]
            BP((1, 0, 2), INPUT, "value[12]"),  # value [bit 12]
            BP((2, 0, 2), INPUT, "value[11]"),  # value [bit 11]
            BP((3, 0, 2), INPUT, "value[10]"),  # value [bit 10]
            BP((4, 0, 2), INPUT, "value[9]"),  # value [bit 9]
            BP((5, 0, 2), INPUT, "value[8]"),  # value [bit 8]
            BP((6, 0, 2), INPUT, "value[7]"),  # value [bit 7]
            BP((15, 0, 2), INPUT, "write"),  # write
        ]
    ),
    BuildingType.MULTIPLIER: BuildingProperties(
        blocks=[
            BP((-1, 0, 7), INPUT, "a[15]"),  # A [bit 15]
            BP((7, 0, 7), INPUT, "a[6]"),  # A [bit 6]
            BP((8, 0, 7), INPUT, "a[5]"),  # A [bit 5]
            BP((9, 0, 7), INPUT, "a[4]"),  # A [bit 4]
            BP((10, 0, 7), INPUT, "a[3]"),  # A [bit 3]
            BP((11, 0, 7), INPUT, "a[2]"),  # A [bit 2]
            BP((12, 0, 7), INPUT, "a[1]"),  # A [bit 1]
            BP((13, 0, 7), INPUT, "a[0]"),  # A [bit 0]
            BP((0, 0, 7), INPUT, "a[14]"),  # A [bit 14]
            BP((1, 0, 7), INPUT, "a[13]"),  # A [bit 13]
            BP((2, 0, 7), INPUT, "a[12]"),  # A [bit 12]
            BP((3, 0, 7), INPUT, "a[11]"),  # A [bit 11]
            BP((3, 0, 7), INPUT, "a[10]"),  # A [bit 10]
            BP((4, 0, 7), INPUT, "a[9]"),  # A [bit 9]
            BP((5, 0, 7), INPUT, "a[8]"),  # A [bit 8]
            BP((6, 0, 7), INPUT, "a[7]"),  # A [bit 7]
            BP((16, 0, 7), INPUT, "b[15]"),  # B [bit 15]
            BP((25, 0, 7), INPUT, "b[6]"),  # B [bit 6]
            BP((26, 0, 7), INPUT, "b[5]"),  # B [bit 5]
            BP((27, 0, 7), INPUT, "b[4]"),  # B [bit 4]
            BP((28, 0, 7), INPUT, "b[3]"),  # B [bit 3]
            BP((29, 0, 7), INPUT, "b[2]"),  # B [bit 2]
            BP((30, 0, 7), INPUT, "b[1]"),  # B [bit 1]
            BP((31, 0, 7), INPUT, "b[0]"),  # B [bit 0]
            BP((17, 0, 7), INPUT, "b[14]"),  # B [bit 14]
            BP((18, 0, 7), INPUT, "b[13]"),  # B [bit 13]
            BP((19, 0, 7), INPUT, "b[12]"),  # B [bit 12]
            BP((20, 0, 7), INPUT, "b[11]"),  # B [bit 11]
            BP((21, 0, 7), INPUT, "b[10]"),  # B [bit 10]
            BP((22, 0, 7), INPUT, "b[9]"),  # B [bit 9]
            BP((23, 0, 7), INPUT, "b[8]"),  # B [bit 8]
            BP((24, 0, 7), INPUT, "b[7]"),  # B [bit 7]
            BP((-1, 0, -1), OUTPUT, "output[31]"),  # Output [bit 31]
            BP((7, 0, -1), OUTPUT, "output[22]"),  # Output [bit 22]
            BP((8, 0, -1), OUTPUT, "output[21]"),  # Output [bit 21]
            BP((9, 0, -1), OUTPUT, "output[20]"),  # Output [bit 20]
            BP((10, 0, -1), OUTPUT, "output[19]"),  # Output [bit 19]
            BP((11, 0, -1), OUTPUT, "output[18]"),  # Output [bit 18]
            BP((12, 0, -1), OUTPUT, "output[17]"),  # Output [bit 17]
            BP((13, 0, -1), OUTPUT, "output[16]"),  # Output [bit 16]
            BP((16, 0, -1), OUTPUT, "output[15]"),  # Output [bit 15]
            BP((17, 0, -1), OUTPUT, "output[14]"),  # Output [bit 14]
            BP((18, 0, -1), OUTPUT, "output[13]"),  # Output [bit 13]
            BP((0, 0, -1), OUTPUT, "output[30]"),  # Output [bit 30]
            BP((19, 0, -1), OUTPUT, "output[12]"),  # Output [bit 12]
            BP((20, 0, -1), OUTPUT, "output[11]"),  # Output [bit 11]
            BP((21, 0, -1), OUTPUT, "output[10]"),  # Output [bit 10]
            BP((22, 0, -1), OUTPUT, "output[9]"),  # Output [bit 9]
            BP((23, 0, -1), OUTPUT, "output[8]"),  # Output [bit 8]
            BP((24, 0, -1), OUTPUT, "output[7]"),  # Output [bit 7]
            BP((25, 0, -1), OUTPUT, "output[6]"),  # Output [bit 6]
            BP((26, 0, -1), OUTPUT, "output[5]"),  # Output [bit 5]
            BP((27, 0, -1), OUTPUT, "output[4]"),  # Output [bit 4]
            BP((28, 0, -1), OUTPUT, "output[3]"),  # Output [bit 3]
            BP((1, 0, -1), OUTPUT, "output[29]"),  # Output [bit 29]
            BP((29, 0, -1), OUTPUT, "output[2]"),  # Output [bit 2]
            BP((30, 0, -1), OUTPUT, "output[1]"),  # Output [bit 1]
            BP((31, 0, -1), OUTPUT, "output[0]"),  # Output [bit 0]
            BP((2, 0, -1), OUTPUT, "output[28]"),  # Output [bit 28]
            BP((3, 0, -1), OUTPUT, "output[27]"),  # Output [bit 27]
            BP((3, 0, -1), OUTPUT, "output[26]"),  # Output [bit 26]
            BP((4, 0, -1), OUTPUT, "output[25]"),  # Output [bit 25]
            BP((5, 0, -1), OUTPUT, "output[24]"),  # Output [bit 24]
            BP((6, 0, -1), OUTPUT, "output[23]"),  # Output [bit 23]
        ]
    ),
    BuildingType.N_TRANSISTOR: BuildingProperties(
        blocks=[
            BP((1, 0, 0), BIDIRECTIONAL, "drain"),  # Drain (right)
            BP((0, 0, 1), INPUT, "gate"),  # Gate (bottom)
            BP((-1, 0, 0), BIDIRECTIONAL, "source"),  # Source (left)
        ]
    ),
    BuildingType.P_TRANSISTOR: BuildingProperties(
        blocks=[
            BP((1, 0, 0), BIDIRECTIONAL, "drain"),  # Drain (right)
            BP((0, 0, 1), INPUT, "gate"),  # Gate (bottom)
            BP((-1, 0, 0), BIDIRECTIONAL, "source"),  # Source (left)
        ]
    ),
    BuildingType.PIXEL_DISPLAY: BuildingProperties(
        blocks=[
            BP((4, 0, 10), INPUT, "pixel"),  # Pixel
            BP((6, 0, 10), INPUT, "reset"),  # Reset
            BP((8, 0, 10), INPUT, "write"),  # Write
            BP((-8, 0, 10), INPUT, "x[4]"),  # X [bit 4]
            BP((-7, 0, 10), INPUT, "x[3]"),  # X [bit 3]
            BP((-6, 0, 10), INPUT, "x[2]"),  # X [bit 2]
            BP((-5, 0, 10), INPUT, "x[1]"),  # X [bit 1]
            BP((-4, 0, 10), INPUT, "x[0]"),  # X [bit 0]
            BP((-2, 0, 10), INPUT, "y[4]"),  # Y [bit 4]
            BP((-1, 0, 10), INPUT, "y[3]"),  # Y [bit 3]
            BP((0, 0, 10), INPUT, "y[2]"),  # Y [bit 2]
            BP((1, 0, 10), INPUT, "y[1]"),  # Y [bit 1]
            BP((2, 0, 10), INPUT, "y[0]"),  # Y [bit 0]
        ]
    ),
    BuildingType.QWERTY_KEY_INPUT: BuildingProperties(
        blocks=[
            BP((2, 1, -4), OUTPUT, "zero"),  # 0
            BP((-7, 1, -4), OUTPUT, "one"),  # 1
            BP((-6, 1, -4), OUTPUT, "two"),  # 2
            BP((-5, 1, -4), OUTPUT, "three"),  # 3
            BP((-4, 1, -4), OUTPUT, "four"),  # 4
            BP((-3, 1, -4), OUTPUT, "five"),  # 5
            BP((-2, 1, -4), OUTPUT, "six"),  # 6
            BP((-1, 1, -4), OUTPUT, "seven"),  # 7
            BP((0, 1, -4), OUTPUT, "eight"),  # 8
            BP((1, 1, -4), OUTPUT, "nine"),  # 9
            BP((-7, 1, -2), OUTPUT, "a"),  # A
            BP((-7, 1, 0), OUTPUT, "leftAlt"),  # left alt
            BP((2, 1, 0), OUTPUT, "rightALt"),  # right alt
            BP((3, 1, -2), OUTPUT, "apostrophe"),  # '
            BP((-3, 1, -1), OUTPUT, "b"),  # B
            BP((5, 1, -3), OUTPUT, "backslash"),  # \
            BP((5, 1, -4), OUTPUT, "backspace"),  # backspace
            BP((-5, 1, -1), OUTPUT, "c"),  # C
            BP((-8, 1, -2), OUTPUT, "capsLock"),  # caps lock
            BP((0, 1, -1), OUTPUT, "comma"),  # ,
            BP((-8, 1, 0), OUTPUT, "leftCtrl"),  # left ctrl
            BP((3, 1, 0), OUTPUT, "rightCtrl"),  # right ctrl
            BP((-5, 1, -2), OUTPUT, "d"),  # D
            BP((7, 1, 0), OUTPUT, "down"),  # down
            BP((-5, 1, -3), OUTPUT, "e"),  # E
            BP((4, 1, -2), OUTPUT, "enter"),  # enter
            BP((4, 1, -4), OUTPUT, "equals"),  # =
            BP((-4, 1, -2), OUTPUT, "f"),  # F
            BP((-3, 1, -2), OUTPUT, "g"),  # G
            BP((-2, 1, -2), OUTPUT, "h"),  # H
            BP((0, 1, -3), OUTPUT, "i"),  # I
            BP((-1, 1, -2), OUTPUT, "j"),  # J
            BP((0, 1, -2), OUTPUT, "k"),  # K
            BP((1, 1, -2), OUTPUT, "l"),  # L
            BP((6, 1, 0), OUTPUT, "left"),  # left
            BP((-1, 1, -1), OUTPUT, "m"),  # M
            BP((3, 1, -4), OUTPUT, "minus"),  # -
            BP((-2, 1, -1), OUTPUT, "n"),  # N
            BP((1, 1, -3), OUTPUT, "o"),  # O
            BP((2, 1, -3), OUTPUT, "p"),  # P
            BP((1, 1, -1), OUTPUT, "period"),  # .
            BP((-7, 1, -3), OUTPUT, "q"),  # Q
            BP((-4, 1, -3), OUTPUT, "r"),  # R
            BP((8, 1, 0), OUTPUT, "right"),  # right
            BP((-6, 1, -2), OUTPUT, "s"),  # S
            BP((2, 1, -2), OUTPUT, "semicolon"),  # ;
            BP((-8, 1, -1), OUTPUT, "leftShift"),  # left shift
            BP((3, 1, -1), OUTPUT, "rightShift"),  # right shift
            BP((2, 1, -1), OUTPUT, "slash"),  # /
            BP((-2, 1, 0), OUTPUT, "space"),  # space
            BP((3, 1, -3), OUTPUT, "leftBracket"),  # [
            BP((4, 1, -3), OUTPUT, "rightBracket"),  # ]
            BP((-3, 1, -3), OUTPUT, "t"),  # T
            BP((-8, 1, -3), OUTPUT, "tab"),  # tab
            BP((-8, 1, -4), OUTPUT, "backtick"),  # `
            BP((-1, 1, -3), OUTPUT, "u"),  # U
            BP((7, 1, -1), OUTPUT, "up"),  # up
            BP((-4, 1, -1), OUTPUT, "v"),  # V
            BP((-6, 1, -3), OUTPUT, "w"),  # W
            BP((-6, 1, -1), OUTPUT, "x"),  # X
            BP((-2, 1, -3), OUTPUT, "y"),  # Y
            BP((-7, 1, -1), OUTPUT, "z"),  # Z
        ]
    ),
    BuildingType.RGB_DISPLAY: BuildingProperties(
        blocks=[
            BP((8, 0, 18), INPUT, "b[3]"),  # B [bit 3]
            BP((9, 0, 18), INPUT, "b[2]"),  # B [bit 2]
            BP((10, 0, 18), INPUT, "b[1]"),  # B [bit 1]
            BP((11, 0, 18), INPUT, "b[0]"),  # B [bit 0]
            BP((3, 0, 18), INPUT, "g[3]"),  # G [bit 3]
            BP((4, 0, 18), INPUT, "g[2]"),  # G [bit 2]
            BP((5, 0, 18), INPUT, "g[1]"),  # G [bit 1]
            BP((6, 0, 18), INPUT, "g[0]"),  # G [bit 0]
            BP((-2, 0, 18), INPUT, "r[3]"),  # R [bit 3]
            BP((-1, 0, 18), INPUT, "r[2]"),  # R [bit 2]
            BP((0, 0, 18), INPUT, "r[1]"),  # R [bit 1]
            BP((1, 0, 18), INPUT, "r[0]"),  # R [bit 0]
            BP((13, 0, 18), INPUT, "reset"),  # Reset
            BP((14, 0, 18), INPUT, "write"),  # Write
            BP((-14, 0, 18), INPUT, "x[4]"),  # X [bit 4]
            BP((-13, 0, 18), INPUT, "x[3]"),  # X [bit 3]
            BP((-12, 0, 18), INPUT, "x[2]"),  # X [bit 2]
            BP((-11, 0, 18), INPUT, "x[1]"),  # X [bit 1]
            BP((-10, 0, 18), INPUT, "x[0]"),  # X [bit 0]
            BP((-8, 0, 18), INPUT, "y[4]"),  # Y [bit 4]
            BP((-7, 0, 18), INPUT, "y[3]"),  # Y [bit 3]
            BP((-6, 0, 18), INPUT, "y[2]"),  # Y [bit 2]
            BP((-5, 0, 18), INPUT, "y[1]"),  # Y [bit 1]
            BP((-4, 0, 18), INPUT, "y[0]"),  # Y [bit 0]
        ]
    ),
    BuildingType.REAL_TIME_CLOCK: BuildingProperties(
        blocks=[
            BP((9, 0, -1), INPUT, "change"),  # CHG
            BP((0, 0, -1), INPUT, "sign"),  # +/-
            BP((12, 0, -1), INPUT, "hold"),  # HOL
            BP((10, 0, -1), INPUT, "reset"),  # RST
            BP((11, 0, -1), INPUT, "sync"),  # SYN
            BP((5, 0, -1), INPUT, "1dInput"),  # 1D input
            BP((4, 0, -1), INPUT, "1hInput"),  # 1h input
            BP((3, 0, -1), INPUT, "1mInput"),  # 1m input
            BP((2, 0, -1), INPUT, "1sInput"),  # 1s input
            BP((31, 0, -1), OUTPUT, "1dOutput"),  # 1D output
            BP((30, 0, -1), OUTPUT, "1hOutput"),  # 1h output
            BP((29, 0, -1), OUTPUT, "1mOutput"),  # 1m output
            BP((28, 0, -1), OUTPUT, "1sOutput"),  # 1s output
            BP((31, 0, 4), OUTPUT, "timestamp[0]"),  # Timestamp [bit 0]
            BP((22, 0, 4), OUTPUT, "timestamp[9]"),  # Timestamp [bit 9]
            BP((21, 0, 4), OUTPUT, "timestamp[10]"),  # Timestamp [bit 10]
            BP((20, 0, 4), OUTPUT, "timestamp[11]"),  # Timestamp [bit 11]
            BP((19, 0, 4), OUTPUT, "timestamp[12]"),  # Timestamp [bit 12]
            BP((18, 0, 4), OUTPUT, "timestamp[13]"),  # Timestamp [bit 13]
            BP((17, 0, 4), OUTPUT, "timestamp[14]"),  # Timestamp [bit 14]
            BP((16, 0, 4), OUTPUT, "timestamp[15]"),  # Timestamp [bit 15]
            BP((15, 0, 4), OUTPUT, "timestamp[16]"),  # Timestamp [bit 16]
            BP((14, 0, 4), OUTPUT, "timestamp[17]"),  # Timestamp [bit 17]
            BP((13, 0, 4), OUTPUT, "timestamp[18]"),  # Timestamp [bit 18]
            BP((30, 0, 4), OUTPUT, "timestamp[1]"),  # Timestamp [bit 1]
            BP((12, 0, 4), OUTPUT, "timestamp[19]"),  # Timestamp [bit 19]
            BP((11, 0, 4), OUTPUT, "timestamp[20]"),  # Timestamp [bit 20]
            BP((10, 0, 4), OUTPUT, "timestamp[21]"),  # Timestamp [bit 21]
            BP((9, 0, 4), OUTPUT, "timestamp[22]"),  # Timestamp [bit 22]
            BP((8, 0, 4), OUTPUT, "timestamp[23]"),  # Timestamp [bit 23]
            BP((7, 0, 4), OUTPUT, "timestamp[24]"),  # Timestamp [bit 24]
            BP((6, 0, 4), OUTPUT, "timestamp[25]"),  # Timestamp [bit 25]
            BP((5, 0, 4), OUTPUT, "timestamp[26]"),  # Timestamp [bit 26]
            BP((4, 0, 4), OUTPUT, "timestamp[27]"),  # Timestamp [bit 27]
            BP((3, 0, 4), OUTPUT, "timestamp[28]"),  # Timestamp [bit 28]
            BP((29, 0, 4), OUTPUT, "timestamp[2]"),  # Timestamp [bit 2]
            BP((2, 0, 4), OUTPUT, "timestamp[29]"),  # Timestamp [bit 29]
            BP((1, 0, 4), OUTPUT, "timestamp[30]"),  # Timestamp [bit 30]
            BP((0, 0, 4), OUTPUT, "timestamp[31]"),  # Timestamp [bit 31]
            BP((28, 0, 4), OUTPUT, "timestamp[3]"),  # Timestamp [bit 3]
            BP((27, 0, 4), OUTPUT, "timestamp[4]"),  # Timestamp [bit 4]
            BP((26, 0, 4), OUTPUT, "timestamp[5]"),  # Timestamp [bit 5]
            BP((25, 0, 4), OUTPUT, "timestamp[6]"),  # Timestamp [bit 6]
            BP((24, 0, 4), OUTPUT, "timestamp[7]"),  # Timestamp [bit 7]
            BP((23, 0, 4), OUTPUT, "timestamp[8]"),  # Timestamp [bit 8]
        ]
    ),
    BuildingType.SIGN: BuildingProperties(
        blocks=[
            BP((-4, 0, -4), INPUT, "input"),
        ]
    ),
    BuildingType.TEXT_CONSOLE: BuildingProperties(
        blocks=[
            BP((-1, 0, 9), INPUT, "char[7]"),  # Char [bit 7]
            BP((0, 0, 9), INPUT, "char[6]"),  # Char [bit 6]
            BP((1, 0, 9), INPUT, "char[5]"),  # Char [bit 5]
            BP((2, 0, 9), INPUT, "char[4]"),  # Char [bit 4]
            BP((3, 0, 9), INPUT, "char[3]"),  # Char [bit 3]
            BP((4, 0, 9), INPUT, "char[2]"),  # Char [bit 2]
            BP((5, 0, 9), INPUT, "char[1]"),  # Char [bit 1]
            BP((6, 0, 9), INPUT, "char[0]"),  # Char [bit 0]
            BP((8, 0, 9), INPUT, "clear"),  # Clear
            BP((9, 0, 9), INPUT, "cursor"),  # Cursor
            BP((-10, 0, 9), INPUT, "location[7]"),  # Location [bit 7]
            BP((-9, 0, 9), INPUT, "location[6]"),  # Location [bit 6]
            BP((-8, 0, 9), INPUT, "location[5]"),  # Location [bit 5]
            BP((-7, 0, 9), INPUT, "location[4]"),  # Location [bit 4]
            BP((-6, 0, 9), INPUT, "location[3]"),  # Location [bit 3]
            BP((-5, 0, 9), INPUT, "location[2]"),  # Location [bit 2]
            BP((-4, 0, 9), INPUT, "location[1]"),  # Location [bit 1]
            BP((-3, 0, 9), INPUT, "location[0]"),  # Location [bit 0]
            BP((10, 0, 9), INPUT, "write"),  # Write
        ]
    ),
    BuildingType.DIVIDER_32_BIT: BuildingProperties(
        blocks=[
            BP((-1, 0, 7), INPUT, "a[31]"),  # A [bit 31]
            BP((8, 0, 7), INPUT, "a[22]"),  # A [bit 22]
            BP((9, 0, 7), INPUT, "a[21]"),  # A [bit 21]
            BP((10, 0, 7), INPUT, "a[20]"),  # A [bit 20]
            BP((11, 0, 7), INPUT, "a[19]"),  # A [bit 19]
            BP((12, 0, 7), INPUT, "a[18]"),  # A [bit 18]
            BP((13, 0, 7), INPUT, "a[17]"),  # A [bit 17]
            BP((14, 0, 7), INPUT, "a[16]"),  # A [bit 16]
            BP((15, 0, 7), INPUT, "a[15]"),  # A [bit 15]
            BP((16, 0, 7), INPUT, "a[14]"),  # A [bit 14]
            BP((17, 0, 7), INPUT, "a[13]"),  # A [bit 13]
            BP((0, 0, 7), INPUT, "a[30]"),  # A [bit 30]
            BP((18, 0, 7), INPUT, "a[12]"),  # A [bit 12]
            BP((19, 0, 7), INPUT, "a[11]"),  # A [bit 11]
            BP((20, 0, 7), INPUT, "a[10]"),  # A [bit 10]
            BP((21, 0, 7), INPUT, "a[9]"),  # A [bit 9]
            BP((22, 0, 7), INPUT, "a[8]"),  # A [bit 8]
            BP((23, 0, 7), INPUT, "a[7]"),  # A [bit 7]
            BP((24, 0, 7), INPUT, "a[6]"),  # A [bit 6]
            BP((25, 0, 7), INPUT, "a[5]"),  # A [bit 5]
            BP((26, 0, 7), INPUT, "a[4]"),  # A [bit 4]
            BP((27, 0, 7), INPUT, "a[3]"),  # A [bit 3]
            BP((1, 0, 7), INPUT, "a[29]"),  # A [bit 29]
            BP((28, 0, 7), INPUT, "a[2]"),  # A [bit 2]
            BP((29, 0, 7), INPUT, "a[1]"),  # A [bit 1]
            BP((30, 0, 7), INPUT, "a[0]"),  # A [bit 0]
            BP((2, 0, 7), INPUT, "a[28]"),  # A [bit 28]
            BP((3, 0, 7), INPUT, "a[27]"),  # A [bit 27]
            BP((4, 0, 7), INPUT, "a[26]"),  # A [bit 26]
            BP((5, 0, 7), INPUT, "a[25]"),  # A [bit 25]
            BP((6, 0, 7), INPUT, "a[24]"),  # A [bit 24]
            BP((7, 0, 7), INPUT, "a[23]"),  # A [bit 23]
            BP((33, 0, 7), INPUT, "b[31]"),  # B [bit 31]
            BP((42, 0, 7), INPUT, "b[22]"),  # B [bit 22]
            BP((43, 0, 7), INPUT, "b[21]"),  # B [bit 21]
            BP((44, 0, 7), INPUT, "b[20]"),  # B [bit 20]
            BP((45, 0, 7), INPUT, "b[19]"),  # B [bit 19]
            BP((46, 0, 7), INPUT, "b[18]"),  # B [bit 18]
            BP((47, 0, 7), INPUT, "b[17]"),  # B [bit 17]
            BP((48, 0, 7), INPUT, "b[16]"),  # B [bit 16]
            BP((49, 0, 7), INPUT, "b[15]"),  # B [bit 15]
            BP((50, 0, 7), INPUT, "b[14]"),  # B [bit 14]
            BP((51, 0, 7), INPUT, "b[13]"),  # B [bit 13]
            BP((34, 0, 7), INPUT, "b[30]"),  # B [bit 30]
            BP((52, 0, 7), INPUT, "b[12]"),  # B [bit 12]
            BP((53, 0, 7), INPUT, "b[11]"),  # B [bit 11]
            BP((54, 0, 7), INPUT, "b[10]"),  # B [bit 10]
            BP((55, 0, 7), INPUT, "b[9]"),  # B [bit 9]
            BP((56, 0, 7), INPUT, "b[8]"),  # B [bit 8]
            BP((57, 0, 7), INPUT, "b[7]"),  # B [bit 7]
            BP((58, 0, 7), INPUT, "b[6]"),  # B [bit 6]
            BP((59, 0, 7), INPUT, "b[5]"),  # B [bit 5]
            BP((60, 0, 7), INPUT, "b[4]"),  # B [bit 4]
            BP((61, 0, 7), INPUT, "b[3]"),  # B [bit 3]
            BP((35, 0, 7), INPUT, "b[29]"),  # B [bit 29]
            BP((62, 0, 7), INPUT, "b[2]"),  # B [bit 2]
            BP((63, 0, 7), INPUT, "b[1]"),  # B [bit 1]
            BP((64, 0, 7), INPUT, "b[0]"),  # B [bit 0]
            BP((36, 0, 7), INPUT, "b[28]"),  # B [bit 28]
            BP((37, 0, 7), INPUT, "b[27]"),  # B [bit 27]
            BP((38, 0, 7), INPUT, "b[26]"),  # B [bit 26]
            BP((39, 0, 7), INPUT, "b[25]"),  # B [bit 25]
            BP((40, 0, 7), INPUT, "b[24]"),  # B [bit 24]
            BP((41, 0, 7), INPUT, "b[23]"),  # B [bit 23]
            BP((-1, 0, -1), OUTPUT, "quotient[31]"),  # Quotient [bit 31]
            BP((8, 0, -1), OUTPUT, "quotient[22]"),  # Quotient [bit 22]
            BP((9, 0, -1), OUTPUT, "quotient[21]"),  # Quotient [bit 21]
            BP((10, 0, -1), OUTPUT, "quotient[20]"),  # Quotient [bit 20]
            BP((11, 0, -1), OUTPUT, "quotient[19]"),  # Quotient [bit 19]
            BP((12, 0, -1), OUTPUT, "quotient[18]"),  # Quotient [bit 18]
            BP((13, 0, -1), OUTPUT, "quotient[17]"),  # Quotient [bit 17]
            BP((14, 0, -1), OUTPUT, "quotient[16]"),  # Quotient [bit 16]
            BP((15, 0, -1), OUTPUT, "quotient[15]"),  # Quotient [bit 15]
            BP((16, 0, -1), OUTPUT, "quotient[14]"),  # Quotient [bit 14]
            BP((17, 0, -1), OUTPUT, "quotient[13]"),  # Quotient [bit 13]
            BP((0, 0, -1), OUTPUT, "quotient[30]"),  # Quotient [bit 30]
            BP((18, 0, -1), OUTPUT, "quotient[12]"),  # Quotient [bit 12]
            BP((19, 0, -1), OUTPUT, "quotient[11]"),  # Quotient [bit 11]
            BP((20, 0, -1), OUTPUT, "quotient[10]"),  # Quotient [bit 10]
            BP((21, 0, -1), OUTPUT, "quotient[9]"),  # Quotient [bit 9]
            BP((22, 0, -1), OUTPUT, "quotient[8]"),  # Quotient [bit 8]
            BP((23, 0, -1), OUTPUT, "quotient[7]"),  # Quotient [bit 7]
            BP((24, 0, -1), OUTPUT, "quotient[6]"),  # Quotient [bit 6]
            BP((25, 0, -1), OUTPUT, "quotient[5]"),  # Quotient [bit 5]
            BP((26, 0, -1), OUTPUT, "quotient[4]"),  # Quotient [bit 4]
            BP((27, 0, -1), OUTPUT, "quotient[3]"),  # Quotient [bit 3]
            BP((1, 0, -1), OUTPUT, "quotient[29]"),  # Quotient [bit 29]
            BP((28, 0, -1), OUTPUT, "quotient[2]"),  # Quotient [bit 2]
            BP((29, 0, -1), OUTPUT, "quotient[1]"),  # Quotient [bit 1]
            BP((30, 0, -1), OUTPUT, "quotient[0]"),  # Quotient [bit 0]
            BP((2, 0, -1), OUTPUT, "quotient[28]"),  # Quotient [bit 28]
            BP((3, 0, -1), OUTPUT, "quotient[27]"),  # Quotient [bit 27]
            BP((4, 0, -1), OUTPUT, "quotient[26]"),  # Quotient [bit 26]
            BP((5, 0, -1), OUTPUT, "quotient[25]"),  # Quotient [bit 25]
            BP((6, 0, -1), OUTPUT, "quotient[24]"),  # Quotient [bit 24]
            BP((7, 0, -1), OUTPUT, "quotient[23]"),  # Quotient [bit 23]
            BP((33, 0, -1), OUTPUT, "remainder[31]"),  # Remainder [bit 31]
            BP((42, 0, -1), OUTPUT, "remainder[22]"),  # Remainder [bit 22]
            BP((43, 0, -1), OUTPUT, "remainder[21]"),  # Remainder [bit 21]
            BP((44, 0, -1), OUTPUT, "remainder[20]"),  # Remainder [bit 20]
            BP((45, 0, -1), OUTPUT, "remainder[19]"),  # Remainder [bit 19]
            BP((46, 0, -1), OUTPUT, "remainder[18]"),  # Remainder [bit 18]
            BP((47, 0, -1), OUTPUT, "remainder[17]"),  # Remainder [bit 17]
            BP((48, 0, -1), OUTPUT, "remainder[16]"),  # Remainder [bit 16]
            BP((49, 0, -1), OUTPUT, "remainder[15]"),  # Remainder [bit 15]
            BP((50, 0, -1), OUTPUT, "remainder[14]"),  # Remainder [bit 14]
            BP((51, 0, -1), OUTPUT, "remainder[13]"),  # Remainder [bit 13]
            BP((34, 0, -1), OUTPUT, "remainder[30]"),  # Remainder [bit 30]
            BP((52, 0, -1), OUTPUT, "remainder[12]"),  # Remainder [bit 12]
            BP((53, 0, -1), OUTPUT, "remainder[11]"),  # Remainder [bit 11]
            BP((54, 0, -1), OUTPUT, "remainder[10]"),  # Remainder [bit 10]
            BP((55, 0, -1), OUTPUT, "remainder[9]"),  # Remainder [bit 9]
            BP((56, 0, -1), OUTPUT, "remainder[8]"),  # Remainder [bit 8]
            BP((57, 0, -1), OUTPUT, "remainder[7]"),  # Remainder [bit 7]
            BP((58, 0, -1), OUTPUT, "remainder[6]"),  # Remainder [bit 6]
            BP((59, 0, -1), OUTPUT, "remainder[5]"),  # Remainder [bit 5]
            BP((60, 0, -1), OUTPUT, "remainder[4]"),  # Remainder [bit 4]
            BP((61, 0, -1), OUTPUT, "remainder[3]"),  # Remainder [bit 3]
            BP((35, 0, -1), OUTPUT, "remainder[29]"),  # Remainder [bit 29]
            BP((62, 0, -1), OUTPUT, "remainder[2]"),  # Remainder [bit 2]
            BP((63, 0, -1), OUTPUT, "remainder[1]"),  # Remainder [bit 1]
            BP((64, 0, -1), OUTPUT, "remainder[0]"),  # Remainder [bit 0]
            BP((36, 0, -1), OUTPUT, "remainder[28]"),  # Remainder [bit 28]
            BP((37, 0, -1), OUTPUT, "remainder[27]"),  # Remainder [bit 27]
            BP((38, 0, -1), OUTPUT, "remainder[26]"),  # Remainder [bit 26]
            BP((39, 0, -1), OUTPUT, "remainder[25]"),  # Remainder [bit 25]
            BP((40, 0, -1), OUTPUT, "remainder[24]"),  # Remainder [bit 24]
            BP((41, 0, -1), OUTPUT, "remainder[23]"),  # Remainder [bit 23]
        ]
    ),
    BuildingType.DIVIDER_32_BIT: BuildingProperties(
        blocks=[
            BP((-1, 0, 7), INPUT, "a[31]"),  # A [bit 31]
            BP((8, 0, 7), INPUT, "a[22]"),  # A [bit 22]
            BP((9, 0, 7), INPUT, "a[21]"),  # A [bit 21]
            BP((10, 0, 7), INPUT, "a[20]"),  # A [bit 20]
            BP((11, 0, 7), INPUT, "a[19]"),  # A [bit 19]
            BP((12, 0, 7), INPUT, "a[18]"),  # A [bit 18]
            BP((13, 0, 7), INPUT, "a[17]"),  # A [bit 17]
            BP((14, 0, 7), INPUT, "a[16]"),  # A [bit 16]
            BP((15, 0, 7), INPUT, "a[15]"),  # A [bit 15]
            BP((16, 0, 7), INPUT, "a[14]"),  # A [bit 14]
            BP((17, 0, 7), INPUT, "a[13]"),  # A [bit 13]
            BP((0, 0, 7), INPUT, "a[30]"),  # A [bit 30]
            BP((18, 0, 7), INPUT, "a[12]"),  # A [bit 12]
            BP((19, 0, 7), INPUT, "a[11]"),  # A [bit 11]
            BP((20, 0, 7), INPUT, "a[10]"),  # A [bit 10]
            BP((21, 0, 7), INPUT, "a[9]"),  # A [bit 9]
            BP((22, 0, 7), INPUT, "a[8]"),  # A [bit 8]
            BP((23, 0, 7), INPUT, "a[7]"),  # A [bit 7]
            BP((24, 0, 7), INPUT, "a[6]"),  # A [bit 6]
            BP((25, 0, 7), INPUT, "a[5]"),  # A [bit 5]
            BP((26, 0, 7), INPUT, "a[4]"),  # A [bit 4]
            BP((27, 0, 7), INPUT, "a[3]"),  # A [bit 3]
            BP((1, 0, 7), INPUT, "a[29]"),  # A [bit 29]
            BP((28, 0, 7), INPUT, "a[2]"),  # A [bit 2]
            BP((29, 0, 7), INPUT, "a[1]"),  # A [bit 1]
            BP((30, 0, 7), INPUT, "a[0]"),  # A [bit 0]
            BP((2, 0, 7), INPUT, "a[28]"),  # A [bit 28]
            BP((3, 0, 7), INPUT, "a[27]"),  # A [bit 27]
            BP((4, 0, 7), INPUT, "a[26]"),  # A [bit 26]
            BP((5, 0, 7), INPUT, "a[25]"),  # A [bit 25]
            BP((6, 0, 7), INPUT, "a[24]"),  # A [bit 24]
            BP((7, 0, 7), INPUT, "a[23]"),  # A [bit 23]
            BP((33, 0, 7), INPUT, "b[31]"),  # B [bit 31]
            BP((42, 0, 7), INPUT, "b[22]"),  # B [bit 22]
            BP((43, 0, 7), INPUT, "b[21]"),  # B [bit 21]
            BP((44, 0, 7), INPUT, "b[20]"),  # B [bit 20]
            BP((45, 0, 7), INPUT, "b[19]"),  # B [bit 19]
            BP((46, 0, 7), INPUT, "b[18]"),  # B [bit 18]
            BP((47, 0, 7), INPUT, "b[17]"),  # B [bit 17]
            BP((48, 0, 7), INPUT, "b[16]"),  # B [bit 16]
            BP((49, 0, 7), INPUT, "b[15]"),  # B [bit 15]
            BP((50, 0, 7), INPUT, "b[14]"),  # B [bit 14]
            BP((51, 0, 7), INPUT, "b[13]"),  # B [bit 13]
            BP((34, 0, 7), INPUT, "b[30]"),  # B [bit 30]
            BP((52, 0, 7), INPUT, "b[12]"),  # B [bit 12]
            BP((53, 0, 7), INPUT, "b[11]"),  # B [bit 11]
            BP((54, 0, 7), INPUT, "b[10]"),  # B [bit 10]
            BP((55, 0, 7), INPUT, "b[9]"),  # B [bit 9]
            BP((56, 0, 7), INPUT, "b[8]"),  # B [bit 8]
            BP((57, 0, 7), INPUT, "b[7]"),  # B [bit 7]
            BP((58, 0, 7), INPUT, "b[6]"),  # B [bit 6]
            BP((59, 0, 7), INPUT, "b[5]"),  # B [bit 5]
            BP((60, 0, 7), INPUT, "b[4]"),  # B [bit 4]
            BP((61, 0, 7), INPUT, "b[3]"),  # B [bit 3]
            BP((35, 0, 7), INPUT, "b[29]"),  # B [bit 29]
            BP((62, 0, 7), INPUT, "b[2]"),  # B [bit 2]
            BP((63, 0, 7), INPUT, "b[1]"),  # B [bit 1]
            BP((64, 0, 7), INPUT, "b[0]"),  # B [bit 0]
            BP((36, 0, 7), INPUT, "b[28]"),  # B [bit 28]
            BP((37, 0, 7), INPUT, "b[27]"),  # B [bit 27]
            BP((38, 0, 7), INPUT, "b[26]"),  # B [bit 26]
            BP((39, 0, 7), INPUT, "b[25]"),  # B [bit 25]
            BP((40, 0, 7), INPUT, "b[24]"),  # B [bit 24]
            BP((41, 0, 7), INPUT, "b[23]"),  # B [bit 23]
            BP((-1, 0, -1), OUTPUT, "output[63]"),  # Output [bit 63]
            BP((8, 0, -1), OUTPUT, "output[54]"),  # Output [bit 54]
            BP((9, 0, -1), OUTPUT, "output[53]"),  # Output [bit 53]
            BP((10, 0, -1), OUTPUT, "output[52]"),  # Output [bit 52]
            BP((11, 0, -1), OUTPUT, "output[51]"),  # Output [bit 51]
            BP((12, 0, -1), OUTPUT, "output[50]"),  # Output [bit 50]
            BP((13, 0, -1), OUTPUT, "output[49]"),  # Output [bit 49]
            BP((14, 0, -1), OUTPUT, "output[48]"),  # Output [bit 48]
            BP((15, 0, -1), OUTPUT, "output[47]"),  # Output [bit 47]
            BP((16, 0, -1), OUTPUT, "output[46]"),  # Output [bit 46]
            BP((17, 0, -1), OUTPUT, "output[45]"),  # Output [bit 45]
            BP((0, 0, -1), OUTPUT, "output[62]"),  # Output [bit 62]
            BP((18, 0, -1), OUTPUT, "output[44]"),  # Output [bit 44]
            BP((19, 0, -1), OUTPUT, "output[43]"),  # Output [bit 43]
            BP((20, 0, -1), OUTPUT, "output[42]"),  # Output [bit 42]
            BP((21, 0, -1), OUTPUT, "output[41]"),  # Output [bit 41]
            BP((22, 0, -1), OUTPUT, "output[40]"),  # Output [bit 40]
            BP((23, 0, -1), OUTPUT, "output[39]"),  # Output [bit 39]
            BP((24, 0, -1), OUTPUT, "output[38]"),  # Output [bit 38]
            BP((25, 0, -1), OUTPUT, "output[37]"),  # Output [bit 37]
            BP((26, 0, -1), OUTPUT, "output[36]"),  # Output [bit 36]
            BP((27, 0, -1), OUTPUT, "output[35]"),  # Output [bit 35]
            BP((1, 0, -1), OUTPUT, "output[61]"),  # Output [bit 61]
            BP((28, 0, -1), OUTPUT, "output[34]"),  # Output [bit 34]
            BP((29, 0, -1), OUTPUT, "output[33]"),  # Output [bit 33]
            BP((30, 0, -1), OUTPUT, "output[32]"),  # Output [bit 32]
            BP((33, 0, -1), OUTPUT, "output[31]"),  # Output [bit 31]
            BP((34, 0, -1), OUTPUT, "output[30]"),  # Output [bit 30]
            BP((35, 0, -1), OUTPUT, "output[29]"),  # Output [bit 29]
            BP((36, 0, -1), OUTPUT, "output[28]"),  # Output [bit 28]
            BP((37, 0, -1), OUTPUT, "output[27]"),  # Output [bit 27]
            BP((38, 0, -1), OUTPUT, "output[26]"),  # Output [bit 26]
            BP((39, 0, -1), OUTPUT, "output[25]"),  # Output [bit 25]
            BP((2, 0, -1), OUTPUT, "output[60]"),  # Output [bit 60]
            BP((40, 0, -1), OUTPUT, "output[24]"),  # Output [bit 24]
            BP((41, 0, -1), OUTPUT, "output[23]"),  # Output [bit 23]
            BP((42, 0, -1), OUTPUT, "output[22]"),  # Output [bit 22]
            BP((43, 0, -1), OUTPUT, "output[21]"),  # Output [bit 21]
            BP((44, 0, -1), OUTPUT, "output[20]"),  # Output [bit 20]
            BP((45, 0, -1), OUTPUT, "output[19]"),  # Output [bit 19]
            BP((46, 0, -1), OUTPUT, "output[18]"),  # Output [bit 18]
            BP((47, 0, -1), OUTPUT, "output[17]"),  # Output [bit 17]
            BP((48, 0, -1), OUTPUT, "output[16]"),  # Output [bit 16]
            BP((49, 0, -1), OUTPUT, "output[15]"),  # Output [bit 15]
            BP((3, 0, -1), OUTPUT, "output[59]"),  # Output [bit 59]
            BP((50, 0, -1), OUTPUT, "output[14]"),  # Output [bit 14]
            BP((51, 0, -1), OUTPUT, "output[13]"),  # Output [bit 13]
            BP((52, 0, -1), OUTPUT, "output[12]"),  # Output [bit 12]
            BP((53, 0, -1), OUTPUT, "output[11]"),  # Output [bit 11]
            BP((54, 0, -1), OUTPUT, "output[10]"),  # Output [bit 10]
            BP((55, 0, -1), OUTPUT, "output[9]"),  # Output [bit 9]
            BP((56, 0, -1), OUTPUT, "output[8]"),  # Output [bit 8]
            BP((57, 0, -1), OUTPUT, "output[7]"),  # Output [bit 7]
            BP((58, 0, -1), OUTPUT, "output[6]"),  # Output [bit 6]
            BP((59, 0, -1), OUTPUT, "output[5]"),  # Output [bit 5]
            BP((4, 0, -1), OUTPUT, "output[58]"),  # Output [bit 58]
            BP((60, 0, -1), OUTPUT, "output[4]"),  # Output [bit 4]
            BP((61, 0, -1), OUTPUT, "output[3]"),  # Output [bit 3]
            BP((62, 0, -1), OUTPUT, "output[2]"),  # Output [bit 2]
            BP((63, 0, -1), OUTPUT, "output[1]"),  # Output [bit 1]
            BP((64, 0, -1), OUTPUT, "output[0]"),  # Output [bit 0]
            BP((5, 0, -1), OUTPUT, "output[57]"),  # Output [bit 57]
            BP((6, 0, -1), OUTPUT, "output[56]"),  # Output [bit 56]
            BP((7, 0, -1), OUTPUT, "output[55]"),  # Output [bit 55]
        ]
    ),
}

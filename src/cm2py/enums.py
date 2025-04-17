from enum import Enum


class BlockType(int, Enum):
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
    NODE = 15
    DELAY = 16
    ANTENNA = 17
    CONDUCTOR_V2 = 18
    LED_MIXER = 19


class Direction:
    NORTH = [0, 0, -1, 0, 1, 0, 1, 0, 0]
    EAST = [-1, 0, 0, 0, 1, 0, 0, 0, -1]
    SOUTH = [0, 0, 1, 0, 1, -0, -1, 0, 0]
    WEST = [1, 0, 0, 0, 1, 0, 0, 0, 1]


class BuildingType(str, Enum):
    ASCII_KEY_INPUT = "AsciiKeyInput"
    ASSEMBLER = "Assembler"
    DIVIDER = "Divider"
    DOOR = "Door"
    DUAL_MEMORY = "DualMemory"
    FUNCTION_GENERATOR = "FunctionGenerator"
    GRAPH = "Graph"
    HUGE_MEMORY = "HugeMemory"
    INTEGRATED_CIRCUIT = "IntegratedCircuit"
    KEY_INPUT = "KeyInput"
    LARGE_RGB_DISPLAY = "LargeRGBDisplay"
    MASS_MEMORY = "MassMemory"
    MASSIVE_MEMORY = "MassiveMemory"
    MULTIPLIER = "Multiplier"
    N_TRANSISTOR = "N-Transistor"
    P_TRANSISTOR = "P-Transistor"
    PIXEL_DISPLAY = "PixelDisplay"
    QWERTY_KEY_INPUT = "QwertyKeyInput"
    RGB_DISPLAY = "RGBDisplay"
    REAL_TIME_CLOCK = "RealTimeClock"
    SIGN = "Sign"
    TEXT_CONSOLE = "TextConsole"
    DIVIDER_32_BIT = "32BitDivider"
    MULTIPLIER_32_BIT = "32BitMultiplier"


class Directions(str, Enum):
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"

#!/usr/bin/env python3
"""
Additional utilities for working with cm2py.
"""

from ..cm2py import *
import zlib
import base64

def generateCLA(
    numBits: int,
    *,
    includeCarryIn: bool = True,
    includeOverflow: bool = True,
    generateIO: bool = True,
) -> str:
    """
    Generates a carry-lookahead adder based on the number of bits. Has options for including the overflow and carry in.
    """

    save = Save()

    inputA = []
    inputB = []

    inputAnds = []
    inputXors = []

    andGates = []
    if includeCarryIn:
        carryIn = save.addBlock(2, (-1, 0, -1))

    outputs = []

    for i in range(numBits):
        a = save.addBlock(3, (0, i, -1))
        b = save.addBlock(2, (1, i, -1))

        if generateIO:
            flipflop1 = save.addBlock(5, (0, i, -3))
            flipflop2 = save.addBlock(5, (1, i, -3))
            save.addConnection(flipflop1, a)
            save.addConnection(flipflop2, b)

        if i < numBits - 1 or includeOverflow:
            gand = save.addBlock(1, (0, i, 0))
            save.addConnection(a, gand)
            save.addConnection(b, gand)
            inputAnds.append(gand)

        gxor = save.addBlock(3, (1, i, 0))
        save.addConnection(a, gxor)
        save.addConnection(b, gxor)

        inputA.append(a)
        inputB.append(b)
        inputXors.append(gxor)

        outputs.append(save.addBlock(3, (1, i, -2)))

        save.addConnection(gxor, outputs[i])
        if i > 0:
            save.addConnection(inputAnds[i - 1], outputs[i])

    if includeOverflow:
        outputs.append(save.addBlock(2, (0, numBits, 1)))
        save.addConnection(inputAnds[numBits - 1], outputs[numBits])
    if includeCarryIn:
        save.addConnection(carryIn, outputs[0])

    currentPosition = (0, 0, 1)

    def addAndGate():
        nonlocal currentPosition
        gate = save.addBlock(1, currentPosition)
        andGates.append(gate)

        newY = currentPosition[1] + 1
        newX = currentPosition[0] + newY // numBits
        newZ = newX // 2 + currentPosition[2]
        currentPosition = (newX % 2, newY % numBits, newZ)

        return gate

    if includeCarryIn:
        for i in range(numBits if includeOverflow else numBits - 1):
            gate = addAndGate()
            save.addConnection(carryIn, gate)
            for j in range(i + 1):
                save.addConnection(inputXors[j], gate)
            save.addConnection(gate, outputs[i + 1])

    for bit in range(numBits):
        for i in range(bit + 1, numBits if includeOverflow else numBits - 1):
            gate = addAndGate()
            save.addConnection(inputAnds[bit], gate)

            for j in range(bit + 1, i + 1):
                save.addConnection(inputXors[j], gate)
            save.addConnection(gate, outputs[i + 1])

    output_zPos = currentPosition[2] + (
        not (
            (currentPosition[0] == 1 and currentPosition[1] == 0)
            or currentPosition[0] == 0
        )
    )

    for i in range(numBits):
        outputs[i].z = output_zPos

    if generateIO:
        for i in range(numBits):
            led = save.addBlock(6, (1, i, output_zPos + 2))
            save.addConnection(outputs[i], led)

    saveString = save.exportSave()
    return saveString


def generateDecoder(
    numBits: int,
    *,
    shape: Literal["square", "line"] = "line",
    inputShape: Literal["vertical", "horizontal"] = "vertical",
) -> str:
    """
    Generates a decoder based on the number of bits. Includes options for different shapes, like square and line.
    """

    save = Save()

    inputs = []
    inverseInputs = []

    for bit in range(numBits):
        node = save.addBlock(
            15, (0, bit, 0) if inputShape == "vertical" else (bit, 0, -2)
        )
        inputs.append(
            save.addBlock(2, (1, bit, 0) if inputShape == "vertical" else (bit, 0, -1))
        )
        inverseInputs.append(
            save.addBlock(0, (2, bit, 0) if inputShape == "vertical" else (bit, 0, 0))
        )

        save.addConnection(node, inputs[bit])
        save.addConnection(node, inverseInputs[bit])

    gatesPerRow = 2 ** math.ceil(numBits / 2)

    for i in range(2**numBits):
        pos = (
            ((0, i, 1) if inputShape == "vertical" else (i, 0, 1))
            if shape == "line"
            else (
                (i % gatesPerRow, i // gatesPerRow, 1)
                if inputShape == "vertical"
                else (i % gatesPerRow, 0, 1 + i // gatesPerRow)
            )
        )
        gate = save.addBlock(1, pos)

        for bit in range(numBits):
            if i & (1 << bit):
                save.addConnection(inputs[bit], gate)
            else:
                save.addConnection(inverseInputs[bit], gate)

    saveString = save.exportSave()
    return saveString


base64_strings = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"


def encodeToMemory(
    data: list[int], memoryType: Literal["mass", "massive", "huge"]
) -> str:
    """
    Turns a list of integers into a string that can be pasted into one of the memory buildings.
    """

    assert memoryType in [
        "mass",
        "massive",
        "huge",
    ], 'Invalid memory building type. Use "mass","massive",or "huge"'

    code = ""
    mass_memory_size = 4096
    massive_memory_size = 4096
    huge_memory_size = 65536
    
    if memoryType == "mass":
        if len(data) > mass_memory_size:
            raise ValueError(
            f"Data size ({len(data)}) exceeds available memory capacity of mass memory."
            )
        for v in data:
            code += format(v % 256, "02x")
        code += "00" * (4096 - len(data))
    elif memoryType == "massive":
        if len(data) > massive_memory_size:
            raise ValueError(
            f"Data size ({len(data)}) exceeds available memory capacity of massive memory."
            )
        for v in data:
            code += base64_strings[v & 0x3F]
            code += base64_strings[(v >> 6) & 0x3F]
            code += base64_strings[(v >> 12) & 0x3F]
        code += "AAA" * (4096 - len(data))
    elif memoryType == "huge":
            if len(data) > huge_memory_size:
                raise ValueError(
                f"Data size ({len(data)}) exceeds available memory capacity huge memory."
                )
            while huge_memory_size > len(data):
                data.append(0)
            temp = []
            for index in data:
                bit1 = index&0xff
                bit2 = index>>8
                temp.append(bit1)
                temp.append(bit2)
            data = temp 
            byte_data = bytes(data)
            compressed = zlib.compress(byte_data, level=2, wbits=-zlib.MAX_WBITS)
            compressed_b64 = base64.b64encode(compressed)
            code = compressed_b64.decode("utf-8")
            if code.endswith("=="):
                code = code[:-2]
            elif code.endswith("="):
                code = code[:-1]
    return code


def halfPrecisionBitsToNumber(bits: int) -> float:
    """
    Converts a half-precision floating point number stored in an integer to a python float.
    """
    packed_bytes = bits.to_bytes(2, byteorder="big")

    half_precision_float = struct.unpack(">e", packed_bytes)[0]

    return half_precision_float


def numberToHalfPrecisionBits(f: float) -> int:
    """
    Converts a python float to a half-precision floating point value stored in an integer. This integer then can be used with the encodeToMemory() function.
    """
    if f != f or f == float("inf") or f == float("-inf"):
        if f == float("inf"):
            return 0x7C00
        elif f == float("-inf"):
            return 0xFC00
        else:
            return 0x7E00

    bits = struct.unpack("H", struct.pack("e", f))[0]
    return bits


def generateFunctionLookUpTable(
    func: Callable[[float], float],
    size: int = 4096,
    *,
    valueType: Literal["int", "float"] = "int",
) -> str:
    """
    Generates a lookup table string that can be pasted into a Massive Memory for a math function.
    Takes in a value type parameter as well. If the value type is int, it leaves the results as they are, but if it's float, it converts the values into half-precision floating point.
    """
    values = []
    for num in range(size):
        values.append(func(num))

    if valueType == "float":
        for i in range(size):
            values[i] = numberToHalfPrecisionBits(values[i])

    return encodeToMemory(values, "massive")

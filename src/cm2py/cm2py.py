#!/usr/bin/env python3
""" Circuit Maker 2 save generation and manipulation package

This module contains utilities to generate and manipulate save strings
for the Roblox game Circuit Maker 2 by ismellbeef1.
"""

__author__ = "SKM GEEK"
__contact__ = "qestudios17@gmail.com"
__copyright__ = "Copyright 2024, SKM GEEK"
__date__ = "2024/04/14"
__deprecated__ = False
__email__ = "qestudios17@gmail.com"
__license__ = "MIT"
__maintainer__ = "SKM GEEK"
__status__ = "Production"
__version__ = "0.3.7"

from uuid import uuid4
import math
import regex as re
from typing import Literal, Callable
import string
import struct

class Block:
    __initialised = False

    def __init__(self, blockId, pos, state=False, properties=None):
        assert (
            isinstance(blockId, int) and 0 <= blockId <= 17
        ), "blockId must be an integer between 0 and 17"
        assert (
            isinstance(pos, tuple)
            and len(pos) == 3
            and (isinstance(pos[0], (float, int)))
            and (isinstance(pos[1], (float, int)))
            and (isinstance(pos[2], (float, int)))
        ), "pos must be a 3d tuple of integers or floats"
        assert isinstance(state, bool), "state must be a boolean"
        assert (
            isinstance(properties, list) or properties is None
        ), "properties must be a list of numbers, or None."
        self.blockId = blockId
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.z = self.pos[2]
        self.state = state
        self.properties = properties
        self.uuid = str(uuid4())

        self.__initialised = True

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        if not self.__initialised:
            return
        if name == "pos":
            self.__dict__["x"] = self.pos[0]
            self.__dict__["y"] = self.pos[1]
            self.__dict__["z"] = self.pos[2]
        elif name in ["x", "y", "z"]:
            self.__dict__["pos"] = (self.x, self.y, self.z)


class Connection:
    def __init__(self, source, target):
        assert isinstance(source, Block), "source must be a Block object"
        assert isinstance(target, Block), "target must be a Block object"
        self.source = source
        self.target = target

class Save:
    """A class to represent a save, which can be modified."""

    def __init__(self):
        self.blocks = {}
        self.connections = {}
        self.blockCount = 0
        self.connectionCount = 0

    def addBlock(self, blockId: int, pos: tuple[float,float,float], state:bool = False, properties:bool = None, snapToGrid:bool = True) -> Block:
        """Add a block to the save."""
        if snapToGrid:
            newBlock = Block(
                blockId,
                tuple([int(math.floor(i)) for i in pos]),
                state=state,
                properties=properties,
            )
        else:
            newBlock = Block(blockId, pos, state=state, properties=properties)
        self.blocks[newBlock.uuid] = newBlock
        self.blockCount += 1
        return newBlock

    def addConnection(self, source: Block, target: Block) -> Connection:
        """Add a connection to the save."""
        newConnection = Connection(source, target)
        if newConnection.target.uuid in self.connections:
            self.connections[newConnection.target.uuid].append(newConnection)
        else:
            self.connections[newConnection.target.uuid] = [newConnection]
        self.connectionCount += 1
        return newConnection

    def exportSave(self) -> str:
        """Export the save to a Circuit Maker 2 save string."""
        string = ""
        blockIndexes = {}
        index = 0

        assert self.blockCount > 0, "Saves with less than 1 block cannot be exported."

        for b in self.blocks.values():
            p = "+".join(str(v) for v in b.properties) if b.properties else ""
            string += f"{b.blockId},{int(b.state)},{b.x},{b.y},{b.z},{p};"
            blockIndexes[b.uuid] = index
            index += 1

        string = string[:-1] + "?"
        for c in self.connections.values():
            for n in c:
                string += (
                    f"{blockIndexes[n.source.uuid]+1},{blockIndexes[n.target.uuid]+1};"
                )
        if self.connectionCount > 0:
            string = string[:-1]
        string = string + "??"  # TODO: Custom build support & sign data support
        return string

    def deleteBlock(self, blockRef: Block) -> None:
        """Delete a block from the save."""
        assert isinstance(blockRef, Block), "blockRef must be a Block object"
        assert blockRef.uuid in self.blocks, "block does not exist in save"
        for c in self.connections.values():
            for n in c:
                if n.source.uuid == blockRef.uuid or n.target.uuid == blockRef.uuid:
                    del self.connections[n.target.uuid][
                        self.connections[n.target.uuid].index(n)
                    ]
                    break
        del self.blocks[blockRef.uuid]
        self.blockCount -= 1
        return

    def deleteConnection(self, connectionRef: Connection) -> None:
        """Delete a connection from the save."""
        assert isinstance(
            connectionRef, Connection
        ), "connectionRef must be a Connection object"
        assert connectionRef in (n for c in self.connections.values() for n in c)
        for c in self.connections.values():
            for n in c:
                if connectionRef == n:
                    del self.connections[n.target.uuid][
                        self.connections[n.target.uuid].index(n)
                    ]
        self.connectionCount -= 1





def validateSave(string: str) -> re.Match | None:
    """Check whether a string is a valid savestring or not."""
    # fmt: off
    regex = (
        r"(?<![\d\w,;?+])" # Blocks
        r"(?>"
          r"(?<b>"
            r"\d+,"
            r"[01]?"
            r"(?>,(?<d>-?\d*\.?\d*)){3}"
            r"(?>(\+|,)(?&d)(?!,))*"
            r";?"
          r")+"
        r"(?<!;)\?"
        r")"

        r"(?>" # Connections
          r"(?<i>[1-9][0-9]*),"
          r"(?&i)"
          r";?"
        r")*"
        r"(?<!;)\?"

        r"(?>" # Buildings
          r"[A-Za-z]+,"
          r"(?>(?&d),){3}"
          r"(?>(?&d),){9}"
          r"(?>[01](?&i),?)*"
          r"(?<!,)"
          r";?"
        r")*"
        r"(?<!;)\?"

        r"(" # Sign data
          r"([0-9a-fA-F]{2})"
        r")*"
        r"(?![\d\w,;?+])$"
    )
    # fmt: on
    return re.match(regex, string)


def importSave(string: str, snapToGrid: bool = True) -> Save:
    """Import a Circuit Maker 2 save string as a save."""
    assert validateSave(string), "invalid save string"

    newSave = Save()

    sections = string.split("?")
    blockString = sections[0].split(";")
    connectionString = sections[1].split(";")

    blockVals = [
        [
            (
                None
                if not v
                else (
                    [float(a) for a in v.split("+")]
                    if "+" in v or p == 5
                    else float(v) if (v and p != 0) else int(v)
                )
            )
            for p, v in enumerate(i.split(","))
        ]
        for i in blockString
    ]
    connections = [[int(v) for v in i.split(",")] for i in connectionString if i]

    blocks = []
    for b in blockVals:
        blocks.append(
            newSave.addBlock(
                b[0],
                (b[2], b[3], b[4]),
                state=bool(b[1]),
                properties=b[5],
                snapToGrid=snapToGrid,
            )
        )

    for c in connections:
        newSave.addConnection(blocks[c[0] - 1], blocks[c[1] - 1])

    return newSave


def generateCLA(numBits:int,*, includeCarryIn:bool = True, includeOverflow:bool = True, generateIO:bool = True) -> str:
    """Generates a carry-lookahead adder based on the number of bits. Has options for including the overflow and carry in."""
    
    save = Save()

    inputA = []
    inputB = []

    inputAnds = []
    inputXors = []

    andGates = []
    if includeCarryIn:
        carryIn = save.addBlock(2,(-1,0,-1))

    outputs = []

    for i in range(numBits):
        a = save.addBlock(3,(0,i,-1))
        b = save.addBlock(2,(1,i,-1))

        if generateIO:
            flipflop1 = save.addBlock(5,(0,i,-3))
            flipflop2 = save.addBlock(5,(1,i,-3))
            save.addConnection(flipflop1,a)
            save.addConnection(flipflop2,b)

        if i < numBits-1 or includeOverflow:
            gand = save.addBlock(1,(0,i,0))
            save.addConnection(a, gand)
            save.addConnection(b, gand)
            inputAnds.append(gand)
        
        gxor = save.addBlock(3,(1,i,0))
        save.addConnection(a, gxor)
        save.addConnection(b, gxor)

        inputA.append(a)
        inputB.append(b)
        inputXors.append(gxor)

        outputs.append(save.addBlock(3,(1,i,-2)))

        save.addConnection(gxor,outputs[i])
        if i > 0:
            save.addConnection(inputAnds[i-1],outputs[i])

    if includeOverflow:
        outputs.append(save.addBlock(2,(0,numBits,1)))
        save.addConnection(inputAnds[numBits-1], outputs[numBits])
    if includeCarryIn:
        save.addConnection(carryIn,outputs[0])

    currentPosition = (0,0,1)

    def addAndGate():
        nonlocal currentPosition
        gate = save.addBlock(1,currentPosition)
        andGates.append(gate)

        newY = currentPosition[1] + 1
        newX = currentPosition[0] + newY//numBits
        newZ = newX//2 + currentPosition[2]
        currentPosition = (newX%2, newY%numBits, newZ)

        return gate


    if includeCarryIn:
        for i in range(numBits if includeOverflow else numBits-1):
            gate = addAndGate()
            save.addConnection(carryIn,gate)
            for j in range(i+1):
                save.addConnection(inputXors[j],gate)
            save.addConnection(gate,outputs[i+1])

    for bit in range(numBits):
        for i in range(bit+1, numBits if includeOverflow else numBits-1):
            gate = addAndGate()
            save.addConnection(inputAnds[bit],gate)

            for j in range(bit+1,i+1):
                save.addConnection(inputXors[j],gate)
            save.addConnection(gate,outputs[i+1])


    output_zPos = currentPosition[2] + (not((currentPosition[0] == 1 and currentPosition[1] == 0) or currentPosition[0] == 0))

    for i in range(numBits):
        outputs[i].z = output_zPos

    if generateIO:
        for i in range(numBits):
            led = save.addBlock(6, (1,i,output_zPos+2))
            save.addConnection(outputs[i],led)

    saveString = save.exportSave()
    return saveString
def generateDecoder(numBits: int, *, shape: Literal["square","line"] = "line", inputShape: Literal["vertical","horizontal"] = "vertical") -> str:
    """Generates a decoder based on the number of bits. Includes options for different shapes, like square and line."""
    
    save = Save()

    inputs = []
    inverseInputs = []

    for bit in range(numBits):
        node = save.addBlock(15,(0,bit,0) if inputShape == "vertical" else (bit,0,-2))
        inputs.append(save.addBlock(2,(1,bit,0) if inputShape == "vertical" else (bit,0,-1)))
        inverseInputs.append(save.addBlock(0,(2,bit,0) if inputShape == "vertical" else (bit,0,0)))

        save.addConnection(node, inputs[bit])
        save.addConnection(node, inverseInputs[bit])
    
    gatesPerRow = 2**math.ceil(numBits/2)

    for i in range(2**numBits):
        pos = ((0,i,1) if inputShape == "vertical" else (i,0,1)) if shape == "line" else ((i%gatesPerRow,i//gatesPerRow,1) if inputShape == "vertical" else (i%gatesPerRow,0,1+i//gatesPerRow))
        gate = save.addBlock(1,pos)

        for bit in range(numBits):
            if i & (1<<bit):
                save.addConnection(inputs[bit],gate)
            else:
                save.addConnection(inverseInputs[bit],gate)
    
    saveString = save.exportSave()
    return saveString


base64 = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"

def encodeToMemory(data: list[int], memoryType: Literal["mass","massive","huge"]) -> str:
    """Turns a list of integers into a string that can be pasted into one of the memory buildings."""

    assert memoryType in ["mass","massive","huge"], "Invalid memory building type. Use \"mass\",\"massive\",or \"huge\""

    code = ""

    if memoryType == "mass":
        for v in data:
            code += format(v%256, '02x')
        code += "00" * (4096-len(data))
    elif memoryType == "massive":
        for v in data:
            code += base64[v & 0x3f]
            code += base64[(v>>6) & 0x3f]
            code += base64[(v>>12) & 0x3f]
        code += "AAA" * (4096-len(data))
    elif memoryType == "huge":
        raise (NotImplementedError, "Huge Memory uses full utf8 to represent the values, which don't work well with Roblox yet. When the format gets updated or full utf8 is supported, this function will be updated.")
    return code

def halfPrecisionBitsToNumber(bits: int) -> float:
    """Converts a half-precision floating point number stored in an integer to a python float."""
    packed_bytes = bits.to_bytes(2, byteorder='big')
    
    half_precision_float = struct.unpack('>e', packed_bytes)[0]
    
    return half_precision_float


def numberToHalfPrecisionBits(f: float) -> int:
    """Converts a python float to a half-precision floating point value stored in an integer. This integer then can be used with the encodeToMemory() function."""
    if f != f or f == float('inf') or f == float('-inf'):
        if f == float('inf'):
            return 0x7C00
        elif f == float('-inf'):
            return 0xFC00
        else:
            return 0x7E00
    
    bits = struct.unpack('H', struct.pack('e', f))[0]
    return bits


def generateFunctionLookUpTable(func: Callable[[float], float], size: int = 4096,* , valueType: Literal["int","float"] = "int") -> str:
    """Generates a lookup table string that can be pasted into a Massive Memory for a math function.
    Takes in a value type parameter as well. If the value type is int, it leaves the results as they are, but if it's float, it converts the values into half-precision floating point."""
    values = []
    for num in range(size):
        values.append(func(num))

    if valueType == "float":
        for i in range(size):
            values[i] = numberToHalfPrecisionBits(values[i])
    
    return encodeToMemory(values, "massive")


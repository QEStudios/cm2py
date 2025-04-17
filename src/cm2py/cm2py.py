#!/usr/bin/env python3
"""Circuit Maker 2 save generation and manipulation package

This module contains utilities to generate and manipulate save strings
for the Roblox game Circuit Maker 2 by ismellbeef1.
"""

__author__ = "SKM GEEK"
__contact__ = "qestudios17@gmail.com"
__copyright__ = "Copyright 2025, SKM GEEK"
__date__ = "2025/04/15"
__deprecated__ = False
__email__ = "qestudios17@gmail.com"
__license__ = "MIT"
__maintainer__ = "SKM GEEK"
__status__ = "Production"
__version__ = "0.4.0.dev0"

from uuid import uuid4
import math
import regex as re
from . import enums
from typing import Literal, Callable
import string
import struct


class Block:
    __initialised = False

    def __init__(self, blockId, pos, state=False, properties=None):
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
        self.blockId = self._normalise_block_type(blockId)
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

    @staticmethod
    def _normalise_block_type(value):
        if isinstance(value, enums.BlockType):
            return value
        try:
            return enums.BlockType(value)
        except ValueError:
            raise AssertionError(f"Invalid block id: {value}")


class Connection:
    def __init__(self, source, target):
        assert isinstance(source, Block), "source must be a Block object"
        assert isinstance(target, Block), "target must be a Block object"
        self.source = source
        self.target = target


class Building:
    def __init__(self, pos, rotation):
        assert (
            isinstance(pos, (list, tuple))
            and len(pos) == 3
            and all(isinstance(coord, (int, float)) for coord in pos)
        ), "pos must be a 3D tuple of integers or floats"

        assert (
            isinstance(rotation, (list, tuple))
            and len(rotation) == 9
            and all(isinstance(v, (int, float)) for v in rotation)
        ), "rotation must be a list of 9 numbers"

        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.z = self.pos[2]
        self.rotation = rotation
        self.blocks = {}


class Save:
    """A class to represent a save, which can be modified."""

    def __init__(self):
        self.blocks = {}
        self.connections = {}
        self.blockCount = 0
        self.connectionCount = 0

    def addBlock(
        self,
        blockId: int,
        pos: tuple[float | int, float | int, float | int],
        state: bool = False,
        properties: list[int | float] | None = None,
        snapToGrid: bool = True,
    ) -> Block:
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


def importSave(string: str, snapToGrid: bool = True, validate: bool = True) -> Save:
    """Import a Circuit Maker 2 save string as a save."""
    if validate == True:
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
                (b[2] or 0, b[3] or 0, b[4] or 0),
                state=bool(b[1]),
                properties=b[5],
                snapToGrid=snapToGrid,
            )
        )

    for c in connections:
        newSave.addConnection(blocks[c[0] - 1], blocks[c[1] - 1])

    return newSave

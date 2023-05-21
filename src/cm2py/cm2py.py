#!/usr/bin/env python3
""" Circuit Maker 2 save generation and manipulation package

This module contains utilities to generate and manipulate save strings
for the Roblox game Circuit Maker 2 by ismellbeef1.
"""

__author__ = "SKM GEEK"
__contact__ = "qestudios17@gmail.com"
__copyright__ = "Copyright 2023, SKM GEEK"
__date__ = "2023/04/29"
__deprecated__ = False
__email__ = "qestudios17@example.com"
__license__ = "MIT"
__maintainer__ = "SKM GEEK"
__status__ = "Production"
__version__ = "0.0.3"

import re
from uuid import UUID, uuid4
import numpy as np


class Save:
    """A class to represent a save, which can be modified."""

    def __init__(self):
        self.blocks = []
        self.connections = {}

    def addBlock(self, blockId, pos, state=False, snapToGrid=True):
        """Add a block to the save."""
        if snapToGrid:
            newBlock = Block(blockId, tuple(np.floor(pos)), state)
        else:
            newBlock = Block(blockId, pos, state)
        self.blocks.append(newBlock)
        return newBlock

    def addConnection(self, source, target):
        """Add a connection to the save."""
        newConnection = Connection(source, target)
        if str(newConnection.target.uuid) in self.connections:
            self.connections[str(newConnection.target.uuid)].append(newConnection)
        else:
            self.connections[str(newConnection.target.uuid)] = [newConnection]
        return newConnection

    def exportSave(self):
        """Export the save to a Circuit Maker 2 save string."""
        blockStrings = []
        for b in self.blocks:
            blockStrings.append(f"{b.blockId},{int(b.state)},{b.x},{b.y},{b.z},")
        saveString = ";".join(blockStrings) + "?"
        connectionStrings = []
        for c in self.connections.values():
            for n in c:
                connectionStrings.append(
                    (
                        f"{[str(b.uuid) for b in self.blocks].index(str(n.source.uuid))+1},"
                        f"{[str(b.uuid) for b in self.blocks].index(str(n.target.uuid))+1}"
                    )
                )
        saveString += ";".join(connectionStrings) + "?"
        return saveString

    def deleteBlock(self, blockRef):
        """Delete a block from the save."""
        assert isinstance(blockRef, Block), "blockRef must be a block object"
        return


class Block:
    def __init__(self, blockId, pos, state=False):
        assert isinstance(blockId, int) and 0 <= blockId <= 11, "blockId must be an integer between 0 and 11"
        assert (
            isinstance(pos, tuple)
            and len(pos) == 3
            and (isinstance(pos[0], float) or isinstance(pos[0], int))
            and (isinstance(pos[1], float) or isinstance(pos[1], int))
            and (isinstance(pos[2], float) or isinstance(pos[2], int))
        ), "pos must be a 3d tuple of integers"
        assert isinstance(state, bool), "state must be a boolean"
        self.blockId = blockId
        self.pos = tuple(np.round(pos))
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.z = self.pos[2]
        self.state = state
        self.uuid = uuid4()


class Connection:
    def __init__(self, source, target):
        assert isinstance(source, Block), "source must be a block object"
        assert isinstance(target, Block), "target must be a block object"
        self.source = source
        self.target = target


def importSave(string, snapToGrid=True):
    """Import a Circuit Maker 2 save string as a save."""
    regex = (
        # Match all blocks
        r"^((\d+,){2}(-?\d+,){3}(((\d+)|(\d+\+){2}(\d+)))?;)+"
        r"((\d+,){2}(-?\d+,){3}(((\d+)|(\d+\+){2}(\d+))?)\?)"
        # Match all connections
        r"((([1-9][0-9]*),([1-9][0-9]*)|((([1-9][0-9]*),([1-9][0-9]*);)+"
        r"([1-9][0-9]*),([1-9][0-9]*)))?\?)"
        # Match custom build syntax
        r"((\w+(,(-?\d+(\+-?\d+)*)*)+)(;(\w+(,(-?\d+(\+-?\d+)*)*)+))*)*$"
    )

    assert re.match(regex, string), "Invalid save string"

    newSave = Save()

    blocks = [[int(v) if v else None for v in i.split(",")] for i in "".join(string.split("?")[0]).split(";")]
    connections = [
        [int(v) for v in i.split(",")]
        for i in "".join(string.split("?")[1]).split(";")
        if len("".join(string.split("?")[1]).split(";")) > 1
        and isinstance("".join(string.split("?")[1]).split(";")[0], int)
        and isinstance("".join(string.split("?")[1]).split(";")[0], int)
    ]
    # Need to refactor this line

    for b in blocks:
        newSave.addBlock(b[0], (b[2], b[3], b[4]), state=bool(b[1]), snapToGrid=snapToGrid)

    for c in connections:
        newSave.addConnection(blocks[c[0] - 1], blocks[c[1] - 1])

    return newSave

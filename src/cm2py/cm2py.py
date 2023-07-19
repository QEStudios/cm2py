#!/usr/bin/env python3
""" Circuit Maker 2 save generation and manipulation package

This module contains utilities to generate and manipulate save strings
for the Roblox game Circuit Maker 2 by ismellbeef1.
"""

__author__ = "SKM GEEK"
__contact__ = "qestudios17@gmail.com"
__copyright__ = "Copyright 2023, SKM GEEK"
__date__ = "2023/05/21"
__deprecated__ = False
__email__ = "qestudios17@example.com"
__license__ = "MIT"
__maintainer__ = "SKM GEEK"
__status__ = "Production"
__version__ = "0.2.6"

import re
from uuid import UUID, uuid4
import math


class Save:
    """A class to represent a save, which can be modified."""

    def __init__(self):
        self.blocks = []
        self.connections = {}

    def addBlock(self, blockId, pos, state=False, properties=None, snapToGrid=True):
        """Add a block to the save."""
        if snapToGrid:
            newBlock = Block(blockId, tuple([int(math.floor(i)) for i in pos]), state=state, properties=properties)
        else:
            newBlock = Block(blockId, pos, state=state, properties=properties)
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
        string = ""
        for b in self.blocks:
            if b.properties:
                p = "+".join(str(v) for v in b.properties)
                string += f"{b.blockId},{int(b.state)},{b.x},{b.y},{b.z},{p};"
            else:
                string += f"{b.blockId},{int(b.state)},{b.x},{b.y},{b.z},;"

        string = string[:-1] + "?"
        blockUuids = [str(b.uuid) for b in self.blocks]
        for c in self.connections.values():
            for n in c:
                string += f"{blockUuids.index(str(n.source.uuid))+1},{blockUuids.index(str(n.target.uuid))+1};"
        string = string[:-1] + "??"  # TODO: Custom build support & sign data support
        return string

    def deleteBlock(self, blockRef):
        """Delete a block from the save."""
        assert isinstance(blockRef, Block), "blockRef must be a Block object"
        assert blockRef in self.blocks, "block does not exist in save"
        for c in self.connections.values():
            for n in c:
                if n.source.uuid == blockRef.uuid or n.target.uuid == blockRef.uuid:
                    del self.connections[str(n.target.uuid)][self.connections[str(n.target.uuid)].index(n)]
                    break
        del self.blocks[self.blocks.index(blockRef)]
        return

    def deleteConnection(self, connectionRef):
        """Delete a connection from the save."""
        assert isinstance(connectionRef, Connection), "connectionRef must be a Connection object"
        assert connectionRef in (n for c in self.connections.values() for n in c)
        for c in self.connections.values():
            for n in c:
                if connectionRef == n:
                    del self.connections[str(n.target.uuid)][self.connections[str(n.target.uuid)].index(n)]


class Block:
    def __init__(self, blockId, pos, state=False, properties=None):
        assert isinstance(blockId, int) and 0 <= blockId <= 11, "blockId must be an integer between 0 and 11"
        assert (
            isinstance(pos, tuple)
            and len(pos) == 3
            and (isinstance(pos[0], float) or isinstance(pos[0], int))
            and (isinstance(pos[1], float) or isinstance(pos[1], int))
            and (isinstance(pos[2], float) or isinstance(pos[2], int))
        ), "pos must be a 3d tuple of integers"
        assert isinstance(state, bool), "state must be a boolean"
        assert isinstance(properties, list) or properties == None, "properties must be a list of numbers, or None"
        self.blockId = blockId
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.z = self.pos[2]
        self.state = state
        self.properties = properties
        self.uuid = uuid4()


class Connection:
    def __init__(self, source, target):
        assert isinstance(source, Block), "source must be a Block object"
        assert isinstance(target, Block), "target must be a Block object"
        self.source = source
        self.target = target


def importSave(string, snapToGrid=True):
    """Import a Circuit Maker 2 save string as a save."""
    regex = (
        # Match all blocks
        r"^((\d+,){2}(-?\d+(\.\d+)?,){3}(((\d+(\.\d+)?\+)*(\d+(\.\d+)?)))?;)+"
        r"((\d+,){2}(-?\d+(\.\d+)?,){3}(((\d+(\.\d+)?\+)*(\d+(\.\d+)?)))?\?)"
        # Match all connections
        r"((([1-9][0-9]*),([1-9][0-9]*)|((([1-9][0-9]*),([1-9][0-9]*);)+"
        r"([1-9][0-9]*),([1-9][0-9]*)))?\?)"
        # Match custom build syntax
        r"((\w+(,(-?\d+(\.\d+)?(\+-?\d+(\.\d+)?)*)*)+)(;(\w+(,(-?\d+(\.\d+)?(\+-?\d+(\.\d+)?)*)*)+))*)*\?"
        # Match sign data
        r"[0-9a-f]*(;[0-9a-fA-F]*)*$"
    )

    assert re.match(regex, string), "invalid save string"

    newSave = Save()

    blocks = [
        [
            [float(a) for a in v.split("+")] if "+" in v else float(v) if (v and p != 0) else int(v) if p == 0 else None
            for p, v in enumerate(i.split(","))
        ]
        for i in "".join(string.split("?")[0]).split(";")
    ]
    connections = [
        [int(v) for v in i.split(",")]
        for i in "".join(string.split("?")[1]).split(";")
        if len("".join(string.split("?")[1]).split(";")) > 1
        and isinstance("".join(string.split("?")[1]).split(";")[0], int)
        and isinstance("".join(string.split("?")[1]).split(";")[0], int)
    ]
    # Need to refactor these lines

    for b in blocks:
        newSave.addBlock(b[0], (b[2], b[3], b[4]), state=bool(b[1]), properties=b[5], snapToGrid=snapToGrid)

    for c in connections:
        newSave.addConnection(blocks[c[0] - 1], blocks[c[1] - 1])

    return newSave

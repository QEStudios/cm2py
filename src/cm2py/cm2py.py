#!/usr/bin/env python
""" Circuit Maker 2 save generation and manipulation package

This module contains utilities to generate and manipulate save strings
for the Roblox game Circuit Maker 2 by ismellbeef1.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "SKM GEEK"
__contact__ = "qestudios17@gmail.com"
__copyright__ = "Copyright 2023, SKM GEEK"
__date__ = "2023/04/29"
__deprecated__ = False
__email__ =  "qestudios17@example.com"
__license__ = "GPLv3"
__maintainer__ = "SKM GEEK"
__status__ = "Production"
__version__ = "0.0.2"


from uuid import UUID, uuid4

class save:
    
    def __init__(self):
        self.blocks = []
        self.connections = {}

    def addBlock(self, blockId, pos, state=False, snapToGrid=True):
        """Add a block to the save."""
        if snapToGrid:
            newBlock = Block(blockId, tuple(map(lambda x: round(x), pos)), state)
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
                connectionStrings.append(f"{[str(b.uuid) for b in self.blocks].index(str(n.source.uuid))+1},{[str(b.uuid) for b in self.blocks].index(str(n.target.uuid))+1}")
        saveString += ";".join(connectionStrings)
        return saveString

class block:

    def __init__(self, blockId, pos, state=False):
        assert isinstance(blockId, int) and 0 <= blockId <= 11, "blockId must be an integer between 0 and 11"
        assert isinstance(pos, tuple) and len(pos) == 3 and (isinstance(pos[0], float) or isinstance(pos[0], int)) and (isinstance(pos[1], float) or isinstance(pos[1], int)) and (isinstance(pos[2], float) or isinstance(pos[2], int)), "pos must be a 3d tuple of integers"
        assert isinstance(state, bool), "state must be a boolean"
        self.blockId = blockId
        self.pos = tuple([round(pos[i],2) for i in range(3)])
        self.x = round(pos[0],2)
        self.y = round(pos[1],2)
        self.z = round(pos[2],2)
        self.state = state
        self.uuid = uuid4()

class connection:

    def __init__(self, source, target):
        assert isinstance(source, Block) or isinstance(source, UUID), "source must be a Block object, or a UUID"
        assert isinstance(target, Block) or isinstance(source, UUID), "target must be a Block object, or a UUID"
        self.source = source
        self.target = target

def importSave(string):
    """Import a Circuit Maker 2 save string as a save."""
    regex = r'^((\d+,){2}(-?\d+,){3}(|((\d+)|(\d+\+){2}(\d+)));)+((\d+,){2}(-?\d+,){3}(|((\d+)|(\d+\+){2}(\d+)))\?)(|(([1-9][0-9]*),([1-9][0-9]*)|((([1-9][0-9]*),([1-9][0-9]*);)+([1-9][0-9]*),([1-9][0-9]*))))$'
    if not re.match(regex, string):
        raise ValueError("Invalid save string")

    # TODO

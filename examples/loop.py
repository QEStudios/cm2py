#!/usr/bin/env python3
# This code generates a line of blocks connected in a loop, with specified length.

import cm2py as cm2

LENGTH = 8

save = cm2.Save()

blocks = []

for i in range(LENGTH):
    blocks.append(save.addBlock(cm2.OR, (i, 0, 0)))

### Commented out for clarity.
### You should store connections in a list if you want to modify them later.
# connections = []

for i in range(LENGTH):
    # connections.append(save.addConnection(blocks[i-1], blocks[i]))
    save.addConnection(blocks[i - 1], blocks[i])  # Directly add the connections to the save object

saveString = save.exportSave()
print(saveString)

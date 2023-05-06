import cm2py as cm2

save = cm2.save()

blocks = []

for i in range(8):
    blocks.append(save.addBlock(cm2.OR, (i, 0, 0)))

### Commented out for clarity. 
### You should store connections in a list if you want to modify them later.
# connections = []  

for i in range(8):
    # connections.append(save.addConnection(blocks[i-1], blocks[i]))
    save.addConnection(blocks[i-1], blocks[i])  # Directly add the connections to the save object

save.exportSave()

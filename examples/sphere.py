#!/usr/bin/env python3
# This code generates a sphere with a specified radius, resolution, and block type.

import cm2py as cm2
import math

radius = 10  # Radius of the sphere
resolution = 20  # Number of divisions of the cube to generate
block = cm2.OR  # Block ID to be used

save = cm2.Save()

for r in range(resolution // 2):
    for i in range(resolution):
        x = int(
            (math.sin(i / (resolution / (math.pi * 2))))
            * radius
            * math.cos(r / (resolution / (math.pi * 2)))
        )
        y = int((math.cos(i / (resolution / (math.pi * 2))) + 1) * radius)
        z = int(
            (math.sin(r / (resolution / (math.pi * 2))))
            * radius
            * math.sin(i / (resolution / (math.pi * 2)))
        )
        save.addBlock(block, (x, y, z))

saveString = save.exportSave()
print(saveString)

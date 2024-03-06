#!/usr/bin/env python3
# This code generates a sphere with a specified radius, resolution, and block type.
# The blocks are not snapped to the grid, creating a smoother sphere.

import cm2py as cm2
import math

radius = 5  # Radius of the sphere
resolution = 50  # Number of divisions of the cube to generate
block = cm2.OR  # Block ID to be used

save = cm2.Save()

for r in range(resolution // 2):
    for i in range(resolution):
        x = round(
            (math.sin(i / (resolution / (math.pi * 2))))
            * radius
            * math.cos(r / (resolution / (math.pi * 2))),
            3,
        )
        y = round((math.cos(i / (resolution / (math.pi * 2))) + 1) * radius, 3)
        z = round(
            (math.sin(r / (resolution / (math.pi * 2))))
            * radius
            * math.sin(i / (resolution / (math.pi * 2))),
            3,
        )
        save.addBlock(block, (x, y, z), snapToGrid=False)

saveString = save.exportSave()
print(saveString)

# Getting Started

## Installing

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cm2py from [PyPi](https://pypi.org/project/cm2py/).

```sh
python3 -m pip install cm2py
```

## Importing cm2py into your code

The most common way to import cm2py is to alias it to `cm2`. This neatens code without polluting the global namespace:

```py
import cm2py as cm2
```

For the sake of consistency, all code snippets in this documentation will assume cm2py is imported in this fashion.

## Working with Save objects and savestrings

In cm2py, everything in a savestring is stored in a `Save` object. This object contains all the blocks and connections
in the savestring.

There are two main ways of creating a Save object: Starting from a new empty save, or importing a savestring
to modify.

### Creating a new empty Save object

An empty Save object can be created with the following syntax:

```py
import cm2py as cm2

save = cm2.Save()
```

### Importing a savestring

A savestring can be loaded from a string using the following syntax:

```py
import cm2py as cm2

savestring_to_import = "..."
save = cm2.importSave(savestring_to_import)
```

The `save` variable can then be modified like any other Save object.

### Exporting a Save object as a savestring

To use a save in the game itself, you need to export the Save object as a savestring.  
You can do this using the `exportSave` method of the Save object:

```py
# ...
# save variable contains the Save object

exported_savestring = save.exportSave()
```

## Blocks

### Defining a block type

To specify a block type in cm2py, you can use the built-in mapping that cm2py provides:

| Block ID | Block Type   | cm2py Mapping      |
|----------|--------------|--------------------|
| 0        | NOR          | `cm2.NOR`          |
| 1        | AND          | `cm2.AND`          |
| 2        | OR           | `cm2.OR`           |
| 3        | XOR          | `cm2.XOR`          |
| 4        | Button       | `cm2.BUTTON`       |
| 5        | Flip-Flop    | `cm2.FLIPFLOP`     |
| 6        | LED          | `cm2.LED`          |
| 7        | Sound        | `cm2.SOUND`        |
| 8        | Conductor    | `cm2.CONDUCTOR`    |
| 9        | Custom       | `cm2.CUSTOM`       |
| 10       | NAND         | `cm2.NAND`         |
| 11       | XNOR         | `cm2.XNOR`         |
| 12       | Random       | `cm2.RANDOM`       |
| 13       | Text         | `cm2.TEXT`         |
| 14       | Tile         | `cm2.TILE`         |
| 15       | Node         | `cm2.NODE`         |
| 16       | Delay        | `cm2.DELAY`        |
| 17       | Antenna      | `cm2.ANTENNA`      |
| 18       | Conductor V2 | `cm2.CONDUCTOR_V2` |
| 19       | LED Mixer    | `cm2.LED_MIXER`    |

### Adding blocks to a Save object

Each block in a save is stored as a Block object. To add blocks to a Save object, the `addBlock` method is used:

```py
import cm2py as cm2

save = cm2.Save()

# Add a NOR block at position (0,0,0).
# The reference to the Block object is stored into the block variable.
block = save.addBlock(cm2.NOR, (0, 0, 0))
```

When adding a block to a save, you must specify the block type and position.
You can also optionally provide the block state, properties, and whether to allow the block to be placed off-grid:

```py
import cm2py as cm2

save = cm2.Save()

# Add an LED at position (1, 2, 3.5).
# The block state is set to True (activated).
# The properties are set to [255, 0, 255]. This makes the LED purple.
# Grid snapping is disabled to allow the block to be off-grid.
block = save.addBlock(
    cm2.LED,
    (1, 2, 3.5),
    state = True,
    properties = [255, 0, 255],
    snapToGrid = False
    )
```

### Deleting blocks from a Save object

To delete a block from a save, you can call the `deleteBlock` method of the Save object:

```py
# ...
# save variable contains the Save object containing the block
# block variable contains the Block object to delete

save.deleteBlock(block)
```

This will invalidate any futher references to that specific Block object.

### Moving blocks to different locations

To change a block's position, you have two options:

1. **Modifying the `pos` attribute of the Block object:**

    This is useful when you know the full new position of the block.
    
    ```py
    import cm2py as cm2
    
    # Create a save with an AND gate at (0, 0, 0)
    save = cm2.Save()
    block = save.addBlock(cm2.AND, (0, 0, 0))

    # Move that AND gate to (1, 2, 3)
    block.pos = (1, 2, 3)
    ```

2. **Modifying the individual `x`, `y` and `z` attributes of the Block object:**

    This is useful when you only know the new position for a single axis of the block.

    ```py
    import cm2py as cm2

    # Create a save with an AND gate at (0, 0, 0)
    save = cm2.Save()
    block = save.addBlock(cm2.AND, (0, 0, 0))

    # Set that AND gate's X position to 4
    block.x = 4
    ```

## Connections

TODO
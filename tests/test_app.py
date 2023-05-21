import pytest

from src import cm2py as cm2


def test_addBlocks():
    save = cm2.Save()

    save.addBlock(cm2.NOR, (0, 0, 0))
    save.addBlock(cm2.AND, (1, 0, 0))
    save.addBlock(cm2.OR, (2, 0, 0))
    save.addBlock(cm2.XOR, (3, 0, 0))
    save.addBlock(cm2.BUTTON, (4, 0, 0))
    save.addBlock(cm2.FLIPFLOP, (5, 0, 0))
    save.addBlock(cm2.LED, (6, 0, 0))
    save.addBlock(cm2.SOUND, (7, 0, 0))
    save.addBlock(cm2.CONDUCTOR, (8, 0, 0))
    save.addBlock(cm2.CUSTOM, (9, 0, 0))
    save.addBlock(cm2.XNOR, (10, 0, 0))

    save.exportSave()


def test_addConnections():
    save = cm2.Save()

    b1 = save.addBlock(cm2.OR, (0, 0, 0))
    b2 = save.addBlock(cm2.OR, (2, 0, 0))

    c1 = save.addConnection(b1, b2)
    c2 = save.addConnection(b2, b1)

    save.exportSave()


def test_deleteBlock1():
    save = cm2.Save()

    b1 = save.addBlock(cm2.OR, (0, 0, 0))
    b2 = save.addBlock(cm2.OR, (2, 0, 0))

    c1 = save.addConnection(b1, b2)

    save.deleteBlock(b1)

    save.exportSave()


def test_deleteBlock2():
    save = cm2.Save()

    b1 = save.addBlock(cm2.OR, (0, 0, 0))
    b2 = save.addBlock(cm2.OR, (2, 0, 0))

    c1 = save.addConnection(b1, b2)

    save.deleteBlock(b2)

    save.exportSave()

import pytest

from src import cm2py as cm2
from src.cm2py import building_definitions
from random import randint


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
    save.addBlock(cm2.NAND, (10, 0, 0))
    save.addBlock(cm2.XNOR, (11, 0, 0))
    save.addBlock(cm2.RANDOM, (12, 0, 0))
    save.addBlock(cm2.TEXT, (13, 0, 0))
    save.addBlock(cm2.TILE, (14, 0, 0))
    save.addBlock(cm2.NODE, (15, 0, 0))
    save.addBlock(cm2.DELAY, (16, 0, 0))
    save.addBlock(cm2.ANTENNA, (17, 0, 0))
    save.addBlock(cm2.CONDUCTOR_V2, (18, 0, 0))
    save.addBlock(cm2.LED_MIXER, (19, 0, 0))

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


def test_deleteConnection():
    save = cm2.Save()

    b1 = save.addBlock(cm2.OR, (0, 0, 0))
    b2 = save.addBlock(cm2.OR, (2, 0, 0))

    c1 = save.addConnection(b1, b2)

    save.deleteConnection(c1)

    save.exportSave()


def test_properties():
    save = cm2.Save()

    b1 = save.addBlock(cm2.LED, (0, 0, 0), properties=[255, 0, 0])

    save.exportSave()


def test_move():
    save = cm2.Save()

    b1 = save.addBlock(cm2.OR, (1, 2, 3))
    assert b1.pos == (1, 2, 3)
    assert b1.x == 1 and b1.y == 2 and b1.z == 3

    b1.pos = (4, 5, 6)
    assert b1.pos == (4, 5, 6)
    assert b1.x == 4 and b1.y == 5 and b1.z == 6

    b1.x = 7
    b1.y = 8
    b1.z = 9
    assert b1.pos == (7, 8, 9)
    assert b1.x == 7 and b1.y == 8 and b1.z == 9


def test_importSave():
    string = (
        "0,0,0,0,3,;0,0,1,0,3,;0,0,2,0,3,;7,1,17,0,6,;7,0,-9,0,3,1.00;"
        "7,0,20,0,6,1.00;7,0,4,0,-8,10000.00;7,0,19,0,4,;7,0,0,0,-4,100.00;7,0,17,0,2,;"
        "7,1,20,0,2,;7,0,17,0,4,;7,1,20,0,5,;7,0,-1,0,-5,;7,0,0,0,-6,1000.00;"
        "7,1,18,0,4,;7,0,6,0,-8,10000.00;7,0,-5,0,-5,1.00;7,1,17,0,5,;7,0,0,0,-2,10.00;"
        "7,1,20,0,4,;7,0,17,0,3,;7,0,8,0,-8,;7,0,-9,0,1,10.00;7,0,2,0,-8,10000.00;"
        "7,0,0,0,-8,10000.00;7,0,-9,0,-1,100.00;7,0,-9,0,-5,10000.00;7,0,0,0,0,1.00;"
        "7,1,20,0,3,;7,0,-7,0,-5,10000.00;7,0,-3,0,-5,10000.00;7,0,-9,0,-3,1000.00?"
        "16,1;29,11;6,12;24,30;19,9;28,15;21,24;9,16;22,4;25,28;14,20;2,21;26,17;"
        "27,8;8,5;1,3;23,22;10,18;30,25;5,13;3,10;7,19;13,7;12,23;18,27;17,6;15,29??"
    )

    save = cm2.importSave(string)


def test_omittedValues():
    string = "0,,,,,;0,,1,2,3,;0,0,1,2,,???"

    save = cm2.importSave(string)


def test_importSingleBlock():
    string = "0,0,0,0,0,???"

    save = cm2.importSave(string)


def test_buildingObjectCreation():
    for i in range(100):
        buildingPos = tuple([randint(-100, 100) for i in range(3)])

        building = cm2.Building(
            cm2.BuildingType.MASS_MEMORY, buildingPos, cm2.Rotation.NORTH
        )

        assert (
            building.pos == buildingPos
            and building.x == buildingPos[0]
            and building.y == buildingPos[1]
            and building.z == buildingPos[2]
        )

        with pytest.raises(AssertionError):
            building.buildingType = cm2.BuildingType.TEXT_CONSOLE

        with pytest.raises(AssertionError):
            building.blocks = []


def test_buildingBlockObjectCreation():
    for i in range(100):
        buildingPos = tuple([randint(-100, 100) for i in range(3)])
        blockOffset = tuple([randint(-100, 100) for i in range(3)])

        building = cm2.Building(
            cm2.BuildingType.MASS_MEMORY, buildingPos, cm2.Rotation.NORTH
        )

        block = cm2.BuildingBlock(
            cm2.IOType.INPUT,
            blockOffset,
            parentBuilding=building,
            state=False,
            index=0,
        )

        assert (
            block.pos == tuple([sum(x) for x in zip(buildingPos, blockOffset)])
            and block.x == buildingPos[0] + blockOffset[0]
            and block.y == buildingPos[1] + blockOffset[1]
            and block.z == buildingPos[2] + blockOffset[2]
        )
        assert block.state == False

        block.state = True

        assert block.state == True

        with pytest.raises(AttributeError):
            block.pos = tuple([randint(-100, 100) for i in range(3)])

        with pytest.raises(AttributeError):
            block.properties = [randint(-100, 100) for i in range(5)]


def test_buildingCreatesCorrectBlocks():
    for buildingType in building_definitions.definitions.keys():
        for i in range(10):
            print(buildingType)
            buildingPos = tuple([randint(-100, 100) for i in range(3)])

            building = cm2.Building(buildingType, buildingPos, cm2.Rotation.NORTH)

            buildingDefinition = building_definitions.definitions[buildingType]

            for i, block in enumerate(building.blocks):
                definitionBlock = buildingDefinition.blocks[i]
                assert block.parentBuilding == building
                assert block.posOffset == definitionBlock[0]
                assert block.IOType == definitionBlock[1]
                assert block.pos == tuple(
                    [sum(v) for v in zip(definitionBlock[0], buildingPos)]
                )
                assert block.blockId == cm2.CUSTOM
                assert block.state == False
                assert block.index == i


def test_addBuilding():
    save = cm2.Save()
    for buildingType in building_definitions.definitions.keys():
        for i in range(10):
            print(buildingType)
            buildingPos = tuple([randint(-100, 100) for i in range(3)])

            building = save.addBuilding(buildingType, buildingPos, cm2.Rotation.NORTH)

"""
Some basic data types
"""

from enum import Enum, IntEnum

class StrEnum(str, Enum):
    pass


class Dimension(IntEnum):
    nether = -1
    overworld = 0
    end = 1

class Gamemode(IntEnum):
    survival = 0
    creative = 1
    adventure = 2
    spectator = 3

class Difficulty(IntEnum):
    peaceful = 0
    easy = 1
    normal = 2
    hard = 3

class LevelType(StrEnum):
    default = 'DEFAULT'
    flat = 'FLAT'
    large_biomes = 'LARGEBIOMES'
    amplified = 'AMPLIFIED'
    customized = 'CUSTOMIZED'

def string_to_bool(string):
    if string.lower() in ["true", "yes"]:
        return True
    elif string.lower() in ["false", "no"]:
        return False

    raise ValueError

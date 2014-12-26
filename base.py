"""
Some basic data types
"""

from enum import Enum, IntEnum


class Dimension(Enum):
    nether = -1
    overworld = 0
    end = 1

class Gamemode(Enum):
    survival = 0
    creative = 1
    adventure = 2
    spectator = 3

class Difficulty(Enum):
    peaceful = 0
    easy = 1
    normal = 2
    hard = 3

class LevelType(Enum):
    default = 'DEFAULT'
    flat = 'FLAT'
    large_biomes = 'LARGEBIOMES'
    amplified = 'AMPLIFIED'
    customized = 'CUSTOMIZED'

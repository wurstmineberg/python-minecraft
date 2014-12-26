"""
Server properties
"""

from parser.base import SynthesizeableParsedObject
from parser.server_properties import ServerPropertiesParserSynthesizer
from base import Gamemode, Difficulty, Dimension, LevelType

class ServerProperties(SynthesizeableParsedObject):
    _default_properties = {
        'spawn-protection': 16,
        'max-tick-time': 6000,
        'generator-settings': None,
        'force-gamemode': False,
        'allow-nether': True,
        'gamemode': Gamemode.survival,
        'enable-query': False,
        'player-idle-timeout': 0,
        'difficulty': Difficulty.easy,
        'spawn-monsters': True,
        'op-permission-level': 4,
        'resource-pack-hash': None,
        'announce-player-achievements': True,
        'pvp': True,
        'snooper-enabled': True,
        'level-type': LevelType.default,
        'hardcore': False,
        'enable-command-block': False,
        'max-players': 20,
        'network-compression-threshold': 256,
        'max-world-size': 29999984,
        'server-port': 25565,
        'server-ip': None,
        'spawn-npcs': True,
        'allow-flight': False,
        'level-name': 'world',
        'view-distance': 10,
        'resource-pack': None,
        'spawn-animals': True,
        'white-list': False,
        'generate-structures': True,
        'online-mode': True,
        'max-build-height': 256,
        'level-seed': None,
        'use-native-transport': True,
        'motd': 'A Minecraft Server',
        'enable-rcon': False
    }

    def __init__(self, properties_filename):
        super().__init__()

        self._properties_filename = properties_filename

    def reset_to_default(self):
        """This will reset the server.properties file to default"""
        self._attributes = self._default_properties

    def _get_new_parser(self):
        return ServerPropertiesParserSynthesizer(self._properties_filename)

    def _get_new_synthesizer(self):
        return self._get_new_parser()

    def __str__(self):
        return str(self._attributes)

    def __repr__(self):
        return '<ServerProperties attributes:' + str(self._attributes) + '>'

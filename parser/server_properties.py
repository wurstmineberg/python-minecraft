"""
server.properties parser
"""

from .base import Parser
from base import Gamemode, Difficulty, LevelType, string_to_bool


class ServerPropertiesParser(Parser):
    def __init__(self, properties_filename):
        """Parses a server directory"""
        self.properties_filename = properties_filename
        self.reload_data()

    def parse_keys(self):
        return [
            'allow-flight',
            'allow-nether',
            'announce-player-achievements',
            'difficulty',
            'enable-query',
            'enable-rcon',
            'enable-command-block',
            'force-gamemode',
            'gamemode',
            'generate-structures',
            'generator-settings',
            'hardcore',
            'level-name',
            'level-seed',
            'level-type',
            'max-build-height',
            'max-players',
            'max-tick-time',
            'max-world-size',
            'motd',
            'max-players',
            'network-compression-threshold',
            'online-mode',
            'op-permission-level',
            'player-idle-timeout',
            'pvp',
            'query.port',
            'rcon.password',
            'rcon.port',
            'resource-pack',
            'resource-pack-hash',
            'server-ip',
            'server-port'
            'snooper-enabled',
            'spawn-animals',
            'spawn-monsters',
            'spawn-npcs',
            'spawn-protection',
            'use-native-transport',
            'view-distance',
            'white-list',
        ]

    def reload_data(self):
        with open(self.properties_filename, encoding='utf8') as properties_file:
            self.properties_string = properties_file.readlines()

    def parse_value(self, key, value):
        if key in ('allow-flight', 'allow-nether', 'announce-player-achievements', 'enable-query', 'enable-rcon',
                   'enable-command-block', 'force-gamemode', 'generate-structures', 'hardcore', 'online-mode',
                   'pvp', 'snooper-enabled', 'spawn-animals', 'spawn-monsters', 'spawn-npcs', 'use-native-transport',
                   'white-list'):
            return string_to_bool(value)
        elif key in ('max-build-height', 'max-players', 'max-tick-time', 'max-world-size',
                     'network-compression-threshold', 'op-permission-level', 'player-idle-timeout', 'rcon.port',
                     'server-port', 'spawn-protection', 'view-distance'):
            return int(value)
        elif key == 'difficulty':
            return Difficulty(value)
        elif key == 'gamemode':
            return Gamemode(int(value))
        elif key == 'generator-settings':
            # TODO: Add a class to simplify game generation
            return value
        elif key == 'level-type':
            return LevelType(int(value))
        else:
            return value

    def parse_line(self, line):
        if line.strip()[0] == '#':
            # ignore comments
            return None

        key_value = line.strip().split("=", 2)
        if len(key_value) != 2:
            return None

        key = key_value[0]
        value = key_value[1]

        return (key, value)

    def parse_attribute(self, parseKey):
        for line in self.properties_string:
            result = self.parse_line(line)
            if result is not None:
                key, value = result
                if key.strip() == parseKey.strip():
                    return self.parse_value(key, value)

    def parse_all(self):
        attributes = {}
        for line in self.properties_string:
            result = self.parse_line(line)
            if result is not None:
                key, value = result
                attributes[key] = value

        return attributes


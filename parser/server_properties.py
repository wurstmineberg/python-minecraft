"""
server.properties parser
"""

from .base import Parser, Synthesizer
from base import Gamemode, Difficulty, LevelType


class ServerPropertiesParserSynthesizer(Parser, Synthesizer):
    def __init__(self, properties_filename):
        """Parses a server directory"""
        self.properties_filename = properties_filename
        self.reload_data()

    bool_keys = ['allow-flight', 'allow-nether', 'announce-player-achievements', 'enable-query', 'enable-rcon',
                   'enable-command-block', 'force-gamemode', 'generate-structures', 'hardcore', 'online-mode',
                   'pvp', 'snooper-enabled', 'spawn-animals', 'spawn-monsters', 'spawn-npcs', 'use-native-transport',
                   'white-list']
    int_keys = ['max-build-height', 'max-players', 'max-tick-time', 'max-world-size', 'network-compression-threshold',
                'op-permission-level', 'player-idle-timeout', 'rcon.port', 'server-port', 'spawn-protection',
                'view-distance']

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

    def string_to_bool(self, string):
        if string.lower() in ["true"]:
            return True
        elif string.lower() in ["false"]:
            return False

        raise ValueError

    def bool_to_string(self, bool):
        if bool:
            return 'true'
        else:
            return 'false'


    def reload_data(self):
        with open(self.properties_filename, mode='rt', encoding='utf-8') as properties_file:
            self.properties_string = properties_file.readlines()

    def parse_value(self, key, value):
        if value == '':
            return None
        elif key in self.bool_keys:
            return self.string_to_bool(value)
        elif key in self.int_keys:
            return int(value)
        elif key == 'difficulty':
            return Difficulty(int(value))
        elif key == 'gamemode':
            return Gamemode(int(value))
        elif key == 'generator-settings':
            # TODO: Add a class to simplify game generation
            return value
        elif key == 'level-type':
            return LevelType(value)
        else:
            # process escape characters in the string
            return bytes(value, 'utf-8').decode('unicode_escape')

    def parse_line(self, line):
        line = line.strip()
        if len(line) == 0:
            return None

        if line[0] == '#':
            # ignore comments
            return None

        key_value = line.split('=', 2)
        if len(key_value) != 2:
            return None

        key = key_value[0]
        value = self.parse_value(key, key_value[1])

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

    def synthesize_attribute(self, key, value):
        if value is None:
            return ''
        elif key in self.bool_keys:
            return self.bool_to_string(value)
        elif key in self.int_keys:
            return str(value)
        elif key == 'difficulty':
            return str(int(value))
        elif key == 'gamemode':
            return str(int(value))
        elif key == 'generator-settings':
            return value
        elif key == 'level-type':
            return LevelType(value)
        else:
            # insert escape characters in the string
            return value.encode('unicode_escape').decode('utf-8')


    def write(self, attributes):
        # synthesize properties
        result = '#Minecraft server properties\n'
        result += '#Generated with minecraftlib\n'

        from datetime import datetime, timezone
        dt = datetime.now(timezone.utc)
        date_str = dt.strftime('%a %b %d %H:%M:%S %Z %Y')
        result += '#' + date_str + '\n'

        for key, value in sorted(attributes.items()):
            result += key
            result += '='
            result += self.synthesize_attribute(key, value)
            result += '\n'

        with open(self.properties_filename, mode='wt', encoding='utf-8') as properties_file:
            print(result, file=properties_file)


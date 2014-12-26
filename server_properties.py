"""
Server properties
"""

from parser.base import ParsedObject
from parser.server_properties import ServerPropertiesParser


class ServerProperties(ParsedObject):
    def __init__(self, properties_filename):
        self._properties_filename = properties_filename

    def _get_new_parser(self):
        return ServerPropertiesParser(self._properties_filename)

    def __str__(self):
        return str(self._attributes)

    def __repr__(self):
        return '<ServerProperties attributes:' + str(self._attributes) + '>'

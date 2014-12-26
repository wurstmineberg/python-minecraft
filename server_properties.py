"""
Server properties
"""

from parser.base import SynthesizeableParsedObject
from parser.server_properties import ServerPropertiesParserSynthesizer


class ServerProperties(SynthesizeableParsedObject):
    def __init__(self, properties_filename):
        super().__init__()

        self._properties_filename = properties_filename

    def _get_new_parser(self):
        return ServerPropertiesParserSynthesizer(self._properties_filename)

    def _get_new_synthesizer(self):
        return self._get_new_parser()

    def __str__(self):
        return str(self._attributes)

    def __repr__(self):
        return '<ServerProperties attributes:' + str(self._attributes) + '>'

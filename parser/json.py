"""
Defines an abstract JSON parser/synthesizer
"""

from parser.base import Parser, Synthesizer, SynthesizeableParsedObject
import inc.lazyjson.lazyjson


class UncheckedJSONParser(Parser):
    """Parses a JSON file"""

    def __init__(self, filename):
        self.json_filename = filename
        self.lazy_file = lazyjson.File(filename)

    @property
    def parse_keys(self):
        return None

    def parse_attribute(self, key):
        return None


class UncheckedJSONSynthesizer(Synthesizer):
    """Synthesizes a JSON file"""

    def __init__(self, filename):
        self.json_filename = filename
        self.lazy_file = lazyjson.File(filename)


class UncheckedJSONObject(SynthesizeableParsedObject):
    """A simple object that is able to read and write JSON files"""

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def _get_new_parser(self):
        return UncheckedJSONParser(self._filename)

    def _get_new_synthesizer(self):
        return UncheckedJSONSynthesizer(self._filename)

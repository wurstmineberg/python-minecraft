"""
General parser superclasses
"""

from abc import ABCMeta, abstractmethod, abstractproperty


class Parser(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def parse_attribute(self, key):
        return None

    @abstractmethod
    def parse_keys(self):
        return None

    @abstractmethod
    def reload_data(self):
        pass

    def parse_all(self):
        attributes = {}
        for key in self.parse_keys():
            attributes[key] = self.parse_attribute(key)

        return attributes


class Synthesizer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def write(self, attributes):
        pass


class ParsedObject(object):
    __metaclass__ = ABCMeta
    _attributes = {}
    _parser_instance = None

    @abstractmethod
    def _get_new_parser(self):
        return None

    def _parser(self):
        if self._parser_instance is None:
            self._parser_instance = self._get_new_parser()
        return self._parser_instance

    def _parse_all(self):
        self._parser().parse_all()

    def _get_parsed_attribute(self, key):
        print("key: "+ key)
        if key not in self._parser().parse_keys():
            raise AttributeError

        if key not in self._attributes:
            attr = self._parser().parse_attribute(key)
            self._attributes[key] = attr

        return self._attributes[key]

    def _get_all(self):
        self._attributes = self._parser().parse_all()

    def __getattr__(self, item):
        return self._get_parsed_attribute(item)


class SynthesizeableParsedObject(ParsedObject):
    __metaclass__ = ABCMeta
    _synthesizer_instance = None

    @abstractmethod
    def _get_new_synthesizer(self):
        return None

    def _write(self):
        self._synthesizer().write(self._attributes)

    def _synthesizer(self):
        if not self._synthesizer_instance:
            self._synthesizer_instance = self._get_new_synthesizer()
        return self._synthesizer_instance

    def __setattr__(self, key, value):
        if key[0] != '_' and key in self._parser().parse_keys():
            self._attributes[key] = value
        else:
            super().__setattr__(key, value)


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


class ParsedObject(object):
    __metaclass__ = ABCMeta
    _attributes = {}
    _parser_instance = None

    @abstractmethod
    def _get_new_parser(self):
        return None

    def _parser(self):
        if not self._parser_instance:
            _parser_instance = self._get_new_parser()
        return _parser_instance

    def _parse_all(self):
        self._parser().parse_all()

    def _get_parsed_attribute(self, key):
        if key not in self._attributes:
            attr = self._parser().parse_attribute(key)
            self._attributes[key] = attr

        return self._attributes[key]

    def _get_all(self):
        self._attributes = self._parser().parse_all()

    def __getattribute__(self, item):
        try:
            return super().__getattribute__(item)
        except AttributeError:
            return self._get_parsed_attribute(item)

#!/usr/bin/env python
"""
General parser superclasses
"""

from abc import ABCMeta, abstractmethod, abstractproperty


class Parser(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def parse_attribute(self, key):
        return None


class ParsedObject(object):
    __metaclass__ = ABCMeta
    _attributes = {}

    @abstractproperty
    def parser_keys(self):
        return []

    @abstractproperty
    def parser(self):
        return None

    def _parse_attribute(self, key):
        return self.parser().parse_attribute(key)

    def parse_all(self):
        for key in self.parser_keys():
            self.parse_attribute(key)

    def _get_parsed_attribute(self, key):
        if key not in self._attributes:
            attr = self._parse_attribute(key)
            self._attributes[key] = attr

        return self._attributes[key]

    def __getattribute__(self, item):
        try:
            return super().__getattribute__(item)
        except AttributeError:
            return self._get_parsed_attribute(item)

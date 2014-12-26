"""
General parser superclasses
"""

from abc import ABCMeta, abstractmethod


class Parser(metaclass=ABCMeta):

    @abstractmethod
    def parse_attribute(self, key):
        return None

    @property
    @abstractmethod
    def parse_keys(self):
        return None

    @abstractmethod
    def reload_data(self):
        pass

    def parse_all(self):
        attributes = {}

        if self.parse_keys is not None:
            for key in self.parse_keys:
                attributes[key] = self.parse_attribute(key)
        else:
            raise NotImplementedError('Parser.parse_all() must be overridden if the parser is unchecked (you have'
                                      'Parser.parse_keys as None)')

        return attributes


class Synthesizer(metaclass=ABCMeta):

    @abstractmethod
    def write(self, attributes):
        pass


class FileParser(Parser, metaclass=ABCMeta):
    """Parses a file"""

    import os.stat

    def __init__(self, filename, **open_kwargs):
        self.filename = filename
        self._open_kwargs = open_kwargs
        self.file = None
        self.reload_file()

    def open(self):
        self.file = open(self.filename, **self._open_kwargs)
        self._opened_time = os.stat(self.filename).st_mtime

    def close(self):
        self.file.close()

    def reload(self):
        if self.file:
            self.close_file()

        self.file = self.open_file()

    @property
    def has_changed(self):



class FileSynthesizer(Synthesizer, metaclass=ABCMeta):
    """Synthesizes a file"""

    from threading import Lock

    def __init__(self, filename, **open_kwargs):
        self.filename = filename
        self._open_kwargs = open_kwargs
        if not 'mode' in self._open_kwargs:
            self._open_kwargs['mode'] = 'w'

        self._write_lock = Lock()

    @abstractmethod
    def synthesize(self, attributes):
        return None

    def write(self, attributes):
        with self._write_lock:
            data = self.synthesize(attributes)

            with open(self.filename, **self._open_kwargs) as file:
                file.write(data)


class ParsedObject(metaclass=ABCMeta):
    _parser_instance = None

    def __init__(self):
        self._attributes = {}
        self._loaded_all = False

    def parsed_dict(self):
        """
        Returns a copy of the parsed dict. This is not meant to be altered, use the getitem and setitem functions for
        that. Example: Server.properties or Server['properties']. As this will load everything from disk first, use it
        only if you need it
        """
        if not self._loaded_all:
            self._get_all()

        return self._attributes.copy()

    @abstractmethod
    def _get_new_parser(self):
        return None

    @property
    def _parser(self):
        if self._parser_instance is None:
            self._parser_instance = self._get_new_parser()
        return self._parser_instance

    def _parse_all(self):
        self._parser.parse_all()

    def _get_parsed_attribute(self, key):
        if self._parser.parse_keys is not None:
            if key not in self._parser.parse_keys:
                raise AttributeError("key: " + key)

        if key not in self._attributes:
            attr = self._parser.parse_attribute(key)
            self._attributes[key] = attr

        return self._attributes[key]

    def _get_all(self):
        """Gets all attributes that are not already loaded."""
        all_attributes = self._parser.parse_all()
        if 'properties' in all_attributes:
            raise Exception

        for key, value in all_attributes.items():
            if key not in self._attributes:
                self._attributes[key] = value

        self._loaded_all = True

    def __getattr__(self, item):
        return self._get_parsed_attribute(item)

    def __getitem__(self, item):
        return self._get_parsed_attribute(item)


class SynthesizeableParsedObject(ParsedObject, metaclass=ABCMeta):
    _synthesizer_instance = None

    @abstractmethod
    def _get_new_synthesizer(self):
        return None

    def _write(self):
        # First make sure to actually get all objects that are parsed
        if not self._loaded_all:
            self._get_all()

        self._synthesizer().write(self._attributes)

    def _synthesizer(self):
        if not self._synthesizer_instance:
            self._synthesizer_instance = self._get_new_synthesizer()
        return self._synthesizer_instance

    def _set_attribute(self, key, value):
        """Sets an attribute of the parsed object"""

        # Before setting anything we load the whole thing.
        # Lazy loading doesn't help us here from now on
        if not self._loaded_all:
            self._get_all()

        self._attributes[key] = value

    def _del_attribute(self, key):
        """Deletes an attribute of the parsed object"""

        # We need to load everything here, because otherwise
        # it would get overridden
        if not self._loaded_all:
            self._get_all()

        del self._attributes[key]

    def __setattr__(self, key, value):
        if key[0] != '_' and self._parser.parse_keys is not None and key in self._parser.parse_keys:
            self._set_attribute(key, value)
        else:
            super().__setattr__(key, value)

    def __setitem__(self, key, value):
        if self._parser.parse_keys is not None and key in self._parser.parse_keys:
            self._attributes[key] = value
        else:
            raise AttributeError('The key "' + key + '" is not supported')

    def __delattr__(self, item):
        if self._parser.parse_keys is not None and item in self._parser.parse_keys:
            self._del_attribute(item)
        else:
            super().__delattr__(item)

    def __delitem__(self, key):
        self._del_attribute(key)


class ParsedFileObject(ParsedObject, metaclass=ABCMeta):
    @abstractmethod
    def _get_new_parser(self):
        return None

    @property
    def _parser(self):
        if self._parser_instance is None:
            self._parser_instance = self._get_new_parser()
        return self._parser_instance


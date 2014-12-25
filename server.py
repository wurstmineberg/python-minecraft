#!/usr/bin/env python
"""
Class for a minecraft server
"""

from parser.base import ParsedObject
from parser.server import ServerDirParser


class Server(ParsedObject):
    parser_instance = None

    def parser_keys(self):
        return [
            'properties',
        ]

    def parser(self):
        if not self.parser_instance:
            self.parser_instance = ServerDirParser(self.server_dir)
        return self.parser_instance
        return ServerDirParser(self.server_dir)

    def __init__(self, server_dir):
        """Initializes a server"""
        self.server_dir = server_dir

    def start(self):
        """
        Forks a new process and starts the server.
        This creates a PID file in the server directory so that a server only
        runs once at a time.
        """
        pass

    def stop(self):
        """
        Finds out the server process PID and stops the server. Deletes the PID
        file afterwards.
        """
        pass

"""
Class for a minecraft server
"""

from parser.base import ParsedObject
from parser.server import ServerDirParser


class Server(ParsedObject):

    def __init__(self, server_dir):
        """Initializes a server"""
        self._server_dir = server_dir

    def _get_new_parser(self):
        return ServerDirParser(self._server_dir)

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

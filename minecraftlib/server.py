"""
Class for a minecraft server
"""

from parser.base import ParsedObject
from parser.server import ServerDirParser


class Server(ParsedObject):

    def __init__(self, server_dir):
        """Initializes a server"""
        super().__init__()

        self._server_dir = server_dir

    def __repr__(self):
        return '<Server name: '+ self.properties.level-name +' motd: ' + self.properties.motd + '>'

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

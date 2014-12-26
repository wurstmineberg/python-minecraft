"""
Parser for a minecraft server directory
"""

import os.path
from .base import Parser
from server_properties import ServerProperties


class ServerDirParser(Parser):

    def __init__(self, server_dir):
        """Parses a server directory"""
        self.server_dir = server_dir

    def parse_keys(self):
        return [
            'properties',
        ]

    def reload_data(self):
        pass

    def parse_attribute(self, key):
        if key == "properties":
            return ServerProperties(os.path.join(self.server_dir, "server.properties"))


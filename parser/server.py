#!/usr/bin/env python
"""
Parser for a minecraft server directory
"""

import os.path
from .base import Parser


class ServerDirParser(Parser):

    def __init__(self, server_dir):
        """Parses a server directory"""
        self.server_dir = server_dir

    def parse_attribute(self, key):
        if key == "properties":
            # return ServerProperties(os.path.join(self.server_dir, "server.properties"))
            return "properties"

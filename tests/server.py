#!/usr/bin/env python
"""
Tests the server object and parser
"""

from server import Server


def run():
    server = Server("./wurstmineberg_server")
    print(server.properties)
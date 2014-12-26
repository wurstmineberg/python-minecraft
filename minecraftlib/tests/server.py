"""
Tests the server object and parser
"""

from server import Server


def run():
    server = Server('./wurstmineberg_server')
    print(server.properties.parsed_dict())
    server.properties.motd = "Hi there"
    server.properties._write()


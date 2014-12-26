"""
Tests the server object and parser
"""

from server import Server


def run():
    server = Server('./wurstmineberg_server')
    print(server.properties)
    print(server.properties.motd)
    server.properties.motd = 'bla'
    server.properties['rcon.port'] = None
    del server.properties['rcon.port']
    server.properties._write()


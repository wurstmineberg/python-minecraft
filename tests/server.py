"""
Tests the server object and parser
"""

from server import Server


def run():
    server = Server("./wurstmineberg_server")
    server._get_all()
    server.properties._get_all()
    print(server)

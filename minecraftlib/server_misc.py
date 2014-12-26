"""
Some not so commonly used server classes
"""

from parser.json import UncheckedJSONObject


class ServerBannedIPs(UncheckedJSONObject):
    def __init__(self):
        super().__init__()


from setuptools import setup

__version__ = '0.0.1'

import sys

if sys.version_info < (3, 4):
      print('This module only supports python 3.4 and higher!')
      #exit(1)

setup(name = 'minecraftlib',
      version = __version__,
      description = 'Minecraftlib is a library to manage Minecraft Servers',
      url = 'http://github.com/wurstmineberg/python-minecraft',
      author = 'farthen',
      author_email = 'monkey@farthen.de',
      license = 'MIT',
      packages = ['minecraftlib'],
      install_requires = [
          'watchdog>=0.8.2'
      ]
      )

#!/usr/bin/env python3

from distutils.core import setup

setup(name='deware',
      version='1.0',
      description='deware sensor software',
      author='simone massaro',
      author_email='mone.massaro@gmail.com',
      url='https://github.com/mone27/deware',
      packages=['deware.core', 'deware.gui'],
      scripts=['deware/core/main.py','deware/gui/app.py'],
     )

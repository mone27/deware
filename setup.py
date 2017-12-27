#!/usr/bin/env python3

from distutils.core import setup

setup(name='deware',
      version='0.0.1',
      description='deware sensor software',
      author='simone massaro',
      author_email='mone.massaro@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['deware.core', 'deware.gui'],
      scripts=['deware/core/main.py','deware/gui/app.py'],
     )

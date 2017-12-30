#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 09:36:28 2017

@author: simone
"""

from deware.core import get_data
from deware.core import save_db
import logging

logging.basicConfig(level = logging.DEBUG)
data_input = get_data.sensors_read()
db_manager_proc = save_db.db_manager()
data_input.start()
db_manager_proc.start()

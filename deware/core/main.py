#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 09:36:28 2017

@author: simone
"""
import sys
print(sys.version)
from deware.core import get_data
from deware.core import save_db
from deware.core import settings as setg
import logging
if setg.log_to_console:
    logging.basicConfig(level = logging.DEBUG)
else:
    logging.basicConfig(filename=setg.log_file,
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%D:%%H:%M:%S',
                        level=logging.DEBUG)

data_input = get_data.SensorRead().start()
db_manager = save_db.DbManager().start()

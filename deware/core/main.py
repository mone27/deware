#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 09:36:28 2017

@author: simone
"""

import get_data
import save_db
data_input = get_data.sensors_read()
db_manager = save_db.db_manager()
data_input.start()
db_manager.start()

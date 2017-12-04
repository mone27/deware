#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 09:36:28 2017

@author: simone
"""

import get_data
import db_manager
SerialInputProc = SerialInput.SerialInput()
db_manager_proc = db_manager.db_manager()
SerialInputProc.start()
db_manager_proc.start()

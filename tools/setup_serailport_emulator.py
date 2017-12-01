#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 14:11:55 2017

@author: simone
"""

from subprocess import check_output
print(check_output("socat pty,link=vsp_test0 pty,link=vsp_test1", shell=True))
#    raise "failded to create virtual serail port"


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:13:26 2017

@author: simone
"""
#should do somwthing else before
#loads template for service and desktop file
OPTIONS = {
    install_location = 'prova',
    python = 'usr/bin/python3'
}
from string import Template
with open('deware.desktop.tmpl') as t:
    out_f = open('deware.desktop',mode='w')
    out_f.write(Template(t.read()).substitute(OPTIONS))
    out_f.close()

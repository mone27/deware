#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:13:26 2017

@author: simone
"""
from string import Template
import os

#should do somwthing else before
#loads template for service and desktop file
OPTIONS = {
    'install_location': '/home/simone/development/deware/deware',
    'python': 'usr/bin/python3',
    'user_home': '/home/simone/',
}
templates = {
    'desktop': 'deware.desktop.tmpl',
    'service': 'dewared.service.tmpl',
}
def file_template(template_name):
    """ loads a string template from a file (must have .tmpl extension)
    generating corresponding file without .tmpl extension.
    """
    with open(template_name) as t, open(template_name[:-5],mode='w') as out_f:
        out_f.write(Template(t.read()).substitute(OPTIONS))


if __name__ == "__main__":
    [file_template(__) for __ in templates]
# must find a way to install python 3.6 on raspberry
    os.system(Template("ln .....")
              .substitute(OPTIONS.update(templates)))

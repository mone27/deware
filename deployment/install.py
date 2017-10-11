#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:13:26 2017

@author: simone
"""
from string import Template

#should do somwthing else before
#loads template for service and desktop file
OPTIONS = {
    'install_location': 'prova',
    'python': 'usr/bin/python3'
}
templates = [
    'deware.desktop.tmpl',
<<<<<<< HEAD
    'dewared.service.tmpl'
=======
    'deware-core.service.tmpl'
>>>>>>> 20eb804e31222d075164cb469192b6be8113a9d4
]
def file_template(template_name):
    """ loads a string template from a file (must have .tmpl extension)
    generating corresponding file without .tmpl extension.
    """
    with open(template_name) as t, open(template_name[:-5],mode='w') as out_f:
        out_f.write(Template(t.read()).substitute(OPTIONS))
<<<<<<< HEAD


if __name__ == "__main__":
    [file_template(__) for __ in templates]
=======
file_template(templates[0])

#if __name__=='__main__':
#    map(file_template,templates)
>>>>>>> 20eb804e31222d075164cb469192b6be8113a9d4

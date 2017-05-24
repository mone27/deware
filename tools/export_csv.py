#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 18:40:31 2017

@author: simone
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
assert '/home/simone/development/deware' in sys.path
from deware_core.settings import Db
from deware_core.sqlalchemy_models import Record
from sqlalchemy import create_engine
engine = create_engine('sqlite:///%s'%Db.dbFile)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

import csv
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--filter','-f',
                    help = "insert the sqlalchemy orm filter object that \
                    to filter records",
                    default = "filter()"
                    )
args = parser.parse_args()
result = eval('session.query(Record).'+args.filter+'.all()')
with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['date','temperature','humidity'])
    writer.writerows([[i.time,i.temp,i.hum] for i in result])

      
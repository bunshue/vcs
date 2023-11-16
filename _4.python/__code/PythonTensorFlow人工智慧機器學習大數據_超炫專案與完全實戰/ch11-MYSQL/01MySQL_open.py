#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"
try:
 import MySQLdb                         # pip install MySQL-python
except:
 import pymysql as MySQLdb             #  pip install MySQLdb

db = MySQLdb.connect(host="127.0.0.1", user="admin", passwd="admin", db="mydatabase")
cursor = db.cursor()


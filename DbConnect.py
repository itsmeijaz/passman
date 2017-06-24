#!/usr/bin/python
import MySQLdb
import DbController 

database = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="sample_user",         # your username
                     passwd="redhat@456",  # your password
                     db="sample_db")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = database.cursor()
DbController.Add(cur)
database.close()

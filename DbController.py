#!/usr/bin/python
import MySQLdb


database = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="sample_user",         # your username
                     passwd="redhat@456",  # your password
                     db="sample_db")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = database.cursor()


class DbController():
	def Read_Data(obj):
   		obj.server_port = 22
   		obj.server_name = str(raw_input("Enter the server name:"))
   		obj.server_ip = str(raw_input("Enter the IP:"))
   		obj.server_port = int(raw_input("Enter the SSH Port:"))
   		obj.server_root = str(raw_input("Enter the root password:"))
   		obj.wheel_flag = int(raw_input("Enter one if wheel user is enabled:"))
   		if obj.wheel_flag == 1:
      			obj.wheel_username = str(raw_input("Enter wheel user name:"))
      			obj.wheel_password = str(raw_input("Enter wheel password:"))


	def Print_Data(obj):
   		print ("details:"+obj.server_name)

	def Remove_Data(obj,val):
		print ("value:"+val)



database.close()

#def Adding_Data(cur):
#   cur.execute("")
#  for row in cur.fetchall():
#    print row[1]

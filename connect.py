#!/usr/bin/python

hostname = 'localhost'
username = 'root'
password = ''
database = 'pythonconn'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()
    
    #    cur.execute( "SELECT uname, pname FROM employee1" )
    cur.execute( "INSERT INTO `employee1` VALUES ('Raju','Prajapati','Blunderbuzz','13457')" )
    cur.execute( "SELECT fname, lname, uname, pname FROM employee1 WHERE fname='Shantanu'" )

    for firstname, lastname, username, password in cur.fetchall() :
        print (firstname, lastname, username, password) 


print ("Using pymysql…")
import pymysql
myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

print ("Connection Successful!!!")

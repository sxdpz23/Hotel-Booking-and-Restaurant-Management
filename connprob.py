#!/usr/bin/python

hostname = 'localhost'
username = 'root'
password = ''
database = 'pythonconn'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()
    
'''   first='Shreyas'
    last='Patil'
    user='Flamestriker'
    passw='12345'
'''    
    # cur.execute( "SELECT uname, pname FROM employee" )
    cur.execute( "INSERT INTO `employee` VALUES ({0},{1},{2},{3})".format('Shreyas', 'Patil', 'Flamestriker', '12345'))
    cur.execute( "SELECT fname, lname, uname, pname FROM employee WHERE fname={0}".format('Shreyas') )

    for firstname, lastname, username, password in cur.fetchall() :
        print (firstname, lastname, username, password) 


print ("Using pymysql…")
import pymysql
myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

print ("Connection Successful!!!")
import pymysql
from flask import Flask, redirect,render_template,request, url_for
db_connection=None
db_cursor=None
app = Flask(__name__)



def db_connect():
    global db_connection,db_cursor
    try:
        db_connection = pymysql.connect(host="localhost",user="root",passwd="",database="myblog",port=3306)
        print("connected")
        db_cursor=db_connection.cursor()
        return True 
    except:
        print("Error Occured")
        return False 



def db_disconnect():
    global db_connection,db_cursor
    db_connection.close()
    db_cursor.close()

def insertauthor(A_UName,A_Password,A_City):
    isConnected = db_connect()
    if(isConnected):
        insertQuery = "insert into regauthor(A_UName,A_Password,A_City) values (%s,%s,%s);"
        db_cursor.execute(insertQuery,(A_UName,A_Password,A_City))
        db_connection.commit()
        db_disconnect()
        return True
    else:
        return False

def insertuser(U_UName,U_Password,U_City):
    isConnected = db_connect()
    if(isConnected):
        insertQuery = "insert into reguser(U_UName,U_Password,U_City) values (%s,%s,%s);"
        db_cursor.execute(insertQuery,(U_UName,U_Password,U_City))
        db_connection.commit()
        db_disconnect()
        return True
    else:
        return False

def insertblog(P_UName,P_Title,P_Post):
    isConnected=db_connect()
    if(isConnected):
        insertQuery="insert into authorpost(P_UName,P_Title,P_Post) values (%s,%s,%s);"
        db_cursor.execute(insertQuery,(P_UName,P_Title,P_Post))
        db_connection.commit()
        db_disconnect()
        return True
    else:
        return False

def getallpost():
    isconnected= db_connect()
    if (isconnected):
        print("yes connected")
        getquery = "select * from authorpost"
        db_cursor.execute(getquery)
        allData=db_cursor.fetchall()
        db_disconnect()
        return allData

def getpostsbyname(P_UName):
    isConnected=db_connect()
    if(isConnected):
        getquery = "select * from authorpost where P_UName=%s"
        db_cursor.execute(getquery,(P_UName))
        allData=db_cursor.fetchall()
        db_disconnect()
        return allData





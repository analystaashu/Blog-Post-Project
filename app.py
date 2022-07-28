import pymysql
from flask import Flask, redirect,render_template,request, url_for,session
from db import *

db_connection=None
db_cursor=None
app=Flask(__name__)
app.secret_key="secretkey"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/regauthor",methods=["GET","POST"])
def regauthor():
    if request.method == "POST":
        data = request.form
        isInserted = insertauthor(data["A_UName"],data["A_Password"],data["A_City"])
        if(isInserted):
            return redirect(url_for("index"))
    return render_template("regauthor.html")

@app.route("/reguser",methods=["GET","POST"])
def reguser():
    if request.method == "POST":
        data = request.form
        isInserted = insertuser(data["U_UName"],data["U_Password"],data["U_City"])
        if(isInserted):
            return redirect(url_for("index"))
    return render_template("reguser.html")

@app.route("/home")
def home():

    return render_template('home.html',A_UName=session['A_UName'])

@app.route("/loginauthor",methods=["GET","POST"])
def login():
    msg=''

    if request.method == 'POST':
        # Create variables for easy access
        A_UName = request.form['A_UName']
        A_Password = request.form['A_Password']
        db_connection = pymysql.connect(host="localhost",user="root",passwd="",database="myblog",port=3306)
        db_cursor=db_connection.cursor()
        db_cursor.execute('select * from regauthor where A_UName=%s and A_Password=%s ;',(A_UName,A_Password))
        record= db_cursor.fetchone()

        if record:
            session['loggedin']=True
            session['A_UName']=record[1]
            db_connection = pymysql.connect(host="localhost",user="root",passwd="",database="myblog",port=3306)
            db_cursor=db_connection.cursor()
            db_cursor.execute('select P_UNAME from authorpost where p_uname=%s;',(A_UName))
            Pn= db_cursor.fetchall()
            print(Pn[0])
            return render_template("home.html",p=Pn[0][0])
        else:
            msg='incoreect username and password Try again'
    return render_template('loginauthor.html',msg=msg)

@app.route("/addpost",methods=["GET","POST"])
def addpost():
    if request.method == "POST":
        data = request.form
        isInserted = insertblog(data["P_UName"],data["P_Title"],data["P_Post"])
        if(isInserted):
            return redirect(url_for("home"))
    return render_template('addpost.html')

@app.route("/viewpost")
def viewpost():
    name=request.args.get("id")
    db_connection = pymysql.connect(host="localhost",user="root",passwd="",database="myblog",port=3306)
    db_cursor=db_connection.cursor()
    db_cursor.execute('select p_post,p_title from authorpost where p_uname=%s;',(name))
    Pn= db_cursor.fetchall()
    return render_template("home.html",p=Pn)

    
        

if (__name__)=="__main__":
    app.run(debug=True)
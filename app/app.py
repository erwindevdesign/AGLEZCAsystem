from flask import Flask, request, url_for, redirect, abort, render_template

app=Flask(__name__)

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = 'root',
    database = 'prueba'
)

cursor = mydb.cursor(dictionary=True)








if __name__=='__main__':
    app.run(debug=True)
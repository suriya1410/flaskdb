import mysql.connector as mysql
import time

db = mysql.connect(
    host = "database-my.caomyyms75ok.us-east-1.rds.amazonaws.com",
    user = "suriya",
    passwd = "suriya123"
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS regform")
time.sleep(1000)


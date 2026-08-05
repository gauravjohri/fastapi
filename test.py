import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="gaurav",
    password="test123",
    database="demo",
)

print("Connected")
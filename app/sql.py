import mysql.connector

mydb = mysql.connector.connect(host="db", user = "root", password = "Hamza#410", port = "3306", database = "mytodos")

def insert(todo,status):
    mycursor = mydb.cursor()

    sql = "INSERT INTO todos(todo, statu) VALUES (%s, %s)"
    val = (todo,status)
    mycursor.execute(sql,val)
    mydb.commit()

def display():
    mycursor = mydb.cursor() 
    mycursor.execute("SELECT * FROM todos")
    myresult = mycursor.fetchall()
    return myresult

def update(cur_todo, new_todo, status):
    mycursor = mydb.cursor()
    sql = "UPDATE todos SET todo = %s, statu = %s WHERE todo = %s"
    val = (new_todo, status, cur_todo)
    mycursor.execute(sql, val)
    mydb.commit()

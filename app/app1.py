import sql as sq
from flask import Flask, render_template, request
app = Flask(__name__)   
todo = ""
#insert values in todo list and current status 
@app.route("/")
def AddTasks():
    return render_template('AddTask.html')
@app.route("/", methods = ["POST"])
def getval():
   
    todo = request.form['todos']
    status = request.form["status"]
    sq.insert(todo,status)
    return render_template("ViewTasks.html", todo = todo, status = status)
#Display complete list to user 
@app.route("/display")
def display():
    products = sq.display()
    return render_template("display.html", products = products)
#delete from todo list
@app.route("/update", methods = ["GET", "POST"])
def update():
    if request.method == "POST":
        cur_todo = request.form['current']
        new_todo = request.form['new']
        status = request.form['status']
        sq.update(cur_todo, new_todo, status)
    products = sq.display()
    return render_template("update.html", products = products)
    




if __name__=="__main__":
    app.run(host = "0.0.0.0",port = int(5000), debug=True)
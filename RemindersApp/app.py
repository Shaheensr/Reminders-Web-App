from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todos = []

@app.route("/")
def reminders():
    return render_template("reminders.html", todos=todos)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        todo = request.form.get("reminder")
        todos.append(todo)
        return redirect("/")

from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = "Vedant"
    age = "21"
    return render_template("input.html",name = name, age = age)

app.run(debug=True)
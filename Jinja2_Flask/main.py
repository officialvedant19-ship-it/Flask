from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "Devanshu" : 90,
        "Rahul" : 70,
        "Shreyash" : 99
    }
    return render_template('input.html' , marks = marks)
app.run(debug=True)
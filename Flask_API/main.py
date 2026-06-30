from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "Rohan" : 48,
        "kshitij":33,
        "Rahul" : 44,
        "Ethane" : 39
        }
    return jsonify(marks)
app.run(debug=True)
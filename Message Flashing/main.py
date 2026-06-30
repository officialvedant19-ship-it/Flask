from flask import Flask,flash,render_template

app = Flask(__name__)
app.secret_key = "213eri3irh7883412y89jbhjbknvs"

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/logout")
def logout():
    flash("You have been logout!")
    return render_template("index.html")

app.run(debug=True)
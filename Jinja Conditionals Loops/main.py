from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
   marks = {
       "shreyash" : 43,
       "sujal" : 47,
       "harsh" : 50,
       "ethane" : 45
   }
   return render_template('input.html' , marks = marks)
app.run(debug=True)
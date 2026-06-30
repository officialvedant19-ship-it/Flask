from flask import Flask,render_template

#app = Flask(__name__, static_url_path= '/public') # This is how we can change the static url path

app = Flask(__name__,static_url_path='/public',static_folder='asset') # This is the way to change static folder location
@app.route("/")
def hello_world():
    return render_template('input.html')
app.run(debug=True)
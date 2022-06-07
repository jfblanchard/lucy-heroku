from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "blah_blah"

@app.route("/hello")

def index():
    flash("What is your name ?")
    return render_template("index.html")

@app.route("/greet", methods=['POST'])

def greet():
    flash('Hi ' + str(request.form['name_input']) + ', great to meet you!')
    #request.form['name_input']
    return render_template("index.html")

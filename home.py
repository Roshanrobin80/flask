from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def Home():
    return "Welcome"

@app.route('/home1')
def Home1():
    return "Rise up"

@app.route('/index')
def Index():
    return render_template('index.html')

@app.route('/sec')
def sec():
    return render_template('sec.html')

app.run()
from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/secret')
def secret():
    return "you found the secret"

@app.route('/results', methods = ["POST", "GET"])
def results():
    #process the data from the form,
    #stored the data as a dictionary called username
    userdata = dict(request.form)
    print(userdata)
    #access the value of nickname, store as nickname
    nickname = userdata['nickname']
    output = model.flipit(nickname)
    return output

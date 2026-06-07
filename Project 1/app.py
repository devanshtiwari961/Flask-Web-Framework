from flask import Flask
#WSGI Application
app=Flask(__name__)

@app.route('/') #decorator
def welcome():
    return "Welcome to my house"

@app.route('/members') #decorator
def members():
    return "Welcome to my College"


if __name__=='__main__':
    app.run(debug=True)
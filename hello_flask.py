from flask import Flask
from random import randint
app = Flask(__name__)

boosts = ["You are great.", "Smile!", "=)"]

@app.route('/')
def hello_world():
    return "Hello, world!"

@app.route('/boostmyego')
def boost_ego():
    if len(boosts):
        return boosts[randint(0,len(boosts)-1)]
    return ""

@app.route('/number/<int:number>')
def show_number(number):
    return "This number is %d " % number

if __name__ == "__main__":
    app.run(debug=True)
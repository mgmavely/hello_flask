import random
from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def helper():
        return "<b>" + function() + "</b>"

    return helper


def make_emphasis(function):
    def helper():
        return "<em>" + function() + "</em>"

    return helper


def make_underlined(function):
    def helper():
        return "<u>" + function() + "</u>"

    return helper


rng = random.randint(0, 9)


@app.route("/")
def hello():
    return "<h1>Guess a number between 0 and 9</h1>" \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200px>'


@app.route("/<int:num>")
def check(num):
    if num < rng:
        return '<h1 style="color:red;">Too low</h1>' \
               '<img src="https://media.giphy.com/media/H4oLWS4veh9kqxQ1z2/giphy.gif" width=200px>'
    elif num > rng:
        return '<h1 style="color:blue;">Too high</h1>' \
               '<img src="https://media.giphy.com/media/CM1rHbKDMH2BW/giphy.gif" width=200px>'
    else:
        return '<h1 style="color:green;">You got it!</h1>' \
               '<img src="https://media.giphy.com/media/l396ZTR9VynFtYBVe/giphy.gif" width=200px>'


if __name__ == "__main__":
    app.run(debug=True)

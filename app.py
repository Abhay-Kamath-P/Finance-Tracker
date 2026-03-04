from flask import Flask, render_template

app = Flask(__name__)


entries = [
    {
        'debit' : 180,
        'credit' : 0,
        'category' : 'food',
        'date' : '10 Feb, 2026'
    },
    {
        'debit' : 150,
        'credit' : 0,
        'category' : 'travel',
        'date' : '10 Feb, 2026'
    },
    {
        'debit' : 0,
        'credit' : 2000,
        'category' : 'monthly',
        'date' : '1 Mar, 2026'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', entries = entries, title = "Home")

@app.route("/about")
def about():
    return "<h1>I am Abhay</h1>"

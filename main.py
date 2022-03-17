from encodings import search_function
from pydoc import render_doc
from flask import Flask, render_template, render_template_string, request

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    return render_template("report.html", searchingBy=word)

@app.route("/<username>")
def contact(username):
    return f"Hello {username} how are you doing"

app.run(host="0.0.0.0")
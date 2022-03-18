from encodings import search_function
from pydoc import render_doc
from flask import Flask, redirect, render_template, render_template_string, request
from job_scrapper import get_jobs

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    word = request.args.get('word')

    if word:
        word = word.lower()
        jobs = get_jobs()
    else:
        return redirect("/")
    return render_template("report.html", searchingBy=word)

app.run(host="0.0.0.0")
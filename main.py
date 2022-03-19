from flask import Flask, redirect, render_template, request
from job_scrapper import get_jobs

app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    fromDb = db.get(word)

    if word:
        word = word.lower()
        fromDb = db.get(word)
        if fromDb:
           jobs = fromDb
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template(
        "report.html", 
        searchingBy=word,
        resultsNumber=len(jobs),
        jobs=jobs
    )

app.run(host="0.0.0.0")
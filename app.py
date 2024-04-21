from helpers.file import save_to_file
from flask import Flask, render_template, request, redirect, send_file
from scrapers.scrape_bsj import scrape_bsj
from scrapers.scrape_web3 import scrape_web3
from scrapers.scrape_wwr import scrape_wwr

app = Flask("job_scraper")

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")

    if keyword is None or keyword == "":
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        jobs_bsj = scrape_bsj(keyword)
        jobs_web3 = scrape_web3(keyword)
        jobs_wwr = scrape_wwr(keyword)
        jobs = jobs_bsj + jobs_web3 + jobs_wwr

        db[keyword] = jobs

    return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")

    if keyword is None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword?={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)


app.run("0.0.0.0")

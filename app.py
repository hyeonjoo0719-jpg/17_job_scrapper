from flask import Flask, render_template, request, send_file, redirect
from scrapper import search_incruit
from scrapper import search_saramin
from file import save_to_csv

app = Flask(__name__)

db = {}
page = 3

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/search')
def search():
    keyword = request.args.get('keyword')

    if keyword == "":
        return redirect('/')
    if keyword in db:
        jobs = db[keyword]
    else:
        jobs1 = search_incruit(keyword, page)
        jobs2 = search_saramin(keyword, page)
        jobs = jobs1 + jobs2
        db[keyword] = jobs

    return render_template('search.html', jobs = enumerate(jobs), keyword=keyword, count=len(jobs))

@app.route('/file')
def file():
    keyword = request.args.get('keyword')

    if keyword == '':
        return redirect('/')
    if keyword in db:
        jobs = db[keyword]
    else:
        jobs = search_incruit(keyword, page)
        jobs = jobs.append(search_saramin(keyword, page))
    
    save_to_csv(jobs)
    return send_file("./downloads.csv", as_attachment = True)

if __name__ == '__main__':
    app.run()
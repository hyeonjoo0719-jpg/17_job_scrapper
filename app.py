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
        jobs1, jobs2 = db[keyword]
    else:
        jobs1 = search_incruit(keyword, page)
        jobs2 = search_saramin(keyword, page)
        db[keyword] = (jobs1, jobs2)

    return render_template(
        'search.html',
        incruit_jobs=enumerate(jobs1),
        saramin_jobs=enumerate(jobs2),
        keyword=keyword,
        incruit_count=len(jobs1),
        saramin_count=len(jobs2),
    )

@app.route('/file')
def file():
    keyword = request.args.get('keyword')

    if keyword == '':
        return redirect('/')
    if keyword in db:
        jobs1, jobs2 = db[keyword]
    else:
        jobs1 = search_incruit(keyword, page)
        jobs2 = search_saramin(keyword, page)
        db[keyword] = (jobs1, jobs2)

    save_to_csv(jobs1 + jobs2)
    return send_file("./downloads.csv", as_attachment = True)

if __name__ == '__main__':
    app.run(debug=True)
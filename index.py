from flask import Flask, render_template
from scraper import scrap

app = Flask(__name__)

@app.route("/") ##www.domain.com
def index():
    date,post_text,raw_text,post_url = scrap()
    zipped_list = zip(*post_text)
    return render_template("index.html",date=date,zipped_list=zipped_list,raw_text=raw_text,post_url=post_url)


if __name__ == "__main__":
    app.run(debug=False)
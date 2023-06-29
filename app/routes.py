from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


# @app.get("/<name>")
# def main(name):
#     out = ""
#     for number in range(1, 7):
#         out += "<h%s>Hello, %s</h%s>\n" % (number, name, number)
#     return out

@app.get("/")
def main():
    timestamp = datetime.now().strftime("%F %H:%M:%S")
    return render_template("home.html", ts=timestamp)

@app.get("/about")
def about_page():
    return render_template("about.html")
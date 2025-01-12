# to run this:
# export FLASK_APP=WebDev.py
# run flask

# for debugger mode:
# export FLASK_ENV=development

from flask import Flask, render_template, url_for, request, redirect
import csv

from jinja2.lexer import newline_re

app = Flask(__name__)

@app.route("/")
def myhome():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open("database.txt", mode="a") as database:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        file = database.write(f"\n{name}, {email}, {message}")

def write_to_csv(data):
    with open("database.csv", mode="a", newline="") as database2:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/#thankyou")
        except:
            return "did not save to database"
    return "something went wrong, try again"

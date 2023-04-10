from flask import Flask, render_template, request
import csv

app = Flask(__name__)


def write_database(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f' \n{email}, {subject}, {message}')


def write_database_csv(data):
    with open('database.csv', mode='a', newline='') as datbase2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            datbase2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route("/submit_form", methods=['GET', 'POST'])
def submir_form():
    if request.method == 'POST':
        write_database_csv(request.form.to_dict())
        return render_template('/thankyou.html')
    else:
        return 'Something went wrong. Please try again'

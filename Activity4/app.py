import email
import imp
from pickle import TRUE
from typing import Text
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    firstname = request.args.get('firstname')
    lastname = request.args.get('lastname')
    email = request.args.get('email')
    birthday = request.args.get('birthday')
    phone = request.args.get('phone')


    return """
        <html>
        <script type="text/javascript" src="{{ url_for('static', filename='CSS/script.js')}}"></script>
        <body>
        <form action="/">
            <h2>Username: {0} <br> Password: {1} <br> E-mail: {2} <br> Birthdate: {3} <br> Phone Number: {4}</h2>
        </form>
        </body></html>
        """.format(email, birthday, phone)
if __name__ == '__main__':
    app.run(debug=TRUE)
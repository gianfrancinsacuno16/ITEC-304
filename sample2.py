from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
@app.route('/')
def hello():
    name = request.args['name']
    return """
        <html><body>
        <h1>Hello, {0}!</h1>
        The time is {1}.
        </body></html>
        """.format(
    name, str(datetime.now()))
    
# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)
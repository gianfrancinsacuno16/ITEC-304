from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return """
        <html><body>
        <h1>Hello, world!</h1>
        Click <a href="/time">here</a> for the time.
        </body></html>  
        """
@app.route('/time')
def time():
    return """
        <html><body>
        The time is {0}.
        </body></html>
        """.format(str(datetime.now()))
# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)
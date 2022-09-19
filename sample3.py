from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return """<html><body>
        <h1>Welcome to the iMessage</h1>
        <form action="/greet">
          What's your name? <input type ='text' name='username'><br>
          What's your characteristics? <input type='text' name='character'><br>
          <input type='submit' value='Continue'>
         </form>
        </body></html>
        """


@app.route('/greet')
def greet():
    username = request.args.get('username', 'World')
    character = request.args['character']
    if character == '':
        msg = 'You did not tell me your characteristics.'
    else:
        msg = username + ' is ' + character + '.'

    return """
         <html><body>
            <h2>Hello, {0}! </h2>
            {1}
      </body></html>
      """.format(username, msg)


# Launch the Flaskpy dev server
app.run(host="localhost", debug=True)
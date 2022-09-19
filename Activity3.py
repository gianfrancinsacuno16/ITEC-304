from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html><body>
        <h1>Welcome to the Greeter</h1>
        <form action="/greet">
          <p>What's your name? <input type ='text' name='username'></p><br>
          <p>What's your characteristics? <input type='text' name='character'><p><br>
          How old are you? <input type='text' name='age'>
          <input type='submit' value='Continue'>
         </form>
        </body></html>
        """
@app.route('/greet')
def greet():
    username = request.args.get('username', 'World')
    character = request.args['character']
    age = request.args['age']
    if character == '':
        msg = 'You did not tell me your character.'
    if age == '':
        msg = 'You did not tell me your age.'
    else:
        msg = username +  " is " + character +  " " + age

    return """
         <html><body>
            <h1>Hello!  </h1>
            {1}
      </body></html>
      """.format(username, msg)


# Launch the Flaskpy dev server
app.run(host="localhost", debug=True)
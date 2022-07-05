from flask import Flask
app = Flask(__name__)

import requests

@app.route("/")
def hello():
    return "Hello World"

@app.route("/ping")
def ping():
    ping = 'Ping ...'

    response = ''
    try:
      response = requests.get('http://flask_ping_3:5000/peng')
    except requests.exceptions.RequestException as e:
      print('\n Uuuupssss')
      return 'Pi ...\n'

    return "Ping2 ... " + response.text + ' \n'

@app.route("/pong")
def pong():
    return 'Pong2!!!!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=1)

from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/getGoodBoi')
def goodBoi():
    url = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url).json()
    return jsonify(response)

if __name__ == "__main__":
    app.run()
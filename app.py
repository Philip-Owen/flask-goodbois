from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('base.html')

@app.route('/getGoodBoi')
def goodBoi():
    url = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url).json()
    return jsonify(response)

if __name__ == "__main__":
    app.run()
from flask import Flask,render_template,request
import time
from datetime import datetime
import os

app = Flask(__name__)
import json

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/data')
def data():
	arr = []
	arr.append([int(time.time()) * 1000, 100])
	return json.dumps(arr)

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=9092, debug=True)



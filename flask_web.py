from flask import Flask,render_template,request
import time
import os
import getops
import sys, getopt
import getargs
import json

app = Flask(__name__)

host, port, password = getargs.getargs(sys.argv)
conn = getops.connect(host, port, password)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/data')
def data():
	arr = []
	ops = getops.getkey(conn)
	arr.append([int(time.time()) * 1000, int(ops)])
	return json.dumps(arr)

if __name__ == '__main__':
	app.run(host='localhost', port=9092, debug=True)



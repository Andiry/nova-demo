from flask import Flask,render_template,request
import time
import os
import getops
import sys, getopt
import getargs
import json
import random

app = Flask(__name__)

host, port, password = getargs.getargs(sys.argv)
conn = getops.connect(host, port, password)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/data')
def data():
	arr = []
	arr.append([])
	arr.append([])
	ops = getops.getkey(conn)
	arr[0].append([int(time.time()) * 1000, random.uniform(1, 1000)])
	#arr[0].append([int(time.time()) * 1000, float(ops)])
	arr[1].append([int(time.time()) * 1000, random.uniform(1, 1000)])
	#arr[1].append([int(time.time()) * 1000, float(ops) * 10])
	return json.dumps(arr)

if __name__ == '__main__':
	app.run(host='132.239.95.31', port=80, debug=False)



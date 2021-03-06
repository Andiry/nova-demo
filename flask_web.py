from flask import Flask,render_template,request
import time
import os
import getops
import sys, getopt
import getargs
import json
import random

app = Flask(__name__)

fs, host, port, password = getargs.getargs(sys.argv)
conn = getops.connect(host, port, password)

# Set initial values
conn.set('Ext4-datajournal', '0')
conn.set('Ext4-DAX', '0')
conn.set('NOVA', '0')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/data')
def data():
	arr = []
	arr.append([])
	arr.append([])
	arr.append([])
	ops = getops.getkey(conn, 'Ext4-datajournal')
	ops1 = getops.getkey(conn, 'Ext4-DAX')
	ops2 = getops.getkey(conn, 'NOVA')
#	arr[0].append([int(time.time()) * 1000, random.uniform(1, 1000)])
	arr[0].append([int(time.time()) * 1000, float(ops)])
	arr[1].append([int(time.time()) * 1000, float(ops1)])
	arr[2].append([int(time.time()) * 1000, float(ops2)])
	return json.dumps(arr)

if __name__ == '__main__':
	app.run(host='localhost', port=9092, debug=False)



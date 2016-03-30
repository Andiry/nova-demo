#!/usr/bin/python

import re
import sys
import os
import time
import redis
import getargs

def connect(host1, port1, password1):
	conn = redis.Redis(host=host1, port=port1, db=0, password=password1)
	return conn

def setkey(conn, ops):
	conn.set('ops', ops)

def getoutput():
	with open('/root/demo-nova/log') as f:
		f.seek(-2, 2)
		while f.read(1) != b'\n':
			f.seek(-2, 1)
		last = f.readline()
		array = last.split()
		if array[1] == 'IO' and array[2] == 'Summary:':
			ops = array[5]
		else:
			print(array[0])
			ops = 0
	print ops
	return ops

def main():
	host, port, password = getargs.getargs(sys.argv)
	conn = connect(host, port, password)

	while True:
		time.sleep(2)
		output = getoutput()
		setkey(conn, output)

main()

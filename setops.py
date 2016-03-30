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
	conn.set('ops', int(ops))

def getoutput():
	with open('/proc/meminfo') as f:
		total = int(f.readline().split()[1])
		free = int(f.readline().split()[1])
		buffers = int(f.readline().split()[1])
		cache = int(f.readline().split()[1])
	mem_inuse = total - free - buffers - cache
	print mem_inuse / 1024

def main():
	host, port, password = getargs.getargs(sys.argv)
	conn = getops.connect(host, port, password)

	while True:
		time.sleep(2)
		output = getoutput()
		setkey(conn, output)

main()

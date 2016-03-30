#!/usr/bin/python

import re
import sys
import os
import time
import redis

def getkey():
	r = redis.Redis(host='127.0.0.1', port=6379, db=0)
	r.set('123', '789')
	print r.get('123')

def main():
	getkey()

main()

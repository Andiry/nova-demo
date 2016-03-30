#!/usr/bin/python

import re
import sys
import os
import time
import redis

def connect(host1, port1, password1):
	conn = redis.Redis(host=host1, port=port1, db=0, password=password1)
	return conn

def getkey(conn):
	return conn.get('ops')


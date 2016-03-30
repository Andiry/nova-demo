#!/usr/bin/python

import re
import sys
import os
import time

def getMem():
	with open('/proc/meminfo') as f:
		total = int(f.readline().split()[1])
		free = int(f.readline().split()[1])
		buffers = int(f.readline().split()[1])
		cache = int(f.readline().split()[1])
	mem_inuse = total - free - buffers - cache
	print mem_inuse / 1024

def main():
	while True:
		time.sleep(1)
		getMem()

main()

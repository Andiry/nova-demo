import sys, getopt

def usage():
	print("Usage: --host=HOST --port=PORT --password=PASSWORD")

def getargs(argv):
	opts, args = getopt.getopt(argv[1:], "h", ["host=", "port=", "password=", "help"])

	host=""
	port=""
	password=""

	for op, value in opts:
		if op == "--host":
			host = value
		elif op == "--port":
			port = value
		elif op == "--password":
			password = value
		elif op == "-h" or op == "--help":
			usage()
			sys.exit()

	if host == "" or port == "" or password == "":
		usage()
		sys.exit()

	return host, port, password


import sys, getopt

def usage():
	print("Usage: --fs=FS --host=HOST --port=PORT --password=PASSWORD")

def getargs(argv):
	opts, args = getopt.getopt(argv[1:], "h", ["fs=", "host=", "port=", "password=", "help"])

	fs=""
	host=""
	port=""
	password=""

	for op, value in opts:
		if op == "--fs":
			fs = value
		elif op == "--host":
			host = value
		elif op == "--port":
			port = value
		elif op == "--password":
			password = value
		elif op == "-h" or op == "--help":
			usage()
			sys.exit()

	if fs == "" or host == "" or port == "" or password == "":
		usage()
		sys.exit()

	return fs, host, port, password


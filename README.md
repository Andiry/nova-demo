# NOVA Demo

## Introduction

This is a web demo to show real time throughput of filebench on NOVA.

The demo consists of two parts: server and client. On the server side, it runs filebench on NOVA and reads real-time throughput, writing to Redis. On the client side, it gets the throughput number from Redis and shows in a web interface.


## How to run

On the server side, follow the steps:

1. Start a Redis server
2. Run filebench with `psrun` command and write the output to a log file:
    ```
    # filebench -f fileserver.f | tee /root/demo-nova/log
    ```
3. Read the output from the file and write to Redis server:
    ~~~
    # python setops.py --host=HOST --port=PORT --password=PASSWORD
    ~~~

On the client side, follow the steps:

1. Read the output and show in the web server:
    ~~~
    # python flask_web.py --host=HOST --port=PORT --password=PASSWORD
    ~~~
2. Open the web interface and monitor the read time throughput:

[http://localhost:9092](http://localhost:9092)

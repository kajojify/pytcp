pytcp
=====
About
-----
It is simple asyncronous Python 3 TCP server. 


How to run
----------
The application is on the development stage and it isn't installable for now.

But don't be upset, you can run the app in the following way.

Clone this repository. Then go to the repository directory.


Run the script:
```
sudo python3 start_pytcp.py
```

Usage
-----
Client:
```
~$ netcat 127.0.0.1 8888
Hey you! 
9
```
Server:
```
~/pytcp$ sudo python3 start_pytcp.py 
2017-04-11 15:11:01,668 (root) Welcome to pytcp v0.1.0! Press Ctrl+C to stop the server.
2017-04-11 15:11:01,669 (pytcp.server) Serving on 8888 port.
2017-04-11 15:11:43,220 (pytcp.server) Accepted connection from 127.0.0.1:39670.
2017-04-11 15:11:50,837 (pytcp.server) Received 6 bytes from 127.0.0.1:39670.
```
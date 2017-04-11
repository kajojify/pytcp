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
~$ netcat 127.0.0.1 123
abcd
5
```
Server:
```
~/pytcp$ sudo python3 start_pytcp.py -p 123 
2017-04-11 15:15:44,739 (root) Welcome to pytcp v0.1.0! Press Ctrl+C to stop the server.
2017-04-11 15:15:44,740 (pytcp.server) Serving on 123 port.
2017-04-11 15:15:52,117 (pytcp.server) Accepted connection from 127.0.0.1:35586.
2017-04-11 15:15:56,096 (pytcp.server) Received 5 bytes from 127.0.0.1:35586.
```

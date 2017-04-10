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
2017-04-11 02:00:52,718 Listening established on 127.0.0.1:8888
2017-04-11 02:01:21,421 Accepted connection from 127.0.0.1:44842
2017-04-11 02:01:34,858 Received 9 bytes from the client.
```
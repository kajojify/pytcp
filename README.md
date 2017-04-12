pytcp
=====
About
-----
It is simple asyncronous Python 3 TCP server. 


How to install
--------------

Clone this repository. Then go to the repository directory.


Run the script setup.py:
```
sudo python3 setup.py install
```

How to use
----------
**Server:**
```
~/pytcp$ sudo pytcp -p 123 
2017-04-11 15:15:44,739 (root) Welcome to pytcp v0.1.0! Press Ctrl+C to stop the server.
2017-04-11 15:15:44,747 (pytcp.misc) Privileges dropped, running as nobody/nogroup.
2017-04-11 15:15:44,748 (pytcp.server) Serving on 123 port.
2017-04-11 15:15:52,117 (pytcp.server) Accepted connection from 127.0.0.1:35586.
2017-04-11 15:15:56,096 (pytcp.server) Received 5 bytes from 127.0.0.1:35586.
```

**Client:**
```
~$ netcat 127.0.0.1 123
abcd
5
```
.


pytcp
=====
About
-----
This is simple, echo-like, asynchronous Python 3 TCP server.
 
It accepts some bytes from connected client until receiving CRLF and then sends back the number of received bytes. After this it terminates the connection to the client.

**pytcp** writes useful information to the log file: connection state (accepted or terminated), client socket address, number of received bytes and other pytcp related info.

It also shows all this information on the terminal.

How to install
--------------

Clone this repository. Then go to the repository directory.

Run the script setup.py:
```
sudo python3 setup.py install
```

How to use
----------
```~$ sudo pytcp``` - running pytcp. 

You can specify some parameters for **pytcp**. 

pytcp [-h] [-p PORT] [-l LOGFILE]

```-p --port``` - port, which **pytcp** listens on. 
Default port is 8888.
 
```-l --logfile``` - the path to the custom logfile. 
Default logfile is "pytcp.log". It will be created in the directory, where **pytcp** is launched. 

**Server:**
```
~/pytcp$ sudo pytcp -p 123 
2017-04-16 01:39:53,393 (root) Started logging to file - /home/kajoj/pytcp/pytcp.log
2017-04-16 01:39:53,393 (root) Welcome to pytcp v0.1.0! Press Ctrl+C to stop the server.
2017-04-16 01:39:53,394 (pytcp.server) Serving on 123 port.
2017-04-16 01:39:53,395 (pytcp.misc) Privileges dropped, running as nobody/nogroup.
2017-04-16 01:40:34,086 (pytcp.server) Accepted connection from 192.168.0.100:35708.
2017-04-16 01:40:45,284 (pytcp.server) Received 11 bytes from 192.168.0.100:35708.
2017-04-16 01:40:45,284 (pytcp.server) Connection with 192.168.0.100:35708 was terminated.
```

By the way, you don't have to run **pytcp** as root, if you use the number of port > 1023.

**Client:**
```
~$ netcat 127.0.0.1 123
pytcp abcd
11
```

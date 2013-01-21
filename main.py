#!/usr/bin/python
#-*-coding: utf-8-*-

#
# simple ncid-client
#


import socket
import re
import pynotify
import os
import time

def incomingCall(call):
	nmbr = re.search(r"(NMBR\*)([\w]*)(\*)", call).group(2)
	return nmbr

def main():
	# NCID-Server (Vodafone EasyBox 602)
	host = "192.168.2.1"
	port = 3333
	
	s = socket.socket()
	try:
		s.connect((host, port))
		n = pynotify.Notification("")
		pynotify.init("liveNCID")
		while True:
			data = s.recv(1024)
			if data[:4] == "CID:":
				n.update("Incoming Call", incomingCall(data[:-1]), os.path.abspath("./icons/phone_white.png"))
				n.show()
				time.sleep(20)
				n.close()
	except:
		pass
	finally:
		s.close()


if __name__ == "__main__":
	main()

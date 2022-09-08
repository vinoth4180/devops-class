# An example script to connect to Google using socket
# programming in Python
# import socket # for socket
# import sys
#
# try:
# 	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	print ("Socket successfully created")
# except socket.error as err:
# 	print ("socket creation failed with error %s" %(err))
#
# # default port for socket
# port = 801
#
# try:
# 	host_ip = socket.gethostbyname('www.google.com')
# 	print(host_ip)
# 	s.connect((host_ip, port))
# 	print(f"the socket has successfully connected to google and its ip={host_ip}")
# except socket.gaierror:
# 	# this means could not resolve the host
# 	print ("there was an error resolving the host")
# 	sys.exit()

import socket
ipadd=socket.gethostbyname('DESKTOP-H3B0OU5')
print(ipadd)
hostname=socket.gethostbyaddr(ipadd)
print(hostname)
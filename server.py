import os
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

def clear_buffer_cache():
	system('free -g')
	system('sync')
	system("sudo sed -n 's/0/3/w /proc/sys/vm/drop_caches' /proc/sys/vm/drop_caches")
	system('sync')
	system("sudo sed -n 's/3/0/w /proc/sys/vm/drop_caches' /proc/sys/vm/drop_caches")
	system('free -g')

def is_even(n):
	return n%2 == 0

server = SimpleXMLRPCServer(('0.0.0.0', 8888))
print 'Listening on port 8888...'
server.register_function(clear_buffer_cache, 'clear_buffer_cache')
server.register_function(is_even, 'is_even')
server.serve_forever()


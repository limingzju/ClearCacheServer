import xmlrpclib

proxy = xmlrpclib.ServerProxy('http://localhost:8888')

print '3 is even: %s' %str(proxy.is_even(3))

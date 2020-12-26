from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer
address = ("0.0.0.0", 23)

authorizer = DummyAuthorizer()
authorizer.add_user("pi","12345", "/home/myfiles/", perm="elradfmwMT")


handler = FTPHandler
handler.authorizer = authorizer

server = servers.FTPServer(address, FTPHandler)
server.serve_forever()

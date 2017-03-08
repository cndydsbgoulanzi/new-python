#! /usr/bin/env python
#一个小型服务器
import socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
while True:
    c.addr = s.accept()
    print 'Got connection from', addr
    c.send('Thank you for conncting')
    c.close()

#一个小型客户机
import socket

s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host, port))
print s.recv(1024)

#使用分叉技术的服务器
from SocketServer import TCPServer, ForkingMixIn, streamRequestHandler

class Server(ForkingMixIn,TCPServer): pass

class Handler(streamRequestHandler):

    def handler(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        self.wfile.write('Thank you for connecting')

server = Server(('', 1234), Handler)
server.serve_forever()

#使用线程处理的服务器
from SocketServer import TCPServer, ThreadingMixIn, streamRequestHandler

class Server(ThreadingMixIn,TCPServer): pass

class Handler(streamRequestHandler):

    def handler(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        self.wfile.write('Thank you for connecting')

server = Server(('', 1234), Handler)
server.serve_forever()

#使用了select的简单服务器
import select, socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
inputs = [5]
while True:
    rs, ws,es = select.select(inputs, [], [])
    for r in rs:
        if r is s:
            c, addr = s.accept()
            print 'Got connection from', addr
            inputs.append(c)
        else:
            try:
                data = r.recv(1024)
                disconnected = nat data
            except socket.error:
                disconnected = True
            if disconnected:
                print r.getpeername(), 'disconnected'
                inputs.remove(r)
            else:
                print data

#使用poll的简单服务器
import select, socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

fdmap = {s.fileno(): s}


s.listen(5)
p = select.poll()
p.register(s)
while True:
    events = p.poll()
    for fd, event in events:
        if fd = s.fileno():
            c, addr = s.accept()
            print 'Got connection from', addr
            p.register(c)
            fdmap[c, fileno()] = c
        elif event & select.POllIN:
            data = fdmap[fd].recv(1024)
            if not data:
                print fdmap[fd].getpeername(), 'disconnected'
                p.unrigister(fd)
                del fdmap[fd]
        else:
            print data

#使用Twisted的简单服务器
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

class SimpleLogger(Protocol):

    def connectionMade(self):
        print 'Got connection from', self.transport.client
    def connectionLost(self, reason):
        print self.transport.client, 'disconnected'
    def dataReceived(self, data):
        print data

factory = Factory()
factory.protocol = SimpleLogger

reactor.listenTCP(1234, factory)
reactor.run()

#使用LineRecevier协议改进的记录服务器
from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineRecevier


class SimpleLogger(LineRecevier):

    def connectionMade(self):
        print 'Got connection from', self.transport.client
    def connectionLost(self, reason):
        print self.transport.client, 'disconnected'
    def LineRecevier(self, data):
        print data

factory = Factory()
factory.protocol = SimpleLogger

reactor.listenTCP(1234, factory)
reactor.run()


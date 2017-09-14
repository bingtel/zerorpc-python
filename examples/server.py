# -*- coding: utf-8 -*-

import zerorpc

class Server(object):
    def __init__(self):
        super(Server, self).__init__()
        self.data = {str(i): i for i in range(100)}
        self.data2 = None

    def getObj(self):
        print('get data')
        return self.data

    def sendObj(self, data):
        print('send data')
        self.data2 = data


s = zerorpc.Server(Server())
s.bind('tcp://0.0.0.0:5000')
s.run()

import http.client
from queue import Queue




def get(queue, msg):
        q = Queue()
        host = 'localhost'
        connection = http.client.HTTPConnection(host, 8989)
        connection.request("GET", '/')
        resp = connection.getresponse()
        msg = resp.read()
        print(msg.decode(encoding='utf-8'))






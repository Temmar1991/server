from http.server import HTTPServer, BaseHTTPRequestHandler
from queue import Queue, Full


class HttpServerImpl(BaseHTTPRequestHandler):



    def set_headers(self):
        self.send_response(code=200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_GET(self):
        q = Queue()
        self.set_headers()
        item = q.get()
        self.wfile.write(bytes(item, 'utf-8'))

    def do_POST(self):
        q = Queue(maxsize=10)
        self.set_headers()
        print("POST method")
        content_len = int(self.headers['Content-Length'])
        param = self.rfile.read(content_len)
        if q.qsize() != q.maxsize:
            q.put(param)
        else:
            raise Full



def run():
    server_address = ('127.0.0.1', 8989)
    httpd = HTTPServer(server_address, HttpServerImpl)
    print("Served for requests...")
    httpd.serve_forever()


if __name__ == '__main__':
    run()

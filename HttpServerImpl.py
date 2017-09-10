from http.server import HTTPServer, BaseHTTPRequestHandler
from queue import Queue, Full, Empty

q = Queue(10)


class HttpServerImpl(BaseHTTPRequestHandler):

    def set_headers(self):
        self.send_response(code=200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self.set_headers()
        try:
            item = q.get(False)
            self.wfile.write(item)
        except Empty:
            print('Empty queue')


    def do_POST(self):
            # Doesn't do anything with posted data
            content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
            post_data = self.rfile.read(content_length)  # <--- Gets the data itself
            self.set_headers()
            try:
                q.put(post_data, block=False)
            except Full:
                print('Queue is full')


def run():
    server_address = ('127.0.0.1', 8989)
    httpd = HTTPServer(server_address, HttpServerImpl)
    print("Served for requests...")
    httpd.serve_forever()


if __name__ == '__main__':
    run()

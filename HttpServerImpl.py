from http.server import HTTPServer, BaseHTTPRequestHandler


class HttpServerImpl(BaseHTTPRequestHandler):

    def set_headers(self):
        self.send_response(code=200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self.set_headers()
        message = "Hello world!"
        self.wfile.write(bytes(message,encoding='utf-8'))


def run():
    server_address = ('127.0.0.1', 8989)
    httpd = HTTPServer(server_address, HttpServerImpl)
    print("Served for requests")
    httpd.serve_forever()


run()

from http.server import HTTPServer, BaseHTTPRequestHandler


class HttpServerImpl(BaseHTTPRequestHandler):

    def set_headers(self):
        self.send_response(code=200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()


    def do_GET(self):

        self.set_headers()
        self.wfile.write('<h1>Hello world!</h1>')




def run(server_class=HTTPServer, handler_class=HttpServerImpl, port=8989):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("Served for requests")
    httpd.serve_forever()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

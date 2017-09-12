from http.server import HTTPServer, BaseHTTPRequestHandler
from queue import Queue, Full, Empty
import argparse
import time
import json


queues = {q: Queue(10) for q in range(0, 11)}
print(queues)


class HttpServerImpl(BaseHTTPRequestHandler):

    def set_headers(self):
        self.send_response(code=200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        decode_data = data.decode(encoding='utf-8')
        print(data)
        request_json_data1 = json.loads(decode_data)
        queue = request_json_data1['queue']
        num_queue = int(queue)
        print(queue)
        self.set_headers()
        try:
            item = queues[num_queue].get(False)
            byte_item = str.encode(item)
            self.wfile.write(byte_item)
        except Empty:
            print('Empty queue')

    def do_POST(self):
            # Doesn't do anything with posted data
            content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
            post_data = self.rfile.read(content_length)
            decode_post = post_data.decode(encoding='utf-8')
            # print(decode_post)  # <--- Gets the data itself
            request_json_data = json.loads(decode_post)
            message = request_json_data['message']
            num_queue = request_json_data['queue']
            num_queue_number = int(num_queue)
            print(message)
            print(num_queue)
            # print(request_json_data['queue'])
            self.set_headers()
            try:
                queues[num_queue_number].put(message, block=False)

            except KeyError:
                print('There is no such queue')
            except Full:
                print('Queue is full')


def server_paeser():
    parser = argparse.ArgumentParser(description='server')
    parser.add_argument('--port', required=True, help='Server port to run', type=int)
    return parser


def run(namespace):

    server_address = ('127.0.0.1', namespace.port)
    httpd = HTTPServer(server_address, HttpServerImpl)
    print("Served for requests...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
        httpd.server_close()
        print(time.asctime(), "Server Stops ")


if __name__ == '__main__':
    parse = server_paeser()
    namespace = parse.parse_args()
    run(namespace)

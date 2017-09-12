import http.client
import argparse
import requests
import sys


def connect(host, port):
    con = http.client.HTTPConnection(host, port)
    return con


def do_get(namespace=None):
        connection = connect('localhost', 8989)
        connection.request("GET", '/')
        resp = connection.getresponse()
        msg = resp.read()
        namespace.queue = resp.read()
        if not msg:
            print('Queue empty')
        else:
            print("The item is {}".format(msg.decode(encoding='utf-8')))


def do_post(namespace):
    req = requests.post('http://127.0.0.1:8989', data={'message': namespace.message})
    print(req.status_code, req.reason)


def cli():
        parser = argparse.ArgumentParser(description='Parse command parameters')
        subparsers = parser.add_subparsers(dest='command', help='List of commands')
        # GET command
        get_parser = subparsers.add_parser('get', help='Get message from the queue')
        get_parser.add_argument('--queue', nargs='?', default='0')
        # parser.set_defaults(func=get)
        # POST command
        post_parser = subparsers.add_parser('post', help='Put message to queue')
        post_parser.add_argument('--message', required=True, help='Message text, mandatory')
        post_parser.add_argument('--queue', nargs='?', default='0', help='''queue alias, may be number
        from 0 to 10000''')
        # parser.set_defaults(func=post)

        return parser
if __name__ == '__main__':
        Parser = cli()
        namespace = Parser.parse_args(sys.argv[1:])
        print(namespace)
        if namespace.command == "get":
            do_get(namespace)
        elif namespace.command == "post":
            do_post(namespace)
        else:
            print("Something goes wrong")








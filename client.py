import http.client
import argparse
import requests


def connect(host, port):
    con = http.client.HTTPConnection(host, port)
    return con


def get():
        connection = connect('localhost', 8989)
        connection.request("GET", '/')
        resp = connection.getresponse()
        msg = resp.read()
        # queue = resp.read()
        if not msg:
            print('Queue empty')
        else:
            print("The item is {}".format(msg.decode(encoding='utf-8')))


def post(arg):
    req = requests.post('http://127.0.0.1:8989', data={'message': arg})
    print(req.status_code, req.reason)


def cli():
        parser = argparse.ArgumentParser(description='Parse command parameters')
        subparsers = parser.add_subparsers(help='List of commands')
        # GET command
        get_parser = subparsers.add_parser('get', help='Get message from the queue')
        get_parser.add_argument('--queue', action='store', default='0')
        parser.set_defaults(func=get)
        # POST command
        post_parser = subparsers.add_parser('post', help='Put message to queue')
        post_parser.add_argument('--message', action='store', required=True, help='Message text, mandatory')
        post_parser.add_argument('--queue', action='store', default='0', help='''queue alias, may be number
        from 0 to 10000''')
        # parser.set_defaults(func=post)

        return parser.parse_args()
if __name__ == '__main__':
        args = cli()
        #args.func(args)
        print(args)
        message = 'test'
        post(message)
        get()







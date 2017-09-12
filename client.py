import argparse
import requests
import json
import sys
# Port must be known
url = 'http://127.0.0.1:9000'

def do_get(namespace=None):
        data = {'queue': namespace.queue}
        headers = {'content-type': 'application/json'}
        # res = connection.request('GET', '/', body=namespace.queue)
        res = requests.get(url, data=json.dumps(data), headers=headers)
        msg = res.text
        # print(msg)
        if not msg:
            print('Queue empty')
        else:
            print("The item is {}".format(msg))


def do_post(namespace):
    headers = {'content-type': 'application/json'}
    data = {'message': namespace.message, 'queue': namespace.queue}
    req = requests.post(url, data=json.dumps(data), headers=headers)
    # print(req.status_code, req.reason)
    print('[Done]')


def cli():
        parser = argparse.ArgumentParser(description='Simple transfer message program')
        subparsers = parser.add_subparsers(dest='command', help='List of commands')
        # GET command
        get_parser = subparsers.add_parser('get', help='Get message from the queue')
        get_parser.add_argument('--queue', nargs='?', default='0', help="""queue alias, is number from 0
        to 10. For example --queue=3""")
        # parser.set_defaults(func=get)
        # POST command
        post_parser = subparsers.add_parser('post', help='Put message to queue')
        post_parser.add_argument('--message', required=True, help='Message text, mandatory')
        post_parser.add_argument('--queue', nargs='?', default='0', help='''queue alias, is number from 0
        to 10. For example --queue=3''')
        # parser.set_defaults(func=post)

        return parser
if __name__ == '__main__':
        Parser = cli()
        namespace = Parser.parse_args(sys.argv[1:])
        # print(namespace)
        if namespace.command == "get":
            do_get(namespace)
        elif namespace.command == "post":
            do_post(namespace)
        else:
            print("Something goes wrong")








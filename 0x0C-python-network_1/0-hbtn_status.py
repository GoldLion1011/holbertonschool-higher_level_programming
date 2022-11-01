#!/usr/bin/python3
""" Fetches the address https://intranet.hbtn.io/status """
from urlib import request


if __name__ == "__main__":
    request = request.Request('https://intranet.hbtn.io/status')
    with request.urlopen(request) as page:
        page = page.read()
        print('Body response:')
        print('\t- type: {}'.format(type(page)))
        print('\t- content: {}'.format(page))
        print('\t- utf8 content: {}'.format(page.decode('utf-8')))

#!/usr/bin/python3
""" Script that takes in a URL and an email address,
sends a POST request to the passed URL with the email parameter,
and finally displays the body of the response """
import requests
import sys


if __name__ == "__main__":
    print(requests.post(sys.argv[1], data={'email': sys.argv[2]}).text)

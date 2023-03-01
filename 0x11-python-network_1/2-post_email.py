#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter
"""


import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    with urllib.request.urlopen(sys.argv[1], data) as r:
        print(r.read().decode('utf-8'))

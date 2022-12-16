#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
"""
import urllib.request
import sys

if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        print(response.getheader("X-Request-Id"))

#!/usr/bin/python3
""" Open a website and display content"""
from urllib import request

if __name__ == "__main__":
    """ main """
    url = "https://intranet.hbtn.io/status"
    req = request.Request(url)
    req.add_header('cfclearance', 'true')

    with request.urlopen(req) as response:
        body = response.read()
        utf8_content = body.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", utf8_content)

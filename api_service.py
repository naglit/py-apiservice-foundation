import os, sys
import requests
import json

def main():
    send_message()

def send_message():
    url = "https://chatwork.com/"
    headers = { 'X-ChatWorkToken': "" }
    params = { 'body': "body" }

    # send a request
    resp = requests.post(url,
        headers=headers,
        params=params)

if __name__ == "__main__":
    main()

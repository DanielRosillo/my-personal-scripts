#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python3
from multiprocessing import Pool
import requests
import json
import time

url = "http://192.168.2.4:5101/"

def f(i):
    payload = {
        "name": "satoshi nakamoto",
        "password": "xyz",
        "email": f"satoshi+{i}@sample.xyz"
    }

    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.13.0",
        'Accept': "*/*",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(i, response.text) 
    
    return response


def main(number_of_request):
    p = Pool(16)
    return p.map(f, range(number_of_request))


if __name__ == '__main__':
    start_time = time.time()
    number_of_request = 1000000
    print(f"[+] {number_of_request} Requests")
    result = str(main(number_of_request))
    print("--- %s seconds ---" % (time.time() - start_time))

    success = result.count("20")
    server = result.count("50")
    error = result.count("40")

    print("success: ", success)
    print("server errors: ", server)
    print("client errors: ", error)
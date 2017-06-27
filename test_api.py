import requests
import json

def make_request(method, *args):
    url = "http://localhost:5000/api/"
    headers = {'content-type': 'application/json'}
    params = args if args is not None else []
    payload = { "method": method, "params": params, "jsonrpc": "2.0", "id": 0 }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if (response.ok):
        return response.json()
    else:
        return response.text

if __name__ == '__main__':
    make_request("ping")


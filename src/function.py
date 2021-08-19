import requests
import time
import json
from datetime import datetime
from dateutil.parser import parse

BASE_URL = 'https://industrial.api.ubidots.com/api/v1.6/devices/'
VERSION = 'v1.6'

def main(args):

    if not 'token' in args['_parameters']:
        print("[ERROR] Ubidots token not specified")
        return {"status":"error"}
    else:
        print("[INFO] args:", json.dumps(args))
    
        token = args['token']
        device_label = "demo_sigfox"
        payload =json.dumps(args)
        response = ubidots_request(device_label, payload, token)
        return response
    

def ubidots_request(device_label, payload, token):
    BASE_URL = 'https://industrial.api.ubidots.com/api/v1.6/devices/'

    headers = {
        "X-Auth-Token": token,
    "Content-Type": "application/json",
    }
    response = requests.post(BASE_URL+device_label, headers=headers, data = payload)
    return response




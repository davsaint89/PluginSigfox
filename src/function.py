import requests
import json
from control import setup
from user_code import format_payload



BASE_URL = 'https://industrial.api.ubidots.com'

def main(args):
    setup(args)
    if not args['_parameters'].get('token'):
        print("[ERROR] Ubidots token not specified")
        return {"status":"error"}
    else:
        print("[INFO] args:", json.dumps(args))
    
        token = args['_parameters'].get('token')
        device_type = args['_parameters'].get('device_type')
        args.pop('_parameters')
        #args.pop("token")
        device_label = args['device_id']
        args.pop("device_id")
        payload = json.dumps(format_payload(args)) 

        print(payload)
        response = ubidots_request(device_label, device_type, payload, token)
        print(response, response.json())
        return response.json()
    

def ubidots_request(device_label, device_type, payload, token):
    
    url = BASE_URL + '/api/v1.6/devices/' + device_label + '/?type=' + device_type
    headers = {
        "X-Auth-Token": token,
        "Content-Type": "application/json",
    }
    response = requests.post(url, headers=headers, data = payload)
    return response


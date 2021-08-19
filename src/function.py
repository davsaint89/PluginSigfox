import requests
import json


def main(args):

    if not args['_parameters'].get('token'):
        print("[ERROR] Ubidots token not specified")
        return {"status":"error"}
    else:
        print("[INFO] args:", json.dumps(args))
    
        token = args['_parameters']['token']
        args.pop('_parameters')
        #args.pop("token")
        device_label = args['device_id']
        args.pop("device_id")
        payload =json.dumps(args)
        #print(payload)
        response = ubidots_request(device_label, payload, token)
        print(response, response.json())
        return response.json()
    

def ubidots_request(device_label, payload, token):
    BASE_URL = 'https://industrial.api.ubidots.com/api/v1.6/devices/'

    headers = {
        "X-Auth-Token": token,
        "Content-Type": "application/json",
    }
    response = requests.post(BASE_URL+device_label, headers=headers, data = payload)
    return response




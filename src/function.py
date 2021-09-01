import requests
import json
from user_code import format_payload



BASE_URL = 'https://industrial.api.ubidots.com'

def main(args):

    if not args['_parameters'].get('token'):
        print("[ERROR] Ubidots token not specified")
        return {"status":"error"}
    else:
        print("[INFO] args:", json.dumps(args))
    
        token = args['_parameters'].get('token')

        if args['_parameters'].get('device_type')!= "": # here send data decoded to a device type

            device_type = args['_parameters'].get('device_type')
            args.pop('_parameters')
            #args.pop("token")
            device_label = args['device_id']
            args.pop("device_id")
            payload = json.dumps(format_payload(args)) 

            print(payload)
            response = ubidots_request_dev_type(device_label, device_type, payload, token)
            print(response, response.json())
            return response.json()
        
        else:  # if no device type assigned it sends data to a device
            device_label = args['device_id']
            args.pop("device_id")
            payload = json.dumps(format_payload(args))
            response = ubidots_request_device(payload, device_label, token)
            print(response, response.json())
            return response.json()
    
# updates a device type
def ubidots_request_dev_type(device_label, device_type, payload, token):
    
    url = BASE_URL + '/api/v1.6/devices/' + device_label + '/?type=' + device_type
    headers = {
        "X-Auth-Token": token,
        "Content-Type": "application/json",
    }
    response = requests.post(url, headers=headers, data = payload)
    return response

# updates a device
def ubidots_request_device(data, device_label, token):
    url = BASE_URL + '/api/v1.6/devices/' + device_label
    headers = {
        "X-Auth-Token": token,
        "Content-Type": "application/json",
    }
    response = requests.post(url,headers=headers, data=json.dumps(data))
    return response


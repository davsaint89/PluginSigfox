import requests
import json
import time
from user_code import format_payload


BASE_URL = 'https://industrial.api.ubidots.com'

def main(args):
    """
    Main function
    """
    token = args['_parameters'].get('token')
    device_type = args['_parameters'].get('device_type')

    if not token:
        print("[ERROR] Ubidots token not specified")
        return {"status":"error"}
    else:
        print("[INFO] args:", json.dumps(args))
        if device_type!= "": 
            device_label = args['device_id']
            args.pop('_parameters')
            """ gets payload from user_code.py """
            payload = format_payload(args)
            print(payload)
            response = ubidots_request_dev_type(device_label, device_type, payload, token)
            print(response, response.json())
            return response.json()
        else:  
            device_label = args['device_id']
            args.pop("device_id")
            payload = format_payload(args)
            response = ubidots_request_device(payload, device_label, token)
            print(response, response.json())
            return response.json()
    
 
def ubidots_request_dev_type(device_label, device_type, payload, token):
    """
    Updates a device under a device type
    """
    url = BASE_URL + '/api/v1.6/devices/' + device_label + '/?type=' + device_type
    headers = {
        "X-Auth-Token": token,
        "Content-Type": "application/json",
    }
    response = create_request(url, headers, attempts=5,request_type='post',data=payload)
    return response


def ubidots_request_device(data, device_label, token):
    """
    Updates a device
    """
    url = BASE_URL + '/api/v1.6/devices/' + device_label
    headers = {
        "X-Auth-Token": token,
        "Content-Type": "application/json",
    }
    response = create_request(url, headers, attempts=5, data=data, request_type='post')
    return response


def create_request(url, headers, attempts, request_type, data=None):
    """
    Makes an API request to the server
    """
    request_func = getattr(requests, request_type)
    kwargs = {"url": url, "headers": headers}
    if request_type == "post" or request_type == "patch":
        kwargs["json"] = data
    try:
        req = request_func(**kwargs)
        status_code = req.status_code
        time.sleep(1)
        while status_code >= 400 and attempts < 5:
            req = request_func(**kwargs)
            status_code = req.status_code
            attempts += 1
            time.sleep(1)
        return req
    except Exception as e:
        print("[ERROR] There was an error with the request, details:")
        print(e)
        return None
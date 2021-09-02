import requests
import json
import time
from user_code import format_payload

BASE_URL = 'https://industrial.api.ubidots.com'

def main(args):
    """
    Main function
    """
    print("[INFO] args:", json.dumps(args))
    token = args['_parameters'].get('token')
    device_type = args['_parameters'].get('device_type')
    args.pop('_parameters')

    if not token:
        print("[ERROR] Ubidots token not specified")
        return {"status":"error"}
    
    device_label = args['device_id']
    payload = format_payload(args)
    print(payload)
    
    url = f'{BASE_URL}/api/v1.6/devices/{device_label}'
    if device_type is not None and device_type != "":
        url = f'{url}?{device_type}'
    
    response = ubidots_request_device(url, payload, token)
    print(response, response.json())
    return response.json()

def ubidots_request_device(url, data, token):
    """
    Updates a device
    """
    headers = {"X-Auth-Token": token,"Content-Type": "application/json",}
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
import requests
import json
from unicodedata import normalize
import re
import time

""" Global variables """

URL = "https://industrial.api.ubidots.com/api/v2.0/device_types/"
sigfox_main_color = '#0040E5'
sigfox_secondary_color = '#6C95FF'


def setup(args):
    """
    Setup function - runs when the plugin is created or edited
    """
    print("[INFO] args:", json.dumps(args))

    token = args['_parameters'].get('token')
    device_type = args['_parameters'].get('device_type')

    if not token:
        print("[ERROR] Ubidots token not specified")
        return {"status":"error"}

    elif not device_type and token:
        print("[INFO] device type not specified")
        device_type = ""

    if device_type != "":
        device_type_data = set_device_type(device_type)
        try:
            res = create_device_type(device_type_data, token)
            print(res)
            if res.status_code == 409:
                print("[INFO] A device type with this name already exists.")
            elif res.status_code == 201:
                print("[INFO] Device type created successfully.")
        except Exception as e:
            print("[INFO] Setup function ran, but could not create a device type.")
            print(e)
    else:
        print({"[INFO] No device type created"})

    return {"status":"finished"}

 
def set_device_type(device_type):
    """
    Sets a device type normalizing its name 
    """
    device_type_data = {
        'name': device_type,
        'label': normalize_label(device_type),
        'deviceColor': sigfox_main_color,
        'deviceIcon': 'wifi',
        'variableColor': sigfox_secondary_color,
        'properties': [],
            'variables': []
    }
    return device_type_data


def normalize_label(label):
    """
    Normalizes a label to accepted characters
    """
    label = normalize('NFKD', label)
    label = re.sub('/[^a-z0-9-_:.]/g', '-', label)
    label = label.lower()
    return label


def create_device_type(data, token):
    """
    Creates a device_type
    """
    headers = {"X-Auth-Token": token, "Content-Type": "application/json"}
    response = create_request(URL, headers, attempts=5, request_type="post", data=data)
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



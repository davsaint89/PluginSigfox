import requests
import json
from unicodedata import normalize
import re

# global variables
URL = "https://industrial.api.ubidots.com/api/v2.0/device_types/"
tti_main_color = '#0040E5'
tti_secondary_color = '#6C95FF'

# main ffunction
def setup(args):
    """Detup function - runs when the plugin is created or edited"""
    print("[INFO] args:", json.dumps(args))
    if not args['_parameters'].get('token'):
        print("[ERROR] Ubidots token not specified")
        return {"status":"error"}

    elif not args['_parameters'].get('device_type') and args['_parameters']['token']:
        print("[INFO] device type not specified")
        device_type = ""
        token = args['_parameters']['token']

    else:
        token = args['_parameters']['token']
        device_type = args['_parameters']['device_type']

    if device_type != "":
        device_type_data = set_device_type(device_type)
        try:
            res = create_device_type(device_type_data, token, URL)
            print(res)
            if res.status_code == 409:
                print("[INFO] A device type with this name already exists.")
            elif res.status_code == 201:
                print("[INFO] Device type created successfully.")
        except:
            print("[INFO] Setup function ran, but could not create a device type.")
    else:
        print({"[INFO] No device type created"})

    return {"status":"finished"}

    
def set_device_type(device_type):
    device_type_data = {
    'name': device_type,
    'label': normalize_label(device_type),
    'deviceColor': tti_main_color,
    'deviceIcon': 'wifi',
    'variableColor': tti_secondary_color,
    'properties': [],
        'variables': []
    }
    return device_type_data

def normalize_label(label):
    label = normalize('NFKD', label)
    label = re.sub('/[^a-z0-9-_:.]/g', '-', label)
    label = label.lower()
    return label

def create_device_type(data, token, url):
    headers = {"X-Auth-Token": token, "Content-Type": "application/json"}
    response = requests.post(url,headers=headers, data=json.dumps(data))
    return response






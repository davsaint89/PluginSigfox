import requests
import time
from datetime import datetime
from dateutil.parser import parse

BASE_URL = 'https://industrial.api.ubidots.com'
VERSION = 'v1.6'

def main(args):
    if not 'token' in args['_parameters']:
        print("[ERROR]")
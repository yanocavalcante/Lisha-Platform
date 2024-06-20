#!/usr/bin/env python3

# This file is an example for creating SmartData Series in UFSC's and LISHA's
# IoT Platform, using an external JSON file.

import os, argparse, requests, json


parser = argparse.ArgumentParser(description='EPOS Serial->IoT Gateway')

required = parser.add_argument_group('required named arguments')
required.add_argument('-c', '--certificate', help='Your PEM certificate', required=True)
parser.add_argument('-u', '--url', help='Post URL', default='https://iot.lisha.ufsc.br/api/create.php')

args = vars(parser.parse_args())
URL = args['url']
MY_CERTIFICATE = (args['certificate'] + '.pem', args['certificate'] + '.key')

# External JSON file
f = open("series.json")
data_series = json.load(f)
JSON = data_series
f.close()

session = requests.Session()
session.cert = MY_CERTIFICATE

try:
    response = session.post(URL, json=JSON)
    print("SEND", str(response.status_code), str(response.text), str(response))
except Exception as e:
    print("Exception caught:", e)

#!/usr/bin/env python3

import os, argparse, requests, json


parser = argparse.ArgumentParser(description='EPOS Serial->IoT Gateway')

required = parser.add_argument_group('required named arguments')
# required.add_argument('-c', '--certificate', help='Your PEM certificate', required=True)
parser.add_argument('-u', '--url', help='Post URL', default='https://iot.lisha.ufsc.br/api/create.php')
# required.add_argument('-j', '--json', help='JSON', required=True)

args = vars(parser.parse_args())
URL = args['url']
# MY_CERTIFICATE = (args['certificate'] + '.pem', args['certificate'] + '.key')

# Utilizando linha de comando para passar o JSON
# JSON = args['json']
# JSON = json.loads(JSON)
# Comando: python3 my_post_data.py -c labeco -j '{"version": "1.1", "unit": 2224437540, "value": 25, "uncertainty": 321313121, "x": 741868770, "y": 679816011, "z": 25285, "t": 1717612246019815, "dev": 0}'


# # Utilizando arquivo externo
f = open("example.json")
data_series = json.load(f)
JSON = data_series
f.close()


#Das duas formas acima recebo 400
session = requests.Session()
# session.cert = MY_CERTIFICATE

try:
    response = session.post(URL, json=JSON)
    print("SEND", str(response.status_code), str(response.text), str(response))
except Exception as e:
    print("Exception caught:", e)

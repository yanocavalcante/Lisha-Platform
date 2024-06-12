#!/usr/bin/env python3
import time, requests, json

get_url ='https://iot.lisha.ufsc.br/api/get.php'

epoch = int(time.time() * 1000000)
query = {
        'series' : {
            'version' : '1.1',
            'unit'    : 2224179493, #equivalent to 0x84924925 = luminous intensity
            'x'       : 741868770,
            'y'       : 679816011,
            'z'       : 25285,
            'r'       : 10*100,
            't0'      : epoch - (5*60*1000000),
            'tf'      : epoch,
            'dev'   : 0
        },
        'credentials' : {
        	'domain' : 'smartlisha',
                'username' : 'smartusername',
                'password' : 'smartpassword'
        }
    }
session = requests.Session()
session.headers = {'Content-type' : 'application/json'}
response = session.post(get_url, json.dumps(query))

print("Get [", str(response.status_code), "] (", len(query), ") ", query, sep='')
if response.status_code == 200:
	print(json.dumps(response.json(), indent=4, sort_keys=False))

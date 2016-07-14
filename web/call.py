import json
import requests

def call(url, method='GET', data={}, headers={}):
	if method is 'GET':
		req = requests.get(url, params=data, headers={})
	else:
		print(headers)
		req = requests.post(url, data=json.dumps(data), headers=headers)
	
	req.encoding = 'utf-8'

	return req.text


def get(url, data={}):
    return call(url, 'GET', data)

def post(url, data={}, headers={}):
    return json.loads(call(url, 'POST', data, headers))
import json
import utils

def read_json(filename):
	with open(filename, 'r') as jsonfile:
		content = jsonfile.read()
		return json.loads(content)

def write_json(filename, struct):
	with open(filename, 'w+') as jsonfile:
		content = json.dumps(struct)
		jsonfile.write(content)


def update_json_list(filename, dict):
	struct = read_json(filename)
	
	if type(struct) != list:
		raise Exception('{0} is not a list'.format(filename))

	struct.append(dict)
	write_json(filename, struct)

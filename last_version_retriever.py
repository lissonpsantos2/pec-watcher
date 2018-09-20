from config import config

import pickle

filename = config.last_version_filename

def run():
	try:
		last_version_info = pickle.load(open(filename, 'rb'))
	except (OSError, IOError) as e:
		last_version_info = {}
		last_version_info['version'] = ''
		last_version_info['link'] = ''
		pickle.dump(last_version_info, open(filename, 'wb'))

	return last_version_info

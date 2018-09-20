from config import config

import pickle

filename = config.last_version_filename

def run(new_version_info):
	pickle.dump(new_version_info, open(filename, 'wb'))

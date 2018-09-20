from config import config

import esusab_info_requester
import last_version_retriever
import new_version_saver
import logging

log_header = '[PEC-WATCHER STATUS]: '
logging.basicConfig(filename=config.logging_filename,level=logging.DEBUG)

def main():
	logging.info(log_header)
	new_request_info = esusab_info_requester.run()
	last_version_info = last_version_retriever.run()

	if (new_request_info == last_version_info):
		logging.info('No version changes')
		return

	logging.info(
		'New changes: OLD_VERSION: ' + last_version_info['version'] +
		'NEW_VERSION: ' + new_request_info['version']
	)

	new_version_saver.run(new_request_info)

main()

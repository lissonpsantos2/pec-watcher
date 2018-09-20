from bs4 import BeautifulSoup
from config import config

import requests
import time
import re


url = config.requisition_link
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
pec_regex = re.compile(r'PEC:\s*\d+\.\d+\.\d+')
pec_version_regex = re.compile(r'\d+\.\d+\.\d+')
pec__regex = re.compile(r'PEC', re.IGNORECASE)

postgreSQL_regex = re.compile(r'postgresql', re.IGNORECASE)
treinamento_regex = re.compile(r'treinamento', re.IGNORECASE)

def run():
	response = requests.get(url, headers=headers)
	soup = BeautifulSoup(response.text, "lxml")

	actual_version = None
	actual_version_link = None

	for tag in soup.find_all(True):
		if (actual_version_link == None and tag.name == 'a' and 'class' in tag.attrs and 'btn' in tag['class'] and 'btn-success' in tag['class'] and 'href' in tag.attrs): #PEC LINK
			actual_version_link = search_version_link(tag)

		if (actual_version == None and tag.name == 'p' and 'class' in tag.attrs and 'text-info' in tag['class']): #PEC VERSION
			actual_version = search_version(tag.contents)

	return_data = {}
	return_data['version'] = actual_version
	return_data['link'] = actual_version_link

	return return_data

def search_version(tags):
	return_match = None
	for tag in tags:
		if (tag.name == 'strong'):
			return_match = pec_regex.match(tag.string)
			if (return_match != None):
				return_match = pec_version_regex.search(return_match.group(0)).group(0)

	return return_match

def search_version_link(main_tag):
	match_pstg = False
	match_train = False
	match_pec = False
	for tag in main_tag.contents:
		if (tag.string != None):
			match_pstg = True if postgreSQL_regex.search(tag.string) != None else False
			match_train = True if treinamento_regex.search(tag.string) != None else False
			match_pec = True if pec__regex.search(tag.string) != None else False
			if (match_pstg and match_train and match_pec):
				return main_tag.get('href')

	return None

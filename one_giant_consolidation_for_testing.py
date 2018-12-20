# Yeet, you already know what it is

import requests
from bs4 import BeautifulSoup
import re 

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 


def single_site(username):
	BASE_URL = "https://venmo.com/"
	url = 'https://venmo.com/' + username
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	
	payment_boxes = soup.find_all(class_ = "paymentpage-text m_five_t")

	return [str(box) for box in payment_boxes]

def descriptions_cleaner(htmllist):
	no_html_bois = []
	for div in htmllist:
		DIV_HEAD = "<div class=\"paymentpage-text m_five_t\">"
		DIV_TAIL = "</div>"
		last_boi = re.sub("<.*?>", "", div)
		no_html_bois.append(last_boi)
	return no_html_bois

def string_ify(cleaned):
	result = []
	for payment in cleaned:
		for word in payment:
			result.append(word)
	return result

def venmo_scraper(username):
	RAW = single_site(username)
	CLEAN = descriptions_cleaner(RAW)
	FIN = string_ify(CLEAN)
	return FIN


def what_we_found_doe(username):
	OUT =  single_site(username) 
	FIN = descriptions_cleaner(OUT) 

	# Time for some W I L D nltk
	# Supposedly the NLTK was too wild? sorry???
	# stop_words = set(stopwords.words('english'))
	# result = [word for word in FIN if word not in stop_words]

	return FIN 




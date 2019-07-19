from requests import get
from bs4 import BeautifulSoup
import re


def single_site(username):
	url = 'https://venmo.com/' + username
	page = get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	payment_boxes = soup.find_all(class_ = "paymentpage-text m_five_t")
	return [str(box) for box in payment_boxes]


def descriptions_cleaner(htmllist):
	no_html = []
	for div in htmllist:
		last = re.sub("<.*?>", "", div)
		no_html.append(last)
	return no_html


def payment_box_list(username):
	raw =  single_site(username)
	cleaned = descriptions_cleaner(raw)
	return cleaned



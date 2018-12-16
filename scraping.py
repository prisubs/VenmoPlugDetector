# Scraping scripts

# Requests to grab URLs, BS4 for cleaning
import requests
from bs4 import BeautifulSoup

# single_site takes in a username string, and constructs the URL of their profile
def single_site(username):

	# Converting a username to a constructed URL
	BASE_URL = "https://venmo.com/"
	url = BASE_URL + username

	# Opening URL
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	
	# Venmo payment boxes have a certain pre-formatted ID in HTML
	payment_boxes = soup.find_all(class_ = "m_five_t p_ten_r")

	# Now we have all of the user's payment box objects, but need to extract descriptions
	print(payment_boxes)




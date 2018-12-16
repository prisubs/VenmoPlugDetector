# Scraping scripts

# Requests to grab URLs, BS4 for cleaning
import requests
from bs4 import BeautifulSoup
import re # I know regex is bad, but sorry ok

# Takes in a username string, and constructs the URL of their profile
def single_site(username):

	# We need to log into Venmo first, or else we can't see more than five requests
	POST_LOGIN_URL = 'https://venmo.com/account/sign-in'
	REQUEST_URL = 'https://my.freecycle.org/home/posts'

	# Converting a username to a constructed URL
	BASE_URL = "https://venmo.com/"
	url = BASE_URL + username

	# Opening URL
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	
	# Venmo payment boxes have a certain pre-formatted ID in HTML
	payment_boxes = soup.find_all(class_ = "paymentpage-text m_five_t")

	# Now we have all of the user's payment box objects, but need to extract descriptions
	return [str(box) for box in payment_boxes]



# Takes in a list of transactions in HTML format and returns a list of text
# Output format: <div class="paymentpage-text m_five_t"> TEXT HERE </div>
def descriptions_cleaner(htmllist):
	# Outputted text will be just text and not HOGWASH
	no_html_bois = []
	for div in htmllist:
		# escape sequences yuhhhhh
		DIV_HEAD = "<div class=\"paymentpage-text m_five_t\">"
		DIV_TAIL = "</div>"

		# Stripping the HTML from the page - I thought bs4 did this but apparently not
		last_boi = re.sub("<.*?>", "", div)

		# Add it onto the final result
		no_html_bois.append(last_boi)
	return no_html_bois





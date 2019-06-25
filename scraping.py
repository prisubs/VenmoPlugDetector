# Scraping scripts

# Requests to grab URLs, BS4 for cleaning
from requests import get
from bs4 import BeautifulSoup
import re # I know regex is bad, but sorry ok

# To remove stopwords for HTML outputting purposes
from nltk.tokenize import word_tokenize

# Takes in a username string, and constructs the URL of their profile
def single_site(username):

	# Converting a username to a constructed URL
	BASE_URL = "https://venmo.com/"
	url = 'https://venmo.com/' + username

	# Opening URL
	page = get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	
	# Venmo payment boxes have a certain pre-formatted ID in HTML
	# This only applies to the web version as of 12/20. They may switch it up idk
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

# Turns a list of sets of words into just a list of words
def string_ify(cleaned):
	result = ""
	for payment in cleaned:
		result += payment + " "
	return result

# Cleaning driver
def venmo_scraper(username):
	RAW = single_site(username)
	CLEAN = descriptions_cleaner(RAW)
	FIN = string_ify(CLEAN)
	return FIN

# I thought I'd need to show proof on HTML that I was actually scraping, so I'll do a remove stop words output 
def what_we_found_doe(username):
	OUT =  single_site(username) # yeah thats some bad repetitive code
	FIN = descriptions_cleaner(OUT) # list of lists

	# Time for some W I L D nltk

	return FIN # TODO this isn't formatted properly



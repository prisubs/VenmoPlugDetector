# Yeet, you already know what it is

import requests
from bs4 import BeautifulSoup
import re 

# Too much rn apparently !!!! SORRY I GUESS!!!!
# from nltk.corpus import stopwords 
# from nltk.tokenize import word_tokenize 


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

import emoji

def alias_translator(aliases):
	results = []
	BASE = ":"

	for alias in aliases:
		emo_boi = emoji.emojize(BASE + alias + BASE)
		results.append(emo_boi)

	return results

def emoji_counter(clean):
	ALCOHOL_ALIAS = ["tropical_drink", "wine_glass", "beer", "cocktail", "beers", "sake"]
	DRUG_ALIAS = ["smoking", "no_smoking", "pill", "dash", "leaves", "mushroom", "ear_of_rice"]

	alcohol_emojis = alias_translator(ALCOHOL_ALIAS)
	drug_emojis = alias_translator(DRUG_ALIAS)
	ILLICIT_EMOJIS = alcohol_emojis + drug_emojis

	count = 0

	for character in clean:
		if character in ILLICIT_EMOJIS:
			count += 1
	return count


def phrase_counter(clean):
	ALCOHOL_PHRASES = ["alc", "alcohol", "bubbly", "champagne", "drinks", "beer", "bud"]
	DRUG_PHRASES = ["weed", "pills", "ecstasy", "broccoli", "plug", "codeine", "high", "buzzed", "stoned", "420", "smoke"]
	VAPE_PHRASES = ["pods", "pod", "juul", "suorin", "vape", "vaping", "vape"]
	BAD_BOIS = ALCOHOL_PHRASES + DRUG_PHRASES + VAPE_PHRASES

	count = 0 
	for word in clean:
		if word in BAD_BOIS:
			count += 1

	return count

def analysis(clean_list):
	BAD_EMOJIS = emoji_counter(clean_list)
	BAD_WORDS = phrase_counter(clean_list)

	TOTAL_SIN = BAD_EMOJIS + BAD_WORDS
	return TOTAL_SIN 

def function_pass(username):
	CLEANED_OUTPUT = venmo_scraper(username) 
	ANALYZED_VALUE = analysis(CLEANED_OUTPUT) 
	FINAL_STATEMENT = output_determination(ANALYZED_VALUE, username)

	return FINAL_STATEMENT 

def output_determination(ANALYZED_VALUE, username):
	OUT_BASE = "Some words we found are "
	PHRASES = what_we_found_doe(username)
	PHRASEBOI = OUT_BASE + str(PHRASES)

	if ANALYZED_VALUE < 1:
		return "This person is unlikely to be engaging in illicit transactions." + PHRASEBOI
	else:
		return "This person might be up to something. The Venmo Snitch found shady phrases!" + PHRASEBOI



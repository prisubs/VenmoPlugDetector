# This file just drives the other two.
import scraping, analysis 

# Takes in a string username, returns a string describing activity
def function_pass(username):
	# List of all words in transactions
	CLEANED_OUTPUT = scraping.venmo_scraper(username) 
	# Count of bad terms found in transactions
	ANALYZED_VALUE = analysis.analysis(CLEANED_OUTPUT) 
	# Outputted string based on count
	FINAL_STATEMENT = output_determination(ANALYZED_VALUE, username)

	return FINAL_STATEMENT # Outputs a string

# Takes in a whole number bad word count, returns appropriate string
def output_determination(ANALYZED_VALUE, username):
	OUT_BASE = "Some words we found are "
	PHRASES = scraping.what_we_found_doe(username)
	PHRASEBOI = OUT_BASE + str(PHRASES)

	if ANALYZED_VALUE < 1:
		return "This person is unlikely to be engaging in illicit transactions." + PHRASEBOI
	else:
		return "This person might be up to something. The Venmo Snitch found shady phrases!" + PHRASEBOI

# function_pass(username) 

# Python driver for testing purposes
uid = input("Enter a username to test ")
out = function_pass(uid)
print(out)

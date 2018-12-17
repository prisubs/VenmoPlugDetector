import scraping.py, analysis.py

# point of contact with HTML
def generate_percentage(username):

	# Generate scraped output for user's name
	venmo_output = single_site(username)
	cleaned_text = descriptions_cleaner(venmo_output)

	# Pass scraped output to analysis methods
	result = analysis(cleaned_text)

	# This result is a whole number percentage, so return a formatted string
	return "%s's likelihood of being a dealer is %s percent.".format(username, result)

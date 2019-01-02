import analysis.py, driver.py, scraping.py

usernames = ["priankaaa", "neilgurnani", "siddhardha-kareddy", "pranav-vysyaraju"]

for username in usernames:
	CLEANED_OUTPUT = venmo_scraper(username) 
	# Count of bad terms found in transactions
	ANALYZED_VALUE = analysis(CLEANED_OUTPUT) 
	# Outputted string based on count
	FINAL_STATEMENT = output_determination(ANALYZED_VALUE, username)

	print("for user %s \n OUTPUT: %s \n VALUE: %s \n STATEMENT: %s \n".format(username, CLEANED_OUTPUT, ANALYZED_VALUE, FINAL_STATEMENT))
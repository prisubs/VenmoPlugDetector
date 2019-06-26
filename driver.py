# This file just drives the other two.
import scraping, analysis
from wtforms import Form, StringField, SubmitField, validators

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
	PHRASES = scraping.what_we_found_doe(username)
	PHRASEBOI = " Some words we found are {0}.".format(str(PHRASES)[1:-1])

	if ANALYZED_VALUE < 1:
		return "This person is unlikely to be engaging in illicit transactions." + PHRASEBOI
	else:
		return "This person might be up to something. The Venmo Snitch found shady phrases!" + PHRASEBOI


from flask import Flask, render_template, request          
app = Flask(__name__)

class UsernameForm(Form):
	query = StringField("Enter a username: ", validators=[validators.data_required()])
	submit = SubmitField('Snitch time!')

@app.route('/', methods=['POST', 'GET'])
def my_form_post():
	form = UsernameForm(request.form)
	if request.method == 'POST':
		text = request.form['query']
		processed_text = function_pass(text)
		return render_template('result.html', output=processed_text)
	elif request.method == 'GET':
		return render_template('index.html', form=form)

if __name__ == "__main__":
	app.run(debug=True)

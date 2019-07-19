from run_model import generate_output
from wtforms import Form, StringField, SubmitField, validators
from flask import Flask, render_template, request

app = Flask(__name__)

class UsernameForm(Form):
	query = StringField("Enter a username: ", validators=[validators.data_required()])
	submit = SubmitField('Snitch time!')

@app.route('/', methods=['POST', 'GET'])
def my_form_post():
	form = UsernameForm(request.form)
	if request.method == 'POST':
		usr = request.form['query']
		conclusion, pmts = generate_output(usr)
		return render_template('result.html', a=conclusion, b=pmts)
	elif request.method == 'GET':
		return render_template('index.html', form=form)

if __name__ == "__main__":
	app.run(debug=True, port=4000)

import scraping.py, analysis.py
from flask import request, redirect

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    print("The email address is '" + email + "'")
    return redirect('/')

# This is the point of contact for the Flask app
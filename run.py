import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', page_title="About", list_of_numbers=[1,2,3]) #page_title is an argument created by ourselves

@app.route('/contact')
def contact():
    return render_template('contact.html', page_title="Contact")

@app.route('/careers')
def careers():
    return render_template('careers.html', page_title="Careers")

if __name__ == "__main__": #name of the default module in Python
    app.run(
        host=os.environ.get('IP', '0.0.0.0'),
        port=int(os.environ.get('PORT', '5001')),
        debug=True) #this allows debug code to be easier but this one should never be TRUE for a finished product or assesement
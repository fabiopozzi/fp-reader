from flask import render_template
from lettore import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Fabio'}
    return render_template('index.html', title='Home', user=user)

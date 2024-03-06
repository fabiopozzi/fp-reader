import sqlite3
from flask import render_template
from lettore import app

connection = sqlite3.connect('prova.sqlite', check_same_thread=False)

@app.route('/')
@app.route('/index')
def index():
    cursore = connection.cursor()
    query = (f"SELECT title, url, content, feed_title, published_date, last_updated from feed_items")
    cursore.execute(query)
    all_news_items = cursore.fetchall()
    cursore.close()
    return render_template('index.html', title='Home', news=all_news_items)


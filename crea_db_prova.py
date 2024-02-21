import sqlite3
import hashlib

url = 'https://www.example.com/feed.xml'
dati = [{'title': 'prova titolo',
         'url': url,
         'urlhash': hashlib.md5(url.encode()),
         'description': 'antani desc',
         'feed_title': 'Un bel feed',
         'content': 'prova contenuto',
         'date_published': '2013-10-07 08:23:19',
         'date_updated': '2013-10-07 10:42:00',
         'feed_id': 1,
         }]
c = sqlite3.connect('prova.sqlite')
cur = c.cursor()

for d in dati:
    query = (f"INSERT INTO feed_items (title, url, urlhash, content, "
             f"feed_title,  published_date, last_updated, feed_id)"
             f"VALUES ('{d['title']}', '{d['url']}', '{d['urlhash'].hexdigest()}', "
             f"'{d['description']}', '{d['feed_title']}', '{d['date_published']}', "
             f"'{d['date_updated']}', {d['feed_id']})")
    cur.execute(query)
c.commit()
cur.close()


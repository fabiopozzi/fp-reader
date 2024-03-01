import sqlite3
import hashlib
import sys

def esempi_tabella_feed_items():
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


def esempi_tabella_feeds():
    dati = [
        {
            'url': 'https://feeds.feedburner.com/LifereaBlog',
            'title': 'Blog Liferea',
            'weburl': 'https://www.example.com/',
        },
        {
            'url': 'https://fabiensanglard.net/rss.xml',
            'title': 'Blog Fabien Sanglard',
            'weburl': 'https://fabiensanglard.net/',
        }]

    c = sqlite3.connect('prova.sqlite')
    cur = c.cursor()
    query = (f"INSERT INTO feeds (title, feedurl, websiteurl, feed_item_count) VALUES (?, ?, ?, ?)")
    for d in dati:
        try:
            sql_data = (d['title'], d['url'], d['weburl'], 0)
            cur.execute(query, sql_data)
            c.commit()
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
    cur.close()
    c.close()
        
if __name__ == "__main__":
    esempi_tabella_feeds()

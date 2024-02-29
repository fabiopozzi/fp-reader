import sqlite3
import hashlib
import feedparser
import ssl
from datetime import datetime
from time import strftime
import logging

logging.basicConfig(filename='/tmp/update-feeds.log', encoding='utf-8', level=logging.DEBUG)

def processrss(url):
    """
    Download the rss feed, break it up and stuff it into the database
    """
    c = sqlite3.connect('prova.sqlite')
    cur = c.cursor()
    try:
        feed = feedparser.parse(url)
        feeditemcount = len(feed["entries"])
        for entry in feed["entries"]:
            title = entry.get("title")
            link = entry.get("link")
            urlhash = hashlib.md5(link.encode())
            description = entry.get("description")
            feed_title = "bho"
            if entry.get("content"):
                description = entry.get("content")[0]["value"]
            # TODO Fix for my timezone
            published = entry.get("published_parsed")
            published = strftime("%Y-%m-%d %H:%M:%S", published)
            date_updated = datetime.now()
            feed_id = 1
            query = (f"INSERT INTO feed_items (title, url, urlhash, content, feed_title, published_date, last_updated, feed_id)"
                     f"VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
            cur.execute(query, (title, link, urlhash.hexdigest(), description, feed_title, published, date_updated, feed_id))

    except Exception as e:
        print(e)
        print("Error processing feed: --------------------------------------------" + url)
        return

    c.commit()
    cur.close()

if __name__ == '__main__':
    processrss("https://feeds.feedburner.com/LifereaBlog")

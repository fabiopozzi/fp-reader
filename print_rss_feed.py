import sqlite3
import hashlib
import feedparser
import ssl
from datetime import datetime
from time import strftime
import logging

logging.basicConfig(filename='/tmp/update-feeds.log', encoding='utf-8', level=logging.DEBUG)
connection = sqlite3.connect('prova.sqlite')

def processrss(feed_id, url, feed_title):
    """
    Download the rss feed, break it up and stuff it into the database
    """
    cur = connection.cursor()
    try:
        feed = feedparser.parse(url)
        feeditemcount = len(feed["entries"])
        for entry in feed["entries"]:
            title = entry.get("title")
            link = entry.get("link")
            urlhash = hashlib.md5(link.encode())
            description = entry.get("description")
            if entry.get("content"):
                description = entry.get("content")[0]["value"]
            # TODO Fix for my timezone
            published = entry.get("published_parsed")
            published = strftime("%Y-%m-%d %H:%M:%S", published)
            date_updated = datetime.now()
            query = (f"INSERT INTO feed_items (title, url, urlhash, content, feed_title, published_date, last_updated, feed_id)"
                     f"VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
            cur.execute(query, (title, link, urlhash.hexdigest(), description, feed_title, published, date_updated, feed_id))

    except Exception as e:
        print(e)
        print("Error processing feed: --------------------------------------------" + url)
        return

    connection.commit()
    cur.close()


if __name__ == "__main__":

    ID = 0
    URL = 1
    TITLE = 2
    cursore = connection.cursor()
    cursore.execute("SELECT id, feedurl, title FROM feeds")
    for row in cursore:
        print(f"id: {row[ID]} url: {row[URL]}, titolo: {row[TITLE]}")
        processrss(row[0], row[1], row[2])
    cursore.close()

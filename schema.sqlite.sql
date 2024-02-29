BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "feed_items" (
	"id"	INTEGER NOT NULL,
	"title"	TEXT,
	"url"	TEXT,
	"urlhash"	TEXT,
	"content"	TEXT,
	"last_updated"	TEXT,
	"haveread"	INTEGER,
	"feed_title"	TEXT,
	"published_date"	TEXT,
	"feed_id"	INTEGER,
	"star"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "feeds" (
	"id"	INTEGER,
	"feedurl"	TEXT,
	"last_checked"	TEXT,
	"title"	TEXT,
	"websiteurl"	TEXT,
	"feed_item_count"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
COMMIT;

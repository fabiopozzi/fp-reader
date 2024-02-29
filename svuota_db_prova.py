import sqlite3
import hashlib

def delete_table_content(conn, cur, table_name):
    query = (f"DELETE FROM {table_name}")
    cur.execute(query)
    conn.commit()


if __name__ == "__main__":
    c = sqlite3.connect('prova.sqlite')
    cur = c.cursor()

    delete_table_content(c, cur, "feed_items")
    delete_table_content(c, cur, "feeds")
    #delete_table_content(c, cur, "sqlite_sequence")

    c.commit()
    cur.close()


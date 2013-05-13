# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from feedparser import parse
import sqlite3
import os

url = "http://ashok567.blogspot.in/feeds/posts/default?alt=rss&v=2&dynamicviews=1&orderby=published&max-results=348&published-max=2013-12-30T18%3A30%3A00.000Z&published-min=2006-01-01T00:00:00%2B05:30"
conn = None

def init_db(path):
    global conn
    if(os.path.exists(path)):
        os.unlink(path)
    
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute('CREATE TABLE posts(title text, post text, date text)')
    conn.commit()
    c.close()

def insert(data):
    global conn
    if not conn:
        init_db('ashok_blog.db')
    c = conn.cursor()
    c.execute('INSERT into posts (title, post, date) values (?, ?, ?)',data)
    conn.commit()
    c.close()
    
parsed_feed = parse(url)

for i in range(0, len(parsed_feed['entries'])):
    item = parsed_feed['entries'][i]
    insert((item['title'],item['summary_detail']['value'],item['published']))


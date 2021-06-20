# -*- coding: utf-8 -*-
from pyquery import PyQuery
import datetime
import sqlite3

def delete_brands_generator():
    url = 'http://www.jpx.co.jp/listing/stocks/delisted/index.html'
    q = PyQuery(url)
    for d, i in zip(q.find('tbody > tr > td:eq(0)'),
                    q.find('tbody > tr > td:eq(2)')):
        date = datetime.datetime.strptime(d.text, '%Y/%m/%d').date()
        yield (i.text, date)

def insert_delete_brands_to_db(db_file_name):
  conn = sqlite3.connect(db_file_name)
  with conn:
    sql = 'INSERT INTO delete_brands(code,date) VALUES(?,?)'
    conn.executemany(sql, delete_brands_generator())

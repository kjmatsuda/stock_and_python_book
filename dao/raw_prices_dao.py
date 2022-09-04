# -*- coding: utf-8 -*-
import sqlite3

# TODO DAO のベースクラスを定義
class RawPricesDAO(object):
    def __init__(self, db_file_name):
        self.db_file_name = db_file_name

    def get_latest_date_of_tick_code(self, code):
        conn = sqlite3.connect(self.db_file_name)
        with conn:
            result = conn.execute('SELECT date from raw_prices '
                                    'WHERE code = ? ORDER BY date DESC LIMIT 1',
                                    (code,)).fetchone()
            latest_date = None
            if result != None:
                latest_date = result[0]
            return latest_date

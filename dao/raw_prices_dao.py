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

    def insert(self, code, pdr_df):
        price_generator = self.generate_price_from_pdr_df(code, pdr_df)

        conn = sqlite3.connect(self.db_file_name)
        with conn:
            sql = """
            INSERT INTO raw_prices(code,date,open,high,low,close,volume)
            VALUES(?,?,?,?,?,?,?)
            """
            conn.executemany(sql, price_generator)

    def generate_price_from_pdr_df(self, code, pdr_df):
        for tuple in pdr_df.itertuples():
            date = tuple[0].strftime('%Y-%m-%d')
            open = round(float(tuple[3]), 2) # 初値
            high = round(float(tuple[1]), 2) # 高値
            low = round(float(tuple[2]), 2) # 安値
            close = round(float(tuple[4]), 2) # 終値
            volume = int(tuple[5]) # 出来高

            yield code, date, open, high, low, close, volume

# pandas_datareader で株価データを取得し、raw_prices テーブルに登録する
import os
from datetime import datetime as dt, date, timedelta
from pandas_datareader import data as pdr

from dao.brands_dao import BrandsDAO
from dao.raw_prices_dao import RawPricesDAO

db_file_name = os.getcwd() + '/chapter2/stock.db'

brands_dao = BrandsDAO(db_file_name)
raw_prices_dao = RawPricesDAO(db_file_name)

code_list = brands_dao.get_brands_code_list()

for code in code_list:
    if code == '7201':
        latest_date_str = raw_prices_dao.get_latest_date_of_tick_code(code)
        # print('code:%s, 最新日時: %s' % (code, latest_date_str))

        # データ取得開始日
        start='2000-01-01'

        if latest_date_str != None:
            latest_date = dt.strptime(latest_date_str, '%Y-%m-%d')
            start = latest_date + timedelta(days = 1)

        # データ取得終了日
        end = '2021-06-15'

        ticker_symbol = code + ".T"
        pdr_df = pdr.get_data_yahoo(symbols=ticker_symbol, start=start, end=end, adjust_price=False)

        raw_prices_dao.insert(code, pdr_df)

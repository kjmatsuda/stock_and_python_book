# pandas_datareader で株価データを取得し、raw_prices テーブルに登録する
import os
from dao.brands_dao import BrandsDAO
from dao.raw_prices_dao import RawPricesDAO

db_file_name = os.getcwd() + '/chapter2/stock.db'

brands_dao = BrandsDAO(db_file_name)
raw_prices_dao = RawPricesDAO(db_file_name)

code_list = brands_dao.get_brands_code_list()

for code in code_list:
    date = raw_prices_dao.get_latest_date_of_tick_code(code)
    print('code:%s, 最新日時: %s' % (code, date))

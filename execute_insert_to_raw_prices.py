# pandas_datareader で株価データを取得し、raw_prices テーブルに登録する
import os
from dao.brands_dao import BrandsDAO

db_file_name = os.getcwd() + '/chapter2/stock.db'

dao = BrandsDAO(db_file_name)

code_list = dao.get_brands_code_list()

for code in code_list:
    print(code)

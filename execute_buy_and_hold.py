# TOPIX Core 30 に連動する ETF の buy and hold 戦略と比較してみる
import chapter3.buy_and_hold as buy_and_hold
import datetime
import os

db_path = os.getcwd() + '/chapter2/stock.db'

start_date = datetime.date(2010, 4, 1)
end_date = datetime.date(2018, 4, 1)

# TOPIX Core30 に連動する ETF である「MAXIS トピックス・コア30 上場投信」のコード
topix_core_30_code = 1344

# 最初の所持金
deposit = 1000000

# シミュレーション実行
portfolio, result = buy_and_hold.simulate_buy_and_hold(
    db_path, start_date, end_date,
    topix_core_30_code, deposit
)

# 3.3.4 ゴールデンクロス・デッドクロス戦略のシミュレーション結果 (No.1379)
import chapter3.golden_core30 as golden_core30
import datetime
import os

db_path = os.getcwd() + '/chapter2/stock.db'

start_date = datetime.date(2010, 4, 1)
end_date = datetime.date(2018, 4, 1)

# Core 30銘柄コード
# code_list = (
# 2914, 3382, 4063, 4502, 4503, 6501, 6752, 6758, 6861, 6902,
# 6954, 6981, 7201, 7203, 7267, 7751, 7974, 8031, 8058, 8306,
# 8316, 8411, 8766, 8802, 9020, 9022, 9432, 9433, 9437, 9984)

# 9437 を含んでたらエラーが出たので消した(TypeError: 'NoneType' object is not subscriptable)
# 9437(ＮＴＴドコモ) は 上場廃止になったからのようだ...
code_list = (
2914, 3382, 4063, 4502, 4503, 6501, 6752, 6758, 6861, 6902,
6954, 6981, 7201, 7203, 7267, 7751, 7974, 8031, 8058, 8306,
8316, 8411, 8766, 8802, 9020, 9022, 9432, 9984)

# test

# 最初の所持金
deposit = 1000000

# 最低購入額
order_under_limit = 100000

# シミュレーション実行
portfolio, result = golden_core30.simulate_golden_dead_cross(
    db_path, start_date, end_date,
    code_list, deposit, order_under_limit
)

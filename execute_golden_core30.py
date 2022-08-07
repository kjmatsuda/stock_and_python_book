# 3.3.4 ゴールデンクロス・デッドクロス戦略のシミュレーション結果 (No.1379)
import chapter3.golden_core30 as golden_core30
import datetime
import os
import chapter4_5.simulator as sim

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
# test2, test3, test4, test5, test6, test7, test8

# 最初の所持金
deposit = 1000000

# 最低購入額
order_under_limit = 100000

# シミュレーション実行
portfolio, result = golden_core30.simulate_golden_dead_cross(
    db_path, start_date, end_date,
    code_list, deposit, order_under_limit
)

# 収益率を求める (p149)
returns = (result.profit - result.profit.shift(1)) / result.price.shift(1)

# 最終結果を出力
print("winning percentage: %(winning_percentage)s" % {'winning_percentage': portfolio.calc_winning_percentage()})
print("payoff ratio: %(payoff_ratio)s" % {'payoff_ratio': portfolio.calc_payoff_ratio()})
print("profit factor: %(profit_factor)s" % {'profit_factor': portfolio.calc_profit_factor()})
print("max drawdown: %(max_drawdown)s" % {'max_drawdown': sim.calc_max_drawdown(result.price)})
print("sharp ratio: %(sharp_ratio)s" % {'sharp_ratio': sim.calc_sharp_ratio(returns)})
# print("information ratio: %(information_ratio)s" % {'information_ratio': calc_information_ratio(returns, returns_benchmark)})
print("sortino_ratio: %(sortino_ratio)s" % {'sortino_ratio': sim.calc_sortino_ratio(returns)})
print("calmar ratio: %(calmar_ratio)s" % {'calmar_ratio': sim.calc_calmar_ratio(result.price, returns)})

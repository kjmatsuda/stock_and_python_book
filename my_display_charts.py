# 参考
# pandas-highchartsのdisplay_chartsをjupyter以外の環境で実行する - Qiita
# https://qiita.com/hatt_takumi/items/b2f333cf22375367c186
import pandas as pd
import webbrowser
import os

def my_display_charts(df, chart_type="default", render_to=None, **kwargs):
    from pandas_highcharts.core import serialize
    from pandas_highcharts.display import _generate_div_id_chart
    if chart_type not in ("default", "stock"):
        raise ValueError("Wrong chart_type: accept 'default' or 'stock'.")
    chart_id = render_to if render_to is not None else _generate_div_id_chart()
    json_data = serialize(df, render_to=chart_id, chart_type=chart_type, **kwargs)

    content = """
    <div id="{chart_id}"</div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highcharts/8.1.1/highstock.min.js"></script>
    <script type="text/javascript">{data}</script>
    """

    html = """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <title>My Result</title>
    </head>
    <body>
        {content}
    </body>
    </html>
    """
    return html.format(content=content.format(chart_id=chart_id, data=json_data))

def display_charts_browser(df, chart_type="default"):
    html_data = my_display_charts(df, chart_type, title="My Result", figsize=(1200, 800), grid=True)
    path = 'index.html'

    with open(path, mode='w') as f:
        f.write(html_data)

    webbrowser.open_new_tab(os.getcwd() + '/' + path)    

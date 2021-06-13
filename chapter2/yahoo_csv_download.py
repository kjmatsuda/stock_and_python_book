# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

MAX_RETRY_NUM = 10

def download_stock_csv(code_range, save_dir):

    # CSVファイルを自動で save_dir に保存するための設定
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList",
                           2)
    profile.set_preference("browser.download.manager.showWhenStarting",
                           False)
    profile.set_preference("browser.download.dir", save_dir)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                           "text/csv")

    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get('https://www.yahoo.co.jp/')

    # ここで手動でログインを行う。ログインしたら enter
    input('After login, press enter: ')

    retry = 0
    for code in code_range:
        url = 'https://stocks.finance.yahoo.co.jp/stocks/history/?code={0}.T'.format(code)

        while retry < MAX_RETRY_NUM:
            try: 
                driver.get(url)
            except TimeoutException:
                retry = retry + 1
                print("Timeout: %(url)s" % {'url': url})
                print("Retrying... (%(retry)s/%(max)s)" % {'retry': retry, 'max': MAX_RETRY_NUM})
            else:
                retry = 0
                break

        if retry >= MAX_RETRY_NUM:
            raise TimeoutException()
        
        try:
            # driver.find_element_by_css_selector('a.stocksCsvBtn').click()
            driver.find_element_by_css_selector('a.To_QbbNE').click()
        except NoSuchElementException:
            pass

if __name__ == '__main__':
    import os
    # download_stock_csv((7203, 9684), os.getcwd())
    download_stock_csv(range(7696,  9998), os.getcwd())
    

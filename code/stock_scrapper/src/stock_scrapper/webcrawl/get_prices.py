"""
Scrap stock data from google.

Erick Medeiros Anastácio
2020-09-12
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def _get_element(driver, xpath):
    try:
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    except Exception as e:
        print(e)
        element = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
    return element


def get_stocks_value(stock_list, fx_bin=None):
    """Get stock value from google.

    Parameters
    ----------
    stock_list : list
        list of stock symbols
    fx_bin : string
        The firefox_binary path, for selenium driver

    Returns
    -------
    list
        Where each item is a dict containing
        - 'stock': stock code
        - 'valor': stock value

    """
    options = Options()
    options.headless = True
    # fx_bin = '/usr/bin/firefox-esr'

    driver = webdriver.Firefox(options=options, firefox_binary=fx_bin)
    stock_values = [_get_one(driver, stock) for stock in stock_list]
    driver.quit()

    # lista_chunks = [
    #     stock_list[pos:pos+3] for pos in range(0, len(stock_list), 3)
    #     ]
    # # flattening
    # stock_values = list(itertools.chain(*stock_values))

    return stock_values


def _get_one(driver, stock):
    try:
        print(f'getting {stock}')
        driver.get('http://www.google.com')

        xpath = "//input[@class='gLFyf gsfi'][1]"
        search_bar = _get_element(driver, xpath)
        # stock = (1, 'ITUB4')
        search_bar.clear()
        search_bar.send_keys(stock)

        xpath = "//input[@class='gNO89b'][1]"
        go_btn = _get_element(driver, xpath)
        go_btn.submit()

        xpath = "//span[@class='IsqQVc NprOob XcVN5d wT3VGc'][1]"
        valor = _get_element(driver, xpath).text
        valor = float(valor.replace(',', '.'))
        print(valor)

    except Exception as e:
        print(e)
        print(f'erro em obter {stock}')
        # raise(e)
        valor = None

    return {'stock': stock, 'valor': valor}

from stock_scrapper.webcrawl.get_prices import get_stocks_value


def test_scrapper():
    data = ['ITUB4', 'BIDI3']
    results = get_stocks_value(data)
    assert isinstance(results, list)
    assert len(results) == 2
    assert results[0]['stock'] == 'ITUB4'
    assert results[1]['stock'] == 'BIDI3'

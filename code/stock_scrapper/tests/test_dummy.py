from stock_scrapper.dummy.dummy_app import process_data


def test_processor():
    data = ['str01', 'str02']
    results = process_data(data)
    assert isinstance(results, dict)


# def test_processor_error():
#     data = ['str01', 'str02']
#     results = process_data(data)
#     assert isinstance(results, list)

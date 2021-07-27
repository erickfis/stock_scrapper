"""Dummy application."""


def process_data(data_list: list) -> dict:
    """Short summary.

    Parameters
    ----------
    data_list : list
        Description of parameter `data_list`.

    Returns
    -------
    dict
        Description of returned object.

    """
    return {data: f'proc_{data}' for data in data_list}

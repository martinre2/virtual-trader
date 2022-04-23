import json

import yfinance as yf


def get_price_by_ticker(symbol: str, interval: str = "30m") -> dict:
    """Get historical price data

    Args:
        symbol (str): ticker symbol
        interval (str, optional): Defaults to "30m".

    Returns:
        dict: {"price": "str", "time": int}
    """

    data = yf.download(tickers=symbol.upper(), period="1d", interval=interval)

    hourly_data = data[1::2]

    hourly_data.reset_index(inplace=True)

    hourly_data_renamed = hourly_data.rename(
        columns={"Open": "price", "Datetime": "time"}
    )
    filtered_data = hourly_data_renamed[["time", "price"]]
    json_f = filtered_data.to_json(orient="records")

    return json.loads(json_f)

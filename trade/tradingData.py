from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
import json
from datetime import datetime, timedelta
from numpy import busday_count, sum
from pydantic.error_wrappers import ValidationError

file = open("data/keys.json", "rb")
api_cred = json.load(file)
file.close()

class getStock:
    def __init__(self) -> None:
        pass
    
    def data(ticker):
        # No keys required for crypto data
        client = StockHistoricalDataClient(api_key=api_cred["Alpaca"]["paper"]["API_KEY_ID"], secret_key=api_cred["Alpaca"]["paper"]["API_SECRET_KEY"])

        try:
            request_params = StockBarsRequest(symbol_or_symbols=[ticker], timeframe=TimeFrame.Day, start=(datetime.now() - timedelta(days=365)), end=datetime.now())

        except ValidationError:
            raise TypeError("Recieved a ticker that is not allowed. Value: %s, Type: %s" % (ticker, type(ticker)))

        ticker_bars = client.get_stock_bars(request_params)

        close_value = ticker_bars.df

        file = "data/stocks/%s.json" % ticker
        with open(file, "w", encoding='utf-8') as f:
            close_value.to_json(path_or_buf=f, orient='records')

class getIndicators:
    
    def __init__(self) -> None:
        pass

    def sma(ticker):
        date_today = datetime.now().strftime("%Y-%m-%d")
        date_50 = (datetime.now() - timedelta(days=50)).strftime("%Y-%m-%d")
        date_200 = (datetime.now() - timedelta(days=200)).strftime("%Y-%m-%d")
        date_200_bus = busday_count(date_200, date_today)
        date_50_bus = busday_count(date_50, date_today)

        file = open("data/stocks/%s.json" % ticker, "rb")
        data = json.load(file)
        file.close()

        close_value = [item['close'] for item in data]

        close_value_length = len(close_value)

        close200 = close_value[(close_value_length-date_200_bus-1):close_value_length]
        close50 = close_value[(close_value_length-date_50_bus-1):close_value_length]

        sum50 = sum(close50)
        sum200 = sum(close200)

        return((sum200 / date_200_bus), (sum50 / date_50_bus))
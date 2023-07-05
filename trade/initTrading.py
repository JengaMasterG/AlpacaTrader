import json
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

#API Credentials
file = open("data/keys.json", "rb")
api_cred = json.load(file)
file.close()

class AccountData:
    
    def __init__(
        self,
        PAPER: bool = True
    ):
        self.PAPER = PAPER
    
    def getAccount(PAPER):
        """
        Downloads personal brokerage account data.
        Args:
            paper (bool): Chooses if the paper account should be used or not. True is paper trading. Enabled by default.
        """
        if PAPER is True:
            url = api_cred["Alpaca"]["paper"]["url"]
            API_KEY = api_cred["Alpaca"]["paper"]["API_KEY_ID"]
            SECRET_KEY = api_cred["Alpaca"]["paper"]["API_SECRET_KEY"]
            file_json = "data/paper.json"

        else:
            url = api_cred["Alpaca"]["live"]["url"]
            API_KEY = api_cred["Alpaca"]["live"]["API_KEY_ID"]
            SECRET_KEY = api_cred["Alpaca"]["live"]["API_SECRET_KEY"]
            file_json = "data/live.json"

        #Check Account Data
        trading_client = TradingClient(API_KEY, SECRET_KEY, paper=PAPER)

        account = trading_client.get_account()

        #Save Account Data
        data = {}

        for property_name, value in account:
            data[f"{property_name}"] = f"{value}"

        with open(file_json, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4, sort_keys=True)

from trade.initTrading import AccountData
from trade.tradingData import getIndicators, getStock

PAPER = True
ticker = "googl"

AccountData.getAccount(PAPER)
getStock.data(ticker)
smavgs = getIndicators.sma(ticker)

print(smavgs)
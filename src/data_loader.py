import yfinance as yf


dat = yf.Ticker("MSFT")
print(dat.quarterly_income_stmt)
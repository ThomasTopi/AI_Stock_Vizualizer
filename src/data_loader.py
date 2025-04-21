import yfinance as yf

class DataLoader():
    def __init__(self, ticker: str) -> None:
        self.ticker = yf.Ticker(ticker)

    def get_info(self) -> dict:
        stock = self.ticker
        info = stock.info
        return {
            "name": info.get("shortName"),
            "sector": info.get("sector"),
            "price": f"${info.get('regularMarketPrice')}",
            "market_cap": info.get("marketCap"),
            "dividendYield": f"{info.get('dividendYield')}% p.a." if info.get('dividendYield') else "N/A"
        }
    
    def format_market_cap(value) -> str:
        if value is None:
            return "N/A"
        elif value >= 1_000_000_000:
            return f"${value / 1_000_000_000:.2f}B"
        elif value >= 1_000_000:
            return f"${value / 1_000_000:.2f}M"
        else:
            return f"${value:,}"
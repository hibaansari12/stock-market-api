import yfinance as yf

symbols = ["AAPL", "MSFT", "GOOG", "TSLA", "AMZN"]

for symbol in symbols:
    df = yf.download(symbol, period="1y")
    df.reset_index().to_csv(
        f"data/raw/{symbol}_raw.csv",
        index=False
    )
print("✅ Raw stock data fetched and saved!")
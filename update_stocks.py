import yfinance as yf
import pandas as pd

symbols = ["AAPL", "MSFT", "GOOG", "TSLA", "AMZN"]
clean_stock_data = {}

for symbol in symbols:
    # Fetch stock data
    stock = yf.Ticker(symbol)
    df = stock.history(period="1y")

    # Clean data
    df = df.reset_index()
    df = df.dropna()
    df = df.sort_values("Date")
    df = df.drop(columns=["Dividends", "Stock Splits"])
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

    # Save to dictionary (optional)
    clean_stock_data[symbol] = df

    # Save CSV (overwrite old file)
    df.to_csv(f"data/clean/{symbol}_clean.csv", index=False)

print("All stock CSVs are updated!")

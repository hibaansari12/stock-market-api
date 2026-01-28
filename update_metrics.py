import pandas as pd

symbols = ["AAPL", "MSFT", "GOOG", "TSLA", "AMZN"]
all_metrics = []

for symbol in symbols:
    # 1️⃣ Load clean CSV
    df = pd.read_csv(f"data/clean/{symbol}_clean.csv")

    # 2️⃣ Ensure Date column is datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # 3️⃣ Calculate Daily Return
    df['daily_return'] = df['Close'].pct_change().fillna(0)

    # 4️⃣ Moving Average (7-day)
    df['MA7'] = df['Close'].rolling(window=7).mean()

    # 5️⃣ 52-week High / Low (252 trading days)
    df['week_52_high'] = df['Close'].rolling(window=252).max()
    df['week_52_low'] = df['Close'].rolling(window=252).min()

    # 6️⃣ Volatility (annualized)
    df['Volatility'] = (
        df['daily_return'].rolling(window=252).std() * (252 ** 0.5)
    )

    # 7️⃣ Round numeric values
    df = df.round({
        "Open": 2,
        "High": 2,
        "Low": 2,
        "Close": 2,
        "daily_return": 6,
        "MA7": 2,
        "week_52_high": 2,
        "week_52_low": 2,
        "Volatility": 6
    })

    # 8️⃣ Replace NaN with None (Django-friendly)
    df = df.where(pd.notnull(df), None)

    # 9️⃣ Add stock symbol
    df['Symbol'] = symbol

    all_metrics.append(df)

# 🔟 Combine all stocks into ONE table
final_df = pd.concat(all_metrics, ignore_index=True)

# Save
final_df.to_csv("data/metric/all_stock_metrics.csv", index=False)

print("✅ All stock metrics updated in ONE file")

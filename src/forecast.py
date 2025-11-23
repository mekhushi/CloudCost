def forecast_cost(df):
    df = df.copy()
    df = df.sort_values("Timestamp")

    df["Forecast"] = df["CostUSD"].rolling(window=3).mean()

    return df.tail(20)

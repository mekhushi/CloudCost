def detect_anomalies(df):
    mean = df["CostUSD"].mean()
    std = df["CostUSD"].std()

    threshold = mean + 2 * std

    anomalies = df[df["CostUSD"] > threshold]
    return anomalies

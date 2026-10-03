def validate_weather_data(df):
    return {
        "rows": len(df),
        "missing_cells": int(df.isna().sum().sum()),
        "duplicates": int(df.duplicated().sum()),
        "negative_rainfall": int((df["Rainfall_mm"] < 0).sum()),
        "invalid_humidity": int((~df["Humidity_pct"].between(0,100)).sum()),
    }

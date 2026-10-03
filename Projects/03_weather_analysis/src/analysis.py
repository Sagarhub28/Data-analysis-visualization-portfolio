def weather_summary(df):
    return df.groupby("Month").agg(
        Avg_Temperature=("Temperature_C","mean"),
        Total_Rainfall=("Rainfall_mm","sum"),
        Avg_Humidity=("Humidity_pct","mean")
    )

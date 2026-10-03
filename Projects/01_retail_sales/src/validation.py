def validate_sales_data(df):
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "negative_sales": int((df["Sales"] < 0).sum()),
        "negative_profit_rows": int((df["Profit"] < 0).sum()),
        "invalid_quantity": int((df["Quantity"] <= 0).sum()),
    }

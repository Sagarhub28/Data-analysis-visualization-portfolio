import pandas as pd

def load_sales_data(path):
    return pd.read_csv(path, encoding="cp1252")

def clean_sales_data(df):
    df = df.copy()
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")
    df["Shipping_Days"] = (df["Ship Date"] - df["Order Date"]).dt.days
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    df["Weekday"] = df["Order Date"].dt.day_name()
    return df

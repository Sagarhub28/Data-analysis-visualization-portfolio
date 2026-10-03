def sector_summary(df):
    return df.groupby('Asset_Sector').agg(
        Avg_Return=('Daily_Return',lambda s:s.mean()*100),
        Volatility=('Daily_Return',lambda s:s.std()*252**0.5*100),
        Avg_Volume=('Trading_Volume','mean'),
        Avg_Sentiment=('Sentiment_Score','mean')
    )

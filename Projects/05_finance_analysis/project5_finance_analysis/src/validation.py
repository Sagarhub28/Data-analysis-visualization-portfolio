def validate(df):
    required=['Date','Asset_Sector','Market','Closing_Price','Daily_Return','Trading_Volume','Sentiment_Score','Engagement_Index','Investment_Risk']
    assert all(c in df.columns for c in required)
    assert df.Closing_Price.gt(0).all()
    assert df.Trading_Volume.ge(0).all()
    return True

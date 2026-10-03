def condition_summary(df):
    return df.groupby('Condition').agg(Patients=('Patient_ID','count'),Avg_Age=('Age','mean'),Avg_Visits=('Annual_Visits','mean'),High_Risk_Rate=('High_Risk',lambda s:(s=='Yes').mean()*100))

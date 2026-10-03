import pandas as pd
def validate(df):
    required=['Patient_ID','Age','Gender','Condition','Smoking_Status','BMI','Systolic_BP','Cholesterol','Glucose','Annual_Visits','High_Risk']
    assert all(c in df.columns for c in required)
    assert df.Patient_ID.is_unique
    assert df.Age.between(0,120).all()
    assert (df.BMI>0).all()
    assert (df.Annual_Visits>=0).all()
    return True

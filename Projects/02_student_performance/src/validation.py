def validate_student_data(df):
    return {
        "rows": len(df),
        "missing_cells": int(df.isna().sum().sum()),
        "duplicates": int(df.duplicated().sum()),
        "attendance_out_of_range": int(((df["Attendance"] < 0) | (df["Attendance"] > 100)).sum()),
        "scores_out_of_range": int(((df[["Math_Score","Science_Score","English_Score","Final_Score"]] < 0) |
                                    (df[["Math_Score","Science_Score","English_Score","Final_Score"]] > 100)).sum().sum())
    }

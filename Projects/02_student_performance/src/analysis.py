def calculate_student_metrics(df):
    return {
        "pass_rate": (df["Result"].eq("Pass").mean() * 100),
        "attendance_final_correlation": df["Attendance"].corr(df["Final_Score"]),
        "study_final_correlation": df["Study_Hours"].corr(df["Final_Score"])
    }

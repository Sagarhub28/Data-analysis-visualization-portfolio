import matplotlib.pyplot as plt
def condition_chart(df,path):
    df.Condition.value_counts().sort_values().plot.barh()
    plt.title('Patient Distribution by Condition'); plt.tight_layout(); plt.savefig(path); plt.close()

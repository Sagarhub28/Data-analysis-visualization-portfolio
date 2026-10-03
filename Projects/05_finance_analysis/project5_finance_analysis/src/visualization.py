import matplotlib.pyplot as plt
def return_distribution(df,path):
    plt.hist(df['Daily_Return']*100,bins=40)
    plt.title('Distribution of Daily Returns')
    plt.tight_layout(); plt.savefig(path); plt.close()

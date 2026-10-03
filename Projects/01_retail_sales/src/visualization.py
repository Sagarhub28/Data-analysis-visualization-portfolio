import matplotlib.pyplot as plt

def save_bar(series, title, xlabel, ylabel, path):
    plt.figure(figsize=(9,5))
    series.plot(kind="bar")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(path, dpi=180)
    plt.close()

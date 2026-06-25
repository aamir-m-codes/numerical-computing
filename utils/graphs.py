import matplotlib.pyplot as plt


def scatter(x, y, title, x_label, y_label):
    plt.scatter(x, y, marker="o")
    plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

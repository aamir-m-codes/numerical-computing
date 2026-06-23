import matplotlib.pyplot as plt


def plot(x, y, title, x_label, y_label):
    plt.plot(x, y, marker="o")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

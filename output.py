import matplotlib.pyplot as plt


def save_plot(x, y, title, xaxis, yaxis, filename):
    """
    Function to generate plots

    """
    plt.figure()
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)

    plt.savefig(f"results/{filename}")
    plt.close()
    print(title + " plot generated")

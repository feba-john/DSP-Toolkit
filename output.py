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


def save_plot_fft(x, y, N, title, xaxis, yaxis, filename):
    """
    Function to generate plot for frequency spectrum

    only positive frequencies taken for real signals
    """
    plt.figure()
    plt.plot(x, y)
    plt.plot(x[:N//2], y[:N//2])
    plt.xlim(0, 20)
    plt.title(title)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)

    plt.savefig(f"results/{filename}")
    plt.close()
    print(title + " plot generated")

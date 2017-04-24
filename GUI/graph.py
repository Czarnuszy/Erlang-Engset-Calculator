import matplotlib.pyplot as plt


def generate_graph(x, y, lines):
    for i in range(len(y)):
        plt.plot(x, y[i], "o:", label=str(lines[i])+" lines")
    plt.title('Block rate Graph')
    plt.grid(True)
    plt.xlabel('Traffic')
    plt.ylabel('Block Rate')
    plt.legend()
    plt.show()


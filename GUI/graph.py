import matplotlib.pyplot as plt


def generate_graph(x, y, lines, graph):
    if graph == "lines":
        for i in range(len(y)):
            plt.plot(x, y[i], "o:", label=str(lines[i])+" lines")
        plt.title('Traffic/Lines Graph')
        plt.grid(True)
        plt.xlabel('Traffic')
        plt.ylabel('Block Rate')
    elif graph == 'block':
        for i in range(len(y)):
            plt.plot(x, y[i], "o:", label=str(lines[i])+" Blocking Rate")
        plt.title('Lines/Blocking Rate Graph')
        plt.grid(True)
        plt.xlabel('Lines')
        plt.ylabel('Traffic')
    plt.legend()
    plt.show()


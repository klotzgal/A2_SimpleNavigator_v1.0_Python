from graph import Graph
from config import FILENAME


def main():
    g = Graph()
    g.load_graph_from_file(FILENAME)
    g.print_graph()


if __name__ == "__main__":
    main()

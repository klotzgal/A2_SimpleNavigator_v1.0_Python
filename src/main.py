from python.config import FILENAME
from python.graph import Graph
from python.s21_graph_algorithms import GraphAlgorithms


def main() -> None:
    g = Graph()
    g.load_graph_from_file(FILENAME)
    g.print_graph()
    g.load_graph_from_file("examples/non_full.txt")
    g.print_graph()
    alg = GraphAlgorithms()
    way = alg.depth_first_search(g, 0)
    print(way)
    g.load_graph_from_file("examples/tsm.txt")
    g.print_graph()
    print(alg.depth_first_search(g, 0))


if __name__ == "__main__":
    main()

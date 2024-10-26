from python.config import FILENAME
from python.graph import Graph
from python.s21_graph_algorithms import GraphAlgorithms


def main() -> None:
    g = Graph()
    g.load_graph_from_file(FILENAME)
    g.print_graph()
    g.load_graph_from_file("examples/weighted_or_graph.txt")
    g.print_graph()
    alg = GraphAlgorithms()
    path_len = alg.get_shortest_path_between_vertices(g, 0, 3)
    print(path_len)


if __name__ == "__main__":
    main()

from python.config import FILENAME
from python.graph import Graph
from python.s21_graph_algorithms import GraphAlgorithms


def main() -> None:
    g = Graph()
    g.load_graph_from_file(FILENAME)
    g.print_graph()
    g.load_graph_from_file("examples/input.txt")
    g.print_graph()
    alg = GraphAlgorithms()
    data = alg.get_shortest_paths_between_all_vertices(g)
    new_g = Graph()
    new_g._data = data
    new_g.print_graph()


if __name__ == "__main__":
    main()

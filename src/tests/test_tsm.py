from python.graph import Graph
from python.s21_graph_algorithms import GraphAlgorithms


def test_tsm(tsm_graph: Graph) -> None:
    alg = GraphAlgorithms()
    result = alg.solve_traveling_salesman_problem(tsm_graph)
    assert result.distance == 62.0


def test_weighted_tsm(weighted_graph: Graph) -> None:
    alg = GraphAlgorithms()
    result = alg.solve_traveling_salesman_problem(weighted_graph)
    assert result.distance == 101.0

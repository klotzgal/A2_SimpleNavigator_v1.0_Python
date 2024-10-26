import pytest

from python import Graph, GraphAlgorithms


def test_valid(weighted_graph: Graph) -> None:
    alg = GraphAlgorithms()
    result: float = alg.get_shortest_path_between_vertices(weighted_graph, 0, 5)
    assert result == 31


def test_invalid(weighted_graph: Graph) -> None:
    alg = GraphAlgorithms()
    with pytest.raises(IndexError):
        alg.get_shortest_path_between_vertices(weighted_graph, 0, 22)


def test_non_full_0_5(non_full_graph: Graph) -> None:
    alg = GraphAlgorithms()
    result: float = alg.get_shortest_path_between_vertices(non_full_graph, 0, 5)
    assert result == 2


def test_non_full_0_7(non_full_graph: Graph) -> None:
    alg = GraphAlgorithms()
    result: float = alg.get_shortest_path_between_vertices(non_full_graph, 0, 7)
    assert result == float("inf")


def test_loop_1_0(loop_graph: Graph) -> None:
    alg = GraphAlgorithms()
    result: float = alg.get_shortest_path_between_vertices(loop_graph, 1, 0)
    assert result == 1


def test_loop_0_7(loop_graph: Graph) -> None:
    alg = GraphAlgorithms()
    result: float = alg.get_shortest_path_between_vertices(loop_graph, 0, 7)
    assert result == 2


def test_oriented_graph_0_3(weighted_or_graph: Graph) -> None:
    alg = GraphAlgorithms()
    result: float = alg.get_shortest_path_between_vertices(weighted_or_graph, 0, 3)
    assert result == 12


def test_oriented_graph_7_1(weighted_or_graph: Graph) -> None:
    alg = GraphAlgorithms()
    result: float = alg.get_shortest_path_between_vertices(weighted_or_graph, 7, 1)
    assert result == float("inf")

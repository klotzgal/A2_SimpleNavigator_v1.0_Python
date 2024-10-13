import pytest

from python import Graph, GraphAlgorithms


def test_bfs_valid(normal_graph: Graph) -> None:
    alg = GraphAlgorithms()
    way = alg.breadth_first_search(normal_graph, 0)
    assert way == [0, 1, 2, 3, 5, 7, 4, 6]


def test_bfs_invalid(normal_graph: Graph) -> None:
    alg = GraphAlgorithms()
    with pytest.raises(IndexError):
        alg.breadth_first_search(normal_graph, 10)


def test_bfs_non_full_0(non_full_graph: Graph) -> None:
    alg = GraphAlgorithms()
    way = alg.breadth_first_search(non_full_graph, 0)
    assert way == [0, 1, 2, 3, 5, 4, 6]


def test_bfs_non_full_7(non_full_graph: Graph) -> None:
    alg = GraphAlgorithms()
    way = alg.breadth_first_search(non_full_graph, 7)
    assert way == [7]


def test_bfs_loop_0(loop_graph: Graph) -> None:
    alg = GraphAlgorithms()
    way = alg.breadth_first_search(loop_graph, 0)
    assert way == [0, 1, 2, 3, 5, 7, 4, 6]


def test_bfs_loop_3(loop_graph: Graph) -> None:
    alg = GraphAlgorithms()
    way = alg.breadth_first_search(loop_graph, 3)
    assert way == [3, 0, 2, 4, 1, 7, 6, 5]


def test_oriented_graph_0(or_graph: Graph) -> None:
    alg = GraphAlgorithms()
    way = alg.breadth_first_search(or_graph, 0)
    assert way == [0, 1, 2, 3, 5, 7, 4, 6]


def test_oriented_graph_3(or_graph: Graph) -> None:
    alg = GraphAlgorithms()
    way = alg.breadth_first_search(or_graph, 3)
    assert way == [3, 4, 6, 7]


def test_oriented_graph_7(or_graph: Graph) -> None:
    alg = GraphAlgorithms()
    way = alg.breadth_first_search(or_graph, 7)
    assert way == [7]

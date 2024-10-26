from python import Graph, GraphAlgorithms


def test_bfs_valid(weighted_graph: Graph) -> None:
    alg = GraphAlgorithms()
    result = alg.get_least_spanning_tree(weighted_graph)
    assert result == [
        [0, 0, 0, 0, 0, 16],
        [0, 0, 0, 0, 0, 15],
        [0, 0, 0, 0, 0, 14],
        [0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 12],
        [16, 15, 14, 4, 12, 0],
    ]


def test_bfs_loop(loop_graph: Graph) -> None:
    alg = GraphAlgorithms()
    way = alg.get_least_spanning_tree(loop_graph)
    assert way == [
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 1, 1, 1, 0],
    ]

from python import Graph, GraphAlgorithms


def test_valid(weighted_graph: Graph) -> None:
    alg = GraphAlgorithms()
    result: float = alg.get_shortest_paths_between_all_vertices(weighted_graph)
    assert result == [
        [0, 29, 20, 20, 16, 31],
        [29, 0, 15, 29, 28, 40],
        [20, 15, 0, 15, 14, 25],
        [20, 29, 15, 0, 4, 12],
        [16, 28, 14, 4, 0, 16],
        [31, 40, 25, 12, 16, 0],
    ]


def test_non_full(non_full_graph: Graph) -> None:
    alg = GraphAlgorithms()
    result: float = alg.get_shortest_paths_between_all_vertices(non_full_graph)
    assert result == [
        [0, 1, 1, 1, 2, 2, 3, float("inf")],
        [1, 0, 1, 2, 2, 1, 2, float("inf")],
        [1, 1, 0, 1, 1, 2, 2, float("inf")],
        [1, 2, 1, 0, 1, 3, 2, float("inf")],
        [2, 2, 1, 1, 0, 2, 1, float("inf")],
        [2, 1, 2, 3, 2, 0, 1, float("inf")],
        [3, 2, 2, 2, 1, 1, 0, float("inf")],
        [
            float("inf"),
            float("inf"),
            float("inf"),
            float("inf"),
            float("inf"),
            float("inf"),
            float("inf"),
            0,
        ],
    ]


def test_loop(loop_graph: Graph) -> None:
    alg = GraphAlgorithms()
    result: float = alg.get_shortest_paths_between_all_vertices(loop_graph)
    assert result == [
        [0, 1, 1, 1, 2, 2, 3, 2],
        [1, 0, 1, 2, 2, 1, 2, 1],
        [1, 1, 0, 1, 1, 2, 2, 1],
        [1, 2, 1, 0, 1, 3, 2, 2],
        [2, 2, 1, 1, 0, 2, 1, 1],
        [2, 1, 2, 3, 2, 0, 1, 1],
        [3, 2, 2, 2, 1, 1, 0, 1],
        [2, 1, 1, 2, 1, 1, 1, 0],
    ]


def test_oriented_graph(weighted_or_graph: Graph) -> None:
    alg = GraphAlgorithms()
    result: float = alg.get_shortest_paths_between_all_vertices(weighted_or_graph)
    assert result == [
        [0, 7, 8, 12, 16, 28, 24, 24],
        [float("inf"), 0, 1, 5, 9, 21, 17, 17],
        [float("inf"), float("inf"), 0, 4, 8, float("inf"), 16, 19],
        [float("inf"), float("inf"), float("inf"), 0, 4, float("inf"), 12, 15],
        [
            float("inf"),
            float("inf"),
            float("inf"),
            float("inf"),
            0,
            float("inf"),
            8,
            11,
        ],
        [float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), 0, 2, 7],
        [
            float("inf"),
            float("inf"),
            float("inf"),
            float("inf"),
            float("inf"),
            float("inf"),
            0,
            9,
        ],
        [
            float("inf"),
            float("inf"),
            float("inf"),
            float("inf"),
            float("inf"),
            float("inf"),
            float("inf"),
            0,
        ],
    ]

import pytest

from python import Graph


@pytest.fixture(scope="session")
def non_weighted_graph():
    g: Graph = Graph()
    g.load_graph_from_file("examples/non_weighted.txt")
    yield g


@pytest.fixture(scope="session")
def weighted_graph():
    g: Graph = Graph()
    g.load_graph_from_file("examples/weighted.txt")
    yield g


@pytest.fixture(scope="session")
def or_graph():
    g: Graph = Graph()
    g.load_graph_from_file("examples/or_graph.txt")
    yield g


@pytest.fixture(scope="session")
def weighted_or_graph():
    g: Graph = Graph()
    g.load_graph_from_file("examples/weighted_or_graph.txt")
    yield g


@pytest.fixture(scope="session")
def non_full_graph():
    g: Graph = Graph()
    g.load_graph_from_file("examples/non_full.txt")
    yield g


@pytest.fixture(scope="session")
def loop_graph():
    g: Graph = Graph()
    g.load_graph_from_file("examples/loop.txt")
    yield g

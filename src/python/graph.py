import logging

logger = logging.getLogger(__name__)


class Graph:
    def __init__(self) -> None:
        self._data = []

    def __getitem__(self, key):
        return self._data[key]

    def __repr__(self) -> str:
        return str(self._data)

    def __len__(self):
        return len(self._data)

    def load_graph_from_file(self, filename: str):
        self._data = []
        with open(filename, "r") as f:
            matrix_size = int(f.readline().strip())
            logger.info(f"matrix size: {matrix_size}")
            for _ in range(matrix_size):
                self._data.append(list(map(int, f.readline().strip().split())))

    def export_graph_to_dot(self, filename: str):
        pass

    def print_graph(self):
        for _ in range(len(self._data)):
            print(" ".join(str(i) for i in self._data[_]))

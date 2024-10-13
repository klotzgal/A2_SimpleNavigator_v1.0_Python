import logging

logger = logging.getLogger(__name__)


class Graph:
    def __init__(self) -> None:
        self.data = []

    def load_graph_from_file(self, filename: str):
        with open(filename, "r") as f:
            matrix_size = int(f.readline().strip())
            logger.info(f"matrix size: {matrix_size}")
            for _ in range(matrix_size):
                self.data.append(f.readline().strip().split())

    def export_graph_to_dot(self, filename: str):
        pass

    def print_graph(self):
        for _ in range(len(self.data)):
            print(" ".join(str(i) for i in self.data[_]))

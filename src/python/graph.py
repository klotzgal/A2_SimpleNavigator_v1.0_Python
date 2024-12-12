import os


class Graph:
    def __init__(self) -> None:
        self._data: list[list[float]] = []

    def __getitem__(self, key: int) -> list[int]:
        return self._data[key]

    def __repr__(self) -> str:
        return str(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def load_graph_from_file(self, filename: str) -> None:
        self._data = []
        if not os.path.exists(filename):
            raise FileNotFoundError
        with open(filename, "r") as f:
            matrix_size = int(f.readline().strip())
            for _ in range(matrix_size):
                self._data.append(list(map(int, f.readline().strip().split())))

    def export_graph_to_dot(self, filename: str) -> None:
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            raise FileNotFoundError(f"{directory} не существует! Создайте")

        graphname = os.path.basename(filename).removesuffix(".txt")
        print(f"Exporting graph to {filename} with graphname {graphname}")
        with open(filename, 'w') as f:
            f.write(f"graph {graphname} \n")
            for i in range(len(self)):
                for j in range(len(self[i])):
                    if (i != j) and self[i][j] != 0:
                        f.write(f"    {i} -- {j};\n")
            f.write("}\n")

    def print_graph(self) -> None:
        for _ in range(len(self._data)):
            print(" ".join(str(i) for i in self._data[_]))

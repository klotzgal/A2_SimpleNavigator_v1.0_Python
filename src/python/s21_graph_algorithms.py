import ctypes
from queue import Queue

from python.graph import Graph


class TsmResult(ctypes.Structure):
    _fields_ = [
        ("vertices", ctypes.POINTER(ctypes.c_void_p)),
        ("distance", ctypes.c_double),
    ]


class GraphAlgorithms:
    # part 1
    def depth_first_search(self, graph: Graph, start_vertex: int) -> list[int]:
        visited: list[bool] = [False for _ in range(len(graph))]
        way: list[int] = []
        # TODO: заменить на плюсовый на стек
        stack: list[int] = [start_vertex]

        while not all(visited) and len(stack):
            vertex = stack.pop()
            if not visited[vertex]:
                visited[vertex] = True
                way.append(vertex)
                for i in range(len(graph)):
                    if graph[vertex][i] != 0 and not visited[i]:
                        stack.append(i)
        return way

    def breadth_first_search(self, graph: Graph, start_vertex: int) -> list[int]:
        dist: list[int] = [float("inf") for _ in range(len(graph))]
        # TODO: заменить на плюсовую очередь
        q: Queue = Queue()
        way: list[int] = []
        dist[start_vertex] = 0
        q.put(start_vertex)

        while not q.empty():
            vertex: int = q.get()
            way.append(vertex)
            for i in range(len(graph)):
                if graph[vertex][i] != 0 and dist[i] == float("inf"):
                    dist[i] = dist[vertex] + graph[vertex][i]
                    q.put(i)
        return way

    # part2
    def get_shortest_path_between_vertices(
        self, graph: Graph, vertex1: int, vertex2: int
    ) -> float:
        dist: list = [float("inf") for _ in range(len(graph))]
        visited: list[bool] = [False for _ in range(len(graph))]
        dist[vertex1] = 0
        vertex: int = vertex1

        while not all(visited):
            visited[vertex] = True
            min_vertex: int = -1
            for i in range(len(graph)):
                if not visited[i] and graph[vertex][i] != 0:
                    if dist[i] > dist[vertex] + graph[vertex][i]:
                        dist[i] = dist[vertex] + graph[vertex][i]

            for i in range(len(graph)):
                if not visited[i]:
                    if min_vertex == -1:
                        min_vertex = i
                    elif dist[i] < dist[min_vertex]:
                        min_vertex = i
            vertex = min_vertex

        return dist[vertex2]

    def get_shortest_paths_between_all_vertices(
        self, graph: Graph
    ) -> list[list[float]]:
        pass

    # part 3
    def get_least_spanning_tree(self, graph: Graph) -> list[list[float]]:
        tree: list[list[float]] = [[0] * len(graph) for _ in range(len(graph))]
        v1: int = 0
        v2: int = 0
        cost: float = 0
        visited: set[int] = {v2}

        while len(visited) < len(graph):
            min_edge: tuple[float, int] = (float("inf"), 0)

            for v1 in visited:
                for v2 in range(len(graph)):
                    if graph[v1][v2] != 0 and v2 not in visited:
                        min_edge = (min(min_edge[0], graph[v1][v2]), v2)

            cost, v2 = min_edge
            tree[v1][v2] = cost
            tree[v2][v1] = cost
            v1 = v2
            visited.add(v2)

        return tree

    # part 4
    def solve_traveling_salesman_problem(self, graph: Graph) -> TsmResult:
        pass

import ctypes
from queue import Queue

from python.graph import Graph


class GraphAlgorithms:
    # part 1
    def depth_first_search(self, graph: Graph, start_vertex: int) -> list[int]:
        visited: list[bool] = [False for _ in range(len(graph))]
        way: list[int] = []
        # TODO: заменить на плюсовый на стек
        stack: list[int] = [start_vertex]

        while not all(visited):
            vertex = stack.pop()
            if not visited[vertex]:
                visited[vertex] = True
                way.append(vertex)
                for i in range(len(graph)):
                    if graph[vertex][i] != 0 and not visited[i]:
                        stack.append(i)
        return way

    def breadth_first_search(self, graph: Graph, start_vertex: int) -> list[int]:
        INF: int = 10**9
        dist: list[int] = [INF for _ in range(len(graph))]
        # TODO: заменить на плюсовую очередь
        q: Queue = Queue()
        way: list[int] = []
        dist[start_vertex] = 0
        q.put(start_vertex)

        while not q.empty():
            vertex: int = q.get()
            way.append(vertex)
            for i in range(len(graph)):
                if graph[vertex][i] != 0 and dist[i] == INF:
                    dist[i] = dist[vertex] + graph[vertex][i]
                    q.put(i)
        return way

    # part2
    def get_shortest_path_between_vertices(self, graph, vertex1, vertex2):
        pass

    def get_shortest_paths_between_all_vertices(self, graph):
        pass

    # part 3
    def get_least_spanning_tree(self, graph):
        pass

    # part 4
    def solve_traveling_salesman_problem(self, graph):
        pass


class TsmResult(ctypes.Structure):
    _fields_ = [
        ("vertices", ctypes.POINTER(ctypes.c_void_p)),
        ("distance", ctypes.c_double),
    ]

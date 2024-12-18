from s21_queue import PyQueue
from s21_stack import PyStack

from python.graph import Graph
from python.ant_colony import TsmResult, AntColonyOptimization


class GraphAlgorithms:
    # part 1
    def depth_first_search(self, graph: Graph, start_vertex: int) -> list[int]:
        visited: list[bool] = [False for _ in range(len(graph))]
        way: list[int] = []
        stack: PyStack = PyStack()
        stack.push(start_vertex)

        while not all(visited) and not stack.empty():
            vertex = stack.top()
            stack.pop()
            if not visited[vertex]:
                visited[vertex] = True
                way.append(vertex)
                for i in range(len(graph)):
                    if graph[vertex][i] != 0 and not visited[i]:
                        stack.push(i)
        return way

    def breadth_first_search(self, graph: Graph, start_vertex: int) -> list[int]:
        dist: list[int] = [float("inf") for _ in range(len(graph))]
        q: PyQueue = PyQueue()
        way: list[int] = []
        dist[start_vertex] = 0
        q.push(start_vertex)

        while not q.empty():
            vertex: int = q.front()
            q.pop()
            way.append(vertex)
            for i in range(len(graph)):
                if graph[vertex][i] != 0 and dist[i] == float("inf"):
                    dist[i] = dist[vertex] + graph[vertex][i]
                    q.push(i)
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
        dist: list[list[float]] = [
            [float("inf")] * len(graph) for _ in range(len(graph))
        ]
        for i in range(len(graph)):
            for j in range(len(graph)):
                if i == j:
                    dist[i][j] = 0
                if graph[i][j] != 0:
                    dist[i][j] = min(dist[i][j], graph[i][j])

        for k in range(len(graph)):
            for i in range(len(graph)):
                for j in range(len(graph)):
                    if dist[i][k] != float("inf") and dist[k][j] != float("inf"):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist

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
        num_vertices = len(graph)
        if num_vertices < 2:
            raise ValueError("The graph must have at least 2 vertices.")

        params = {
            "num_ants": num_vertices,
            "num_iterations": 100,
            "alpha": 1.0,  # Pheromone importance
            "beta": 2.0,  # Heuristic importance
            "rho": 0.5,   # Pheromone evaporation rate
            "q": 1.0      # Pheromone deposit factor
            }

        aco = AntColonyOptimization(graph, **params)
        result = aco.solve()
        return result

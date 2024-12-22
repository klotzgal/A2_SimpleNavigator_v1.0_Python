import random
import ctypes
import numpy as np


class TsmResult(ctypes.Structure):
    _fields_ = [
        ("vertices", ctypes.POINTER(ctypes.c_void_p)),
        ("distance", ctypes.c_double),
    ]


class AntColonyOptimization:
    def __init__(self, graph, num_ants, num_iterations, alpha, beta, rho, q):
        self.graph = graph
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.q = q
        self.num_vertices = len(graph)
        self.pheromone = np.ones((self.num_vertices, self.num_vertices))
        self.distance_matrix = np.array(graph)

    def solve(self):
        best_distance = float('inf')
        best_route = None

        for iteration in range(self.num_iterations):
            routes = []
            distances = []

            for ant in range(self.num_ants):
                route = self.construct_route()
                distance = self.calculate_route_distance(route)
                routes.append(route)
                distances.append(distance)

                if distance < best_distance:
                    best_distance = distance
                    best_route = route

            self.update_pheromone(routes, distances)

        if best_route is None:
            raise ValueError("No valid route found.")

        vertices = (ctypes.c_int * self.num_vertices)(*best_route)
        result = TsmResult(ctypes.cast(vertices, ctypes.POINTER(ctypes.c_void_p)), best_distance)
        return result

    def construct_route(self):
        route = []
        visited = [False] * self.num_vertices
        current_vertex = random.randint(0, self.num_vertices - 1)
        route.append(current_vertex)
        visited[current_vertex] = True

        while len(route) < self.num_vertices:
            probabilities = self.calculate_probabilities(current_vertex, visited)
            next_vertex = np.random.choice(self.num_vertices, p=probabilities)
            route.append(next_vertex)
            visited[next_vertex] = True
            current_vertex = next_vertex

        return route

    def calculate_probabilities(self, current_vertex, visited):
        probabilities = [0] * self.num_vertices
        for vertex in range(self.num_vertices):
            if not visited[vertex] and self.distance_matrix[current_vertex][vertex] > 0:
                probabilities[vertex] = (self.pheromone[current_vertex][vertex] ** self.alpha) * ((1.0 / self.distance_matrix[current_vertex][vertex]) ** self.beta)

        probabilities_sum = sum(probabilities)
        if probabilities_sum == 0:
            raise ValueError("No valid route found.")

        probabilities = [p / probabilities_sum for p in probabilities]
        return probabilities

    def calculate_route_distance(self, route):
        distance = 0
        for i in range(len(route) - 1):
            distance += self.distance_matrix[route[i]][route[i + 1]]
        distance += self.distance_matrix[route[-1]][route[0]]
        return distance

    def update_pheromone(self, routes, distances):
        self.pheromone *= (1 - self.rho)

        for route, distance in zip(routes, distances):
            for i in range(len(route) - 1):
                self.pheromone[route[i]][route[i + 1]] += self.q / distance
            self.pheromone[route[-1]][route[0]] += self.q / distance

import ctypes


class GraphAlgorithms:
    # part 1
    def depth_first_search(self, graph, start_vertex):
        pass

    def breadth_first_search(self, graph, start_vertex):
        pass

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
    _fields_ = [("vertices", ctypes.POINTER(ctypes.c_int_p)), ("distance", ctypes.c_double)]

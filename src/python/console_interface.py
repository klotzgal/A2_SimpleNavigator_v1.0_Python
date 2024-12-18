import sys
from pprint import pprint

from python.graph import Graph
from python.s21_graph_algorithms import GraphAlgorithms


def print_menu() -> None:
    print("Меню:")
    print("1. Загрузить граф из файла")
    print("2. Обход в ширину")
    print("3. Обход в глубину")
    print("4. Найти кратчайший путь между двумя вершинами")
    print("5. Найти кратчайшие пути между всеми парами вершин")
    print("6. Найти минимальное остовное дерево")
    print("7. Решить задачу коммивояжера")
    print("8. Выход")
    print("Введите ваш выбор: ", end="")


def check_user_input(user_input: int) -> tuple[int, bool]:
    result = True
    user_input = 0
    try:
        user_input = int(input())
    except ValueError:
        print("Неверный ввод. Попробуйте еще раз.")
        result = False
    if user_input < 1 or user_input > 8:
        print("Только цифры от 1 до 8")
        result = False
    print("\n================================================\n")
    return user_input, result


def handle_breadth_first_search(graph: Graph, ga: GraphAlgorithms) -> None:
    start_vertex = int(input("Введите начальную точку для обхода: "))
    pprint(ga.breadth_first_search(graph=graph, start_vertex=start_vertex))


def handle_depth_first_search(graph: Graph, ga: GraphAlgorithms):
    start_vertex = int(input("Введите начальную точку для обхода: "))
    pprint(ga.depth_first_search(graph=graph, start_vertex=start_vertex))


def handle_get_shortest_path(graph: Graph, ga: GraphAlgorithms):
    start = int(input("Введите стартовую точку для поиска: "))
    end = int(input("Введите конечную точку для поиска: "))
    pprint(
        ga.get_shortest_path_between_vertices(graph=graph, vertex1=start, vertex2=end)
    )


def graph_program():
    graph = Graph()
    ga = GraphAlgorithms()
    user_input = 0
    while True:
        print_menu()
        user_input, input_valid = check_user_input(user_input)
        if not input_valid:
            continue

        if user_input == 1:
            filename = input("Введите путь к файлу: ")
            graph.load_graph_from_file(filename=filename)
            print("Данные успешно загружены")
        elif user_input == 8:
            print("Программа завершена")
            sys.exit(0)
        else:
            if len(graph) == 0:
                print("\nДанные не загружены. Сначала используйте опцию 1\n")
                print("================================================\n")
                continue

            if user_input == 2:
                handle_breadth_first_search(graph, ga)
            elif user_input == 3:
                handle_depth_first_search(graph, ga)
            elif user_input == 4:
                handle_get_shortest_path(graph, ga)
            elif user_input == 5:
                pprint(ga.get_shortest_paths_between_all_vertices(graph=graph))
            elif user_input == 6:
                pprint(ga.get_least_spanning_tree(graph=graph))
            elif user_input == 7:
                pprint(ga.solve_traveling_salesman_problem(graph=graph))

            print("\n================================================\n")

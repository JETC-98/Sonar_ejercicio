from pilas import initialGraph
from interface import ui

interface_ui = ui()
while True:
    graph = initialGraph()
    edges = graph.update_edges()
    ideal_path = graph.ideal_path()
    path = interface_ui.main_menu()
    graph.chosen_path(path, 0)
    if not interface_ui.feedback(graph.compare_paths(path)):
        print(ideal_path)

    input("Presiona una tecla para continuar...")
    interface_ui.cls()

    if not interface_ui.must_continue():
        break
    interface_ui.cls()
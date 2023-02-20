class Graph:
    def __init__(self):
        self.adj_list = {}

    #=====================================================================================================

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    #=====================================================================================================

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    #=====================================================================================================


add_graph = Graph()
add_graph.add_vertex('A')
add_graph.add_vertex('B')
add_graph.print_graph()

print()


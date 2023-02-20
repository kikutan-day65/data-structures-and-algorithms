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

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    

vertex_graph = Graph()
vertex_graph.add_vertex('A')
vertex_graph.add_vertex('B')
vertex_graph.print_graph()

print()

edge_graph = Graph()
edge_graph.add_vertex(1)
edge_graph.add_vertex(2)
edge_graph.add_edge('D', 'F')
edge_graph.print_graph()
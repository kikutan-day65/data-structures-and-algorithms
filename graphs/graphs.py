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
    
    #=====================================================================================================

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    #=====================================================================================================

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


add_vertex_graph = Graph()
add_vertex_graph.add_vertex('A')
add_vertex_graph.add_vertex('B')
add_vertex_graph.print_graph()

print()

add_edge_graph = Graph()
add_edge_graph.add_vertex('D')
add_edge_graph.add_vertex('F')
add_edge_graph.add_edge('D', 'F')
add_edge_graph.print_graph()

print()

rm_edge_graph = Graph()
rm_edge_graph.add_vertex('A')
rm_edge_graph.add_vertex('B')
rm_edge_graph.add_vertex('C')
rm_edge_graph.add_vertex('D')

rm_edge_graph.add_edge('A', 'B')
rm_edge_graph.add_edge('B', 'C')
rm_edge_graph.add_edge('C', 'A')

rm_edge_graph.remove_edge('A', 'D')

rm_edge_graph.print_graph()

print()

rm_vertex_graph = Graph()
rm_vertex_graph.add_vertex('A')
rm_vertex_graph.add_vertex('B')
rm_vertex_graph.add_vertex('C')
rm_vertex_graph.add_vertex('D')

rm_vertex_graph.add_edge('A', 'B')
rm_vertex_graph.add_edge('A', 'C')
rm_vertex_graph.add_edge('A', 'D')
rm_vertex_graph.add_edge('B', 'D')
rm_vertex_graph.add_edge('C', 'D')

rm_vertex_graph.remove_vertex('D')

rm_vertex_graph.print_graph()
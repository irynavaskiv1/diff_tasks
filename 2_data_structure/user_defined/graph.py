# very simple way
graph = {}
graph["me"] = ["ira", "vaskiv"]
print(graph)


class Graph:
    """full way structure"""

    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def vertices(self):  # вершини
        return list(self.graph_dict.keys())

    def edges(self):  # ребра
        return self.__get_edges()

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = vertex2

    def __get_edges(self):
        edges = []
        for vertex in self.graph_dict:
            for neighbor in self.graph_dict:
                if (vertex, neighbor) not in edges:
                    edges.append({vertex, neighbor})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.graph_dict:
            res += str(k) + "  "
        res += "\nedges"
        for edges in self.__get_edges():
            res += str(edges) + " "
        return res

    def get_path(self, start_vertex, end_vertex, path=None):
        if path is None:
            path = []
        graph = self.graph_dict
        path = path + [start_vertex]
        if start_vertex not in self.graph_dict:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.get_path(vertex, end_vertex, path)
            if extended_path:
                return extended_path
        return None


if __name__ == "__main__":
    g = {
        "a": ["c", "f", "b"],
        "b": ["a", "c", "d"],
        "c": ["f", "a", "b"],
        "d": ["b", "c", "e"],
        "e": ["f", "d"],
        "f": ["e", "c", "a"],
    }
    my_graph = Graph(g)
    print(my_graph.edges())
    print(my_graph.vertices())
    a = my_graph.get_path(start_vertex="a", end_vertex="e")
    print(a)

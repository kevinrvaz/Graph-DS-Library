from graph_interface.graph import Graph
from help_ds.priority_dict import priority_dict
from queue import Queue


class Node(object):
    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.adjacent_set = set()

    def add_edge(self, v, weight):
        if v == self.vertexId:
            raise ValueError("vertex cannot be adjacent to itself")
        self.adjacent_set.add((v, weight))

    def get_adjacent_vertices(self):
        adjacent_vertices = []
        for vertice, _ in self.adjacent_set:
            adjacent_vertices.append(vertice)
        return adjacent_vertices

    def get_edge_weight(self, v):
        for vertice, weight in self.adjacent_set:
            if vertice == v:
                return weight
        return 0


class AdjacentSet(Graph):
    def __init__(self, num_vertices, directed=False):
        super(AdjacentSet, self).__init__(num_vertices, directed)
        self._vertex_list = []
        self._visited = [0]*self.num_vertices
        self._visit_order = []
        for i in range(self.num_vertices):
            self._vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError(f"Vertex v1: {v1} and {v2} are out of bounds")
        self._vertex_list[v1].add_edge(v2, weight)
        if self.directed == False:
            self._vertex_list[v2].add_edge(v1, weight)

    def get_adjacent_vertices(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError(f"Cannot access vertex {v}")
        return self._vertex_list[v].get_adjacent_vertices()

    def get_edge_weight(self, v1, v2):
        return self._vertex_list[v1].get_edge_weight(v2)

    def get_indegree(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError(f"Cannot access vertex {v}")
        indegree = 0
        for i in range(self.num_vertices):
            if v in self.get_adjacent_vertices(i):
                indegree += 1
        return indegree

    def get_outdegree(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError(f"Cannot access vertex {v}")
        return len(self.get_adjacent_vertices(v))

    def breadth_first_search(self, source=0):
        queue = Queue()
        queue.put(source)
        visit_order = []
        while not queue.empty():
            vertex = queue.get()
            if self._visited[vertex] == 1:
                continue
            self._visited[vertex] = 1
            visit_order.append(vertex)
            for v in self.get_adjacent_vertices(vertex):
                if self._visited[v] != 1:
                    queue.put(v)
        self._visited = [0]*self.num_vertices
        return visit_order

    def depth_first_search(self, current=0):
        self._dfs_util(current)
        visit_order = self._visit_order
        self._visit_order = []
        self._visited = [0]*self.num_vertices
        return visit_order

    def _dfs_util(self, current):
        if self._visited[current] == 1:
            return
        self._visited[current] = 1
        self._visit_order.append(current)
        for v in self.get_adjacent_vertices(current):
            self._dfs_util(v)

    def display(self):
        for i in range(self.num_vertices):
            for j in self.get_adjacent_vertices(i):
                print(i, "--->", j, "weight", self.get_edge_weight(i, j))

    def shortest_path_unweighted(self, source, destination):
        pass

    def shortest_path_weighted(self, source, destination):
        pass

    def topological_sort(self):
        queue = Queue()
        indegree_map = {}
        for i in range(self.num_vertices):
            indegree_map[i] = self.get_indegree(i)
            if indegree_map[i] == 0:
                queue.put(i)

        sorted_list = []
        while not queue.empty():
            vertex = queue.get()
            sorted_list.append(vertex)
            for v in self.get_adjacent_vertices(vertex):
                indegree_map[v] -= 1
                if indegree_map[v] == 0:
                    queue.put(v)
        if len(sorted_list) != self.num_vertices:
            raise ValueError("The graph has a cycle")
        return sorted_list

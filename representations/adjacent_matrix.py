'''
Author: Kevin Rohan Vaz

Description: Implements the methods present in the Graph Interface using an adjacency matrix representation

Usage: create an object of the AdjacentMatrix class and call it's methods on the object.
       example:- 

'''
from graph_interface.graph import Graph
from help_ds.priority_dict import priority_dict
from queue import Queue


class AdjacentMatrix(Graph):
    def __init__(self, num_vertices, matrix=[], directed=False):
        super(AdjacentMatrix, self).__init__(num_vertices, directed)
        self._matrix = matrix
        if len(self._matrix) == 0:
            for _ in range(self.num_vertices):
                self._matrix.append([0]*self.num_vertices)
        self._visited = [0]*self.num_vertices
        self._visit_order_dfs = []

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError(f"Vertex v1: {v1} and v2: {v2} are out of bounds")
        self._matrix[v1][v2] = weight
        if self.directed == False:
            self._matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError(f"Cannot access vertex {v}")
        adjacent_vertices = []
        for i in range(self.num_vertices):
            if self._matrix[v][i] > 0:
                adjacent_vertices.append(i)
        return adjacent_vertices

    def get_indegree(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError(f"Cannot access vertex {v}")
        indegree = 0
        for i in range(self.num_vertices):
            if self._matrix[i][v] > 0:
                indegree += 1
        return indegree

    def get_outdegree(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError(f"Cannot access vertes {v}")
        return len(self.get_adjacent_vertices(v))

    def get_edge_weight(self, v1, v2):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError(f"Vertex v1: {v1} and v2: {v2} are out of bounds")
        return self._matrix[v1][v2]

    def breadth_first_search(self, source=0):
        queue = Queue()
        queue.put(source)
        visit_order = []
        visited = [0]*self.num_vertices
        while not queue.empty():
            vertex = queue.get()
            if visited[vertex] == 1:
                continue
            visit_order.append(vertex)
            visited[vertex] = 1
            for v in self.get_adjacent_vertices(vertex):
                if visited[v] != 1:
                    queue.put(v)
        return visit_order

    def depth_first_search(self, current=0):
        self._dfs_util(current)
        visit_order = self._visit_order_dfs
        self._visit_order_dfs = []
        self._visited = [0]*self.num_vertices
        return visit_order

    def _dfs_util(self, current=0):
        if self._visited[current] == 1:
            return
        self._visit_order_dfs.append(current)
        self._visited[current] = 1
        for v in self.get_adjacent_vertices(current):
            self._dfs_util(v)

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
                indegree_map[i] -= 1
                if indegree_map[i] == 0:
                    queue.put(v)
        if len(sorted_list) != self.num_vertices:
            raise ValueError("Graph has a cycle")
        return sorted_list

    def shortest_path_unweighted(self, source, destination):
        distance_table = self._build_distance_table_unweighted(source)
        path = [destination]
        previous_vertex = distance_table[destination][1]
        while previous_vertex is not None and previous_vertex is not source:
            path = [previous_vertex]+path
            previous_vertex = distance_table[previous_vertex][1]
        if previous_vertex is None:
            raise ValueError(
                f"No path between source: {source} and destination: {destination}")
        return [source]+path

    def _build_distance_table_unweighted(self, source):
        distance_table = {}
        for i in range(self.num_vertices):
            distance_table[i] = (None, None)
        distance_table[source] = (0, source)
        queue = Queue()
        queue.put(source)
        while not queue.empty():
            current_vertex = queue.get()
            current_distance = distance_table[current_vertex][0]
            for neighbor in self.get_adjacent_vertices(current_vertex):
                if distance_table[neighbor][0] is None:
                    distance_table[neighbor] = (
                        current_distance+1, current_vertex)
                if len(self.get_adjacent_vertices(neighbor)) > 0 and self._visited[neighbor] != 1:
                    self._visited[neighbor] = 1
                    queue.put(neighbor)
        self._visited = [0]*self.num_vertices
        return distance_table

    def shortest_path_weighted(self, source, destination):
        distance_table = self._build_distance_table_weighted(source)
        path = [destination]
        previous_vertex = distance_table[destination][1]
        while previous_vertex is not None and previous_vertex is not source:
            path = [previous_vertex]+path
            previous_vertex = distance_table[previous_vertex][1]
        if previous_vertex is None:
            raise ValueError(f"No path between {source} and {destination}")
        return [source]+path

    def _build_distance_table_weighted(self, source):
        distance_table = {}
        for i in range(self.num_vertices):
            distance_table[i] = (None, None)
        distance_table[source] = (0, source)
        priority_queue = priority_dict()
        priority_queue[source] = 0
        while len(priority_queue.keys()) > 0:
            current_vertex = priority_queue.pop_smallest()
            current_distance = distance_table[current_vertex][0]
            for neighbor in self.get_adjacent_vertices(current_vertex):
                distance = current_distance + \
                    self.get_edge_weight(current_vertex, neighbor)
                neighbor_distance = distance_table[neighbor][0]
                if neighbor_distance is None or neighbor_distance > distance:
                    distance_table[neighbor] = (distance, current_vertex)
                    priority_queue[neighbor] = distance
        return distance_table

    def display(self):
        for i in range(self.num_vertices):
            for j in self.get_adjacent_vertices(i):
                print(i, "--->", j)

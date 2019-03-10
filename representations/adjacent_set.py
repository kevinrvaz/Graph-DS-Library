'''
Author: Kevin Rohan Vaz

Description: Implements the methods present in the Graph Interface using an adjacency set representation

Usage: create an object of the AdjacentMatrix class and call it's methods on the object.
       example:- 

'''
from graph_interface.graph import Graph
from help_ds.priority_dict import priority_dict
from queue import Queue


class Node(object):
    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.adjacent_set = set()
        self.weight_list = {}

    def add_edge(self, v, weight):
        if v == self.vertexId:
            raise ValueError("vertex cannot be adjacent to itself")
        self.adjacent_set.add(v)
        self.weight_list[v] = weight

    def get_adjacent_vertices(self):
        return self.adjacent_set

    def get_edge_weight(self, v):
        if v in self.adjacent_set:
            return self.weight_list[v]
        return 1


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
        distance_table = self._build_table_weighted(source)
        path = [destination]
        previous_vertex = distance_table[destination][1]
        while previous_vertex is not source and previous_vertex is not None:
            path = [previous_vertex]+path
            previous_vertex = distance_table[previous_vertex][1]
        if previous_vertex is None:
            return []
        return [source]+path

    def _build_table_weighted(self, source):
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
                distance = self.get_edge_weight(
                    current_vertex, neighbor) + current_distance
                neighbor_distance = distance_table[neighbor][0]
                if neighbor_distance is None or neighbor_distance > distance:
                    distance_table[neighbor] = (distance, current_vertex)
                    priority_queue[neighbor] = distance
        return distance_table

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

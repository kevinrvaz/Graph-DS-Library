'''
Author: Kevin Rohan Vaz

Description: Implements the methods present in the Graph Interface using an adjacency set representation

Usage: create an object of the AdjacentSet class and call it's methods on the object.
       example:- 
       consider graph as shown below:
       
       (0)******(1)*
       *         *  *
       *         *   (4)
       *         *  *
       (2)******(3)*

        1. Initialization:
           graph=AdjacentSet(no_of_vertices,directed)

        2. Calling graph methods
           graph.breadth_first_search(source) returns [0,1,2,3,4]

'''
from graph_interface.graph import Graph


class Node(object):
    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.adjacent_set = set()
        self.weight_list = {}

    def add_edge(self, v, weight):
        # if v == self.vertexId:
            # raise ValueError("vertex cannot be adjacent to itself")
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

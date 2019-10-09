'''
Author: excalibur-kvrv, modhtanmay 

Description: Implements the methods present in the GraphAlgorithms Interface using appropriate graph representation.

Usage: create an object of the AdjacentMatrix class and call it's methods on the object.
       consider the graph as Shown below:  
      
      (0)******(1)*
       *         *  *
       *         *   (4)
       *         *  *
       (2)******(3)*

       INITIALIZATION:
       graph=Graph(num_vertices) #Takes an optional argument rep which specifies the type of representation to use.
       
       CALLING GRAPH ALGORITHMS:
       graph.breadth_first_search(0) #Returns a list of visited vertices using bfs traversal.
       graph.depth_first_search(0) #Returns a list of visited vertices using dfs traversal
       graph.topological_sort() #Returns a list of visited vertices satisfying all precedence relationships.
       graph.shortest_path_unweighted(0,1) #Returns the shortest path between source and destination for an unweighted graph.
       graph.shortest_path_weighted(0,1) #Returns the shortest path using djisktra's algorithm between source and destination for a weighted graph.
       graph.minimum_cost(0,1) #Returns an int that is the minimum cost b/w source and destination
       graph.minimum_spanning_tree_prim() #Returns a spanning tree list from source for non-isolated graphs
       graph.minimum_spanning_tree_kruskal() #Returns a spanning tree list from source for disconnected graphs
       
       CALLING GRAPH PROPERTIES:
       graph.prop.add_edge(0,1,2) #This adds an edge of weight 2 between vertices 0 and 1.
       graph.prop.get_adjacent_vertices(0) #This returns a list of adjacent vertices to vertex 0.
       graph.prop.get_edge_weight(0,1) #This returns the weight of the edge between 0 and 1.
       graph.prop.get_indegree(0) #This returns the indegree of vertex 0.
       graph.prop.get_outdegree(0) #This returns the outdegree of vertex 0. 
       graph.prop.display() #This returns the set of edges of the graph with its weights.

'''

from help_ds.priority_dict import priority_dict
from graph_interface.graph_algorithms import GraphAlgorithms
from queue import Queue


class Graph(GraphAlgorithms):
    def __init__(self, num_vertices, rep="AdjacentMatrix", matrix=[], directed=False):
        super(Graph, self).__init__(num_vertices, rep, matrix, directed)

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
            for v in self.prop.get_adjacent_vertices(vertex):
                if self._visited[v] != 1:
                    queue.put(v)
        self._visited = [0]*self.prop.num_vertices
        return visit_order

    def depth_first_search(self, current=0):
        self._dfs_util(current)
        visit_order = self.prop._visit_order
        self._visit_order = []
        self._visited = [0]*self.prop.num_vertices
        return visit_order

    def _dfs_util(self, current):
        if self._visited[current] == 1:
            return
        self._visited[current] = 1
        self._visit_order.append(current)
        for v in self.prop.get_adjacent_vertices(current):
            self._dfs_util(v)

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
        for i in range(self.prop.num_vertices):
            distance_table[i] = (None, None)
        distance_table[source] = (0, source)
        queue = Queue()
        queue.put(source)
        while not queue.empty():
            current_vertex = queue.get()
            current_distance = distance_table[current_vertex][0]
            for neighbor in self.prop.get_adjacent_vertices(current_vertex):
                if distance_table[neighbor][0] is None:
                    distance_table[neighbor] = (
                        current_distance+1, current_vertex)
                if len(self.prop.get_adjacent_vertices(neighbor)) > 0 and self._visited[neighbor] != 1:
                    self._visited[neighbor] = 1
                    queue.put(neighbor)
        self._visited = [0]*self.prop.num_vertices
        return distance_table

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
        for i in range(self.prop.num_vertices):
            distance_table[i] = (None, None)
        distance_table[source] = (0, source)
        priority_queue = priority_dict()
        priority_queue[source] = 0
        while len(priority_queue.keys()) > 0:
            current_vertex = priority_queue.pop_smallest()
            current_distance = distance_table[current_vertex][0]
            for neighbor in self.prop.get_adjacent_vertices(current_vertex):
                distance = self.prop.get_edge_weight(
                    current_vertex, neighbor) + current_distance
                neighbor_distance = distance_table[neighbor][0]
                if neighbor_distance is None or neighbor_distance > distance:
                    distance_table[neighbor] = (distance, current_vertex)
                    priority_queue[neighbor] = distance
        return distance_table

    def topological_sort(self):
        queue = Queue()
        indegree_map = {}
        for i in range(self.prop.num_vertices):
            indegree_map[i] = self.prop.get_indegree(i)
            if indegree_map[i] == 0:
                queue.put(i)

        sorted_list = []
        while not queue.empty():
            vertex = queue.get()
            sorted_list.append(vertex)
            for v in self.prop.get_adjacent_vertices(vertex):
                indegree_map[v] -= 1
                if indegree_map[v] == 0:
                    queue.put(v)
        if len(sorted_list) != self.prop.num_vertices:
            raise ValueError("The graph has a cycle")
        return sorted_list

    def minimum_cost(self, source, destination):
        path = self.shortest_path_weighted(source, destination)
        min_cost = 0
        for i in range(0, len(path)-1):
            min_cost += self.prop.get_edge_weight(path[i], path[i+1])
        return min_cost

    def minimum_spanning_tree_prim(self, source):
        pass

    def minimum_spanning_tree_kruskal(self, source):
        pass

    def display(self):
        for i in range(self.prop.num_vertices):
            for j in self.prop.get_adjacent_vertices(i):
                print(i, "--->", j, "weight", self.prop.get_edge_weight(i, j))

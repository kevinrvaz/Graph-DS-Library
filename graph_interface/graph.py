'''
Author: Kevin Rohan Vaz

Usage: Defines an interface for the graph data structure, for detailed information on methods read the comments within that abstract method/property

Interface Abstract Methods: 1. add_edge(self,v1,v2,weight=1)
                            2. get_adjacent_vertices(self,v)
                            3. get_indegree(self,v)
                            4. get_outdegree(self,v)
                            5. get_edge_weight(self,v1,v2)
                            6. breadth_first_search(self,source)
                            7. depth_first_search(self,current)
                            8. topological_sort(self)
                            9. shortest_path_unweighted(self,source,destination)
                            10. shortest_path_unweighted(self,source,destination) 
                            11. display(self)

'''
import abc


class Graph(abc.ABC):
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight=1):
        '''Adds an edge to the graph'''
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        '''Gets a list of adjacent vertices to v'''
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        '''Returns the indegree of v'''
        pass

    @abc.abstractmethod
    def get_outdegree(self, v):
        '''Returns the outdegree of v'''
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        '''Return the weight of edge between v1 and v2 '''
        pass

    @abc.abstractmethod
    def breadth_first_search(self, source):
        '''Returns a list of visited vertices using bfs traversal'''
        pass

    @abc.abstractmethod
    def depth_first_search(self, current):
        '''Returns a list of visited vertices using dfs traversal'''
        pass

    @abc.abstractmethod
    def topological_sort(self):
        '''Returns a list of visited vertices satisfying all precedence relationships.'''
        pass

    @abc.abstractmethod
    def shortest_path_unweighted(self, source, destination):
        '''Returns the shortest path between source and destination for an unweighted graph.'''
        pass

    @abc.abstractmethod
    def shortest_path_weighted(self, source,destination):
        '''Returns the shortest path using djisktra's algorithm between source and destination for a weighted graph.'''
        pass

    @abc.abstractmethod
    def display(self):
        '''Used for printing a graph'''
        pass

'''
Author: Kevin Rohan Vaz

Usage: Defines an interface for the graph data structure, for detailed information on methods read the comments within that abstract method/property

Interface Abstract Methods: 1. add_edge(self,v1,v2,weight=1)
                            2. get_adjacent_vertices(self,v)
                            3. get_indegree(self,v)
                            4. get_outdegree(self,v)
                            5. get_edge_weight(self,v1,v2)
                            6. display(self)
                            
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
        '''Gets a list of vertices adjacent to v'''
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

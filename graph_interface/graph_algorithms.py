from representations.adjacent_matrix import AdjacentMatrix
from representations.adjacent_set import AdjacentSet
import abc


class GraphAlgorithms(abc.ABC):
    def __init__(self, num_vertices, rep, matrix, directed):
        if rep == "AdjacentMatrix":
            self.graph = AdjacentMatrix(num_vertices, matrix, directed)
        elif rep == "AdjacentSet":
            self.graph = AdjacentSet(num_vertices, directed)

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
    def shortest_path_weighted(self, source, destination):
        '''Returns the shortest path using djisktra's algorithm between source and destination for a weighted graph.'''
        pass

    @abc.abstractmethod
    def minimum_cost(self, source, destination):
        '''Returns an int that is the minimum cost b/w source and destination'''
        pass

    @abc.abstractmethod
    def minimum_spanning_tree_prim(self, source):
        '''Returns a spanning tree list from source for non-isolated graphs'''
        pass

    @abc.abstractmethod
    def minimum_spanning_tree_kruskal(self, source):
        '''Returns a spanning tree list from source for disconnected graphs '''
        pass

    @abc.abstractmethod
    def display(self):
        '''Printing the graph'''
        pass

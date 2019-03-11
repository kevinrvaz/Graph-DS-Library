# from representations.adjacent_set import AdjacentSet
# from representations.adjacent_matrix import AdjacentMatrix
from matrix import matrix
# import sys
# graph=AdjacentMatrix(300,matrix,directed=False)
# print(f"path between 0 and 292")
# for node in graph.shortest_path_weighted(0,268):
    # print(node)

# graph=AdjacentMatrix(5,directed=False)
# # sys.setrecursionlimit(10000)
# graph.add_edge(0,1)
# graph.add_edge(0,2)
# graph.add_edge(1,3)
# graph.add_edge(1,4)

# for node in graph.shortest_path_unweighted(0,4):
    # print(node)
'''
graph=AdjacentSet(5,True)
graph.add_edge(0,1,2)    
graph.add_edge(0,2,4)    
graph.add_edge(2,3,2)    
graph.add_edge(3,1,1)    
graph.add_edge(3,4,1)    
graph.add_edge(1,4,1)

graph.display()

for node in graph.shortest_path_weighted(2,4):
    print(node,end=" ")
print()
for node in graph.breadth_first_search():
    print(node,end=" ")
print()
for node in graph.depth_first_search():
    print(node,end=" ")
print()
for node in graph.topological_sort():
    print(node,end=" ")
print()
'''
from algorithms.graph_algorithms import Graph

graph=Graph(300,matrix=matrix,directed=False)
graph.display()
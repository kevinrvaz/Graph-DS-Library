from adjacent_matrix import AdjacentMatrix
from matrix import matrix
# import sys
graph=AdjacentMatrix(300,matrix,directed=False)
print(f"path between 0 and 292")
for node in graph.shortest_path_weighted(0,268):
    print(node)

# graph=AdjacentMatrix(5,directed=False)
# # sys.setrecursionlimit(10000)
# graph.add_edge(0,1)
# graph.add_edge(0,2)
# graph.add_edge(1,3)
# graph.add_edge(1,4)

# for node in graph.shortest_path_unweighted(0,4):
    # print(node)
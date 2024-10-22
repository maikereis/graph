# Implementation of Depth-First Search
# Sedgewick, Robert. 2010. Algorithms in Java Pt. 5 Graph Algorithms. 3. ed., 7. print. Boston, Mass. [u.a.]: Addison-Wesley.
# 
# procedure DFS_iterative(G, v) is
#     let S be a stack
#     label v as discovered
#     S.push(iterator of G.adjacentEdges(v))
#     while S is not empty do
#         if S.peek().hasNext() then
#             w = S.peek().next()
#             if w is not labeled as discovered then
#                 label w as discovered
#                 S.push(iterator of G.adjacentEdges(w))
#         else
#             S.pop()

from typing import Dict, List, Set
from collections import deque

def dfs(G: Dict[str, List[str]], start_vertex: str) -> Set[str]:
    """
    Perform an iterative depth-first search (DFS) on a graph.

    Parameters
    ----------
    G : dict
        The graph represented as an adjacency list where keys are vertices and values are lists of adjacent vertices.
    start_vertex : str
        The starting vertex for the DFS.

    Returns
    -------
    discovered : set
        A set of vertices that were discovered during the DFS.

    Examples
    --------
    >>> G = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []}
    >>> dfs(G, 'A')
    {'A', 'B', 'C', 'D', 'E', 'F'}
    """

    if start_vertex not in G.keys():
        return set()

    S = deque()
    discovered = set()
    discovered.add(start_vertex)  # Label as discovered
    # Initialize with start vertex's iterator
    S.append(iter(G[start_vertex]))

    while S:
        try:
            # Get the next adjacent vertex
            w = next(S[-1])
            if w not in discovered:
                discovered.add(w)  # Label as discovered
                S.append(iter(G[w]))
        except StopIteration:
            # If there are no more vertices, pop the stack
            S.pop()
    return discovered


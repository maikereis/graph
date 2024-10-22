from ._base import Graph
from .searching import dfs

def reverse(graph) -> 'Graph':
        """
        Reverse the directed graph.

        Returns
        -------
        Graph
            A new graph with all edges reversed.
        """
        reversed_graph = Graph()
        
        for src in graph.keys():
            for dst in graph.get(src, []):
                reversed_graph.add_edge(dst, src)
        
        return reversed_graph

def extract_genealogical_subgraph(graph, start_vertex):
    """
    Extracts a genealogical subgraph starting from a given vertex.

    This function constructs a subgraph representing the genealogical tree 
    of a specified start vertex, including all descendant and ancestor nodes.
    It uses depth-first search (DFS) to traverse the graph and builds a subgraph 
    that includes both children and parent relationships.

    Parameters
    ----------
    graph : Graph
        The original graph containing all nodes and edges.
    start_vertex : hashable
        The starting vertex from which the genealogical tree will be constructed.

    Returns
    -------
    Graph
        A subgraph containing the genealogical tree of the given start vertex, 
        including both descendant and ancestor nodes.

    Notes
    -----
    - The `add_children` function adds child nodes of a given node to the subgraph.
    - The `add_parents` function finds parent nodes by reversing the input graph
      and adding their children to the subgraph.
    - Uses an iterative DFS approach to traverse nodes.

    """
    sub_tree = Graph()

    def add_children(src_graph, dst_graph, start_node):
        for node in dfs(src_graph, start_node):
            for child in src_graph.get(node, []):
                if child not in dst_graph[node]:
                    dst_graph.add_edge(node, child)

    def add_parents(src_graph, dst_graph, start_node):
        reversed_g1 = reverse(src_graph)
        for node in dfs(reversed_g1, start_node):
            if node != start_node and node is not None:
                add_children(src_graph, dst_graph, node)

    add_children(graph, sub_tree, start_node=start_vertex)
    add_parents(graph, sub_tree, start_node=start_vertex)

    return sub_tree
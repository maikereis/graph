from collections import defaultdict

class Graph:
    """
    A class to represent a directed graph using an adjacency list.

    Attributes
    ----------
    graph : defaultdict
        A dictionary to store the graph as an adjacency list,
        where keys are the source vertices and values are lists of destination vertices.

    Methods
    -------
    add_edge(src_vertex, dst_vertex):
        Adds a directed edge from `src_vertex` to `dst_vertex`.
    """

    def __init__(self):
        """
        Initializes an empty graph represented as an adjacency list.
        """
        self.graph = defaultdict(list)
    
    def add_edge(self, src_vertex, dst_vertex):
        """
        Adds a directed edge from `src_vertex` to `dst_vertex`.

        Parameters
        ----------
        src_vertex : any hashable type
            The source vertex from which the edge starts.
        dst_vertex : any hashable type
            The destination vertex to which the edge points.
        
        Examples
        --------
        >>> g = Graph()
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 2)
        >>> print(g.graph)
        defaultdict(<class 'list'>, {0: [1, 2]})
        """
        if src_vertex is None or dst_vertex is None:
            return
        self.graph[src_vertex].append(dst_vertex)

    def all_nodes(self):
        """Get all nodes in the graph.

        This method returns a set containing all unique nodes in the graph,
        including both the source nodes and destination nodes.

        Returns
        -------
        set
            A set of all unique nodes in the graph, combining the keys of
            the adjacency list (source nodes) and the edges (destination nodes).

        Examples
        --------
        >>> g = Graph()
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 2)
        >>> g.add_edge(1, 2)
        >>> g.all_nodes()
        {0, 1, 2}
        """
        return set(self.graph.keys()).union({edge for edges in self.graph.values() for edge in edges})
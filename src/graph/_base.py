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
        """
        if src_vertex not in self.graph:
            self.graph[src_vertex] = []
        self.graph[src_vertex].append(dst_vertex)

    def remove_edge(self, src_vertex, dst_vertex):
        """
        Remove a directed edge from `src_vertex` to `dst_vertex`.

        Parameters
        ----------
        src_vertex : any hashable type
            The source vertex from which the edge starts.
        dst_vertex : any hashable type
            The destination vertex to which the edge points.
        """
        if src_vertex in self.graph and dst_vertex in self.graph[src_vertex]:
            self.graph[src_vertex].remove(dst_vertex)

    def add_vertex(self, vertex):
        """
        Add a `vertex` to graph.

        Parameters
        ----------
        vertex : any hashable type
            The vertex to be added.
        """
        if vertex not in self.graph:
            self.graph[vertex] = []

    def remove_vertex(self, vertex):
        """
        Remove a `vertex` from graph.

        Parameters
        ----------
        vertex : any hashable type
            The vertex to be removed.
        """
        if vertex in self.graph:
            del self.graph[vertex]
            for v in self.graph:
                if vertex in self.graph[v]:
                    self.graph[v].remove(vertex)

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
        >>> g.add_edge(1, 3)
        >>> g.all_nodes()
        {0, 1, 2, 3}
        """
        return set(self.graph.keys()).union({edge for edges in self.graph.values() for edge in edges})
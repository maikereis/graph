from collections import defaultdict
from typing import List, Set, Dict, Any

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
        self._graph = defaultdict(list)
        
    def __getitem__(self, vertex):
        """
        Returns the adjacent vertices for the given `vertex`.

        Parameters
        ----------
        vertex : any hashable type
            The vertex to get the adjacent vertices for.

        Returns
        -------
        list
            A list of adjacent vertices.
        """
        return self._graph[vertex]
    
    def __setitem__(self, vertex, edges):
        """
        Sets the adjacent vertices for the given `vertex`.

        Parameters
        ----------
        vertex : any hashable type
            The vertex to set the adjacent vertices for.
        edges : list
            A list of adjacent vertices to set for the given vertex.
        """
        self._graph[vertex] = edges
    
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
        if src_vertex not in self._graph:
            self._graph[src_vertex] = []
        self._graph[src_vertex].append(dst_vertex)

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
        if src_vertex in self._graph and dst_vertex in self._graph[src_vertex]:
            self._graph[src_vertex].remove(dst_vertex)

    def add_vertex(self, vertex):
        """
        Add a `vertex` to graph.

        Parameters
        ----------
        vertex : any hashable type
            The vertex to be added.
        """
        if vertex not in self._graph:
            self._graph[vertex] = []

    def remove_vertex(self, vertex):
        """
        Remove a `vertex` from graph.

        Parameters
        ----------
        vertex : any hashable type
            The vertex to be removed.
        """
        if vertex in self._graph:
            del self._graph[vertex]
            for v in self._graph:
                if vertex in self._graph[v]:
                    self._graph[v].remove(vertex)

    def get(self, vertex: Any, default: Any = None) -> List:
        """
        Returns the adjacent vertices for the given `vertex` or `default` if the vertex is not found.

        Parameters
        ----------
        vertex : any hashable type
            The vertex to get the adjacent vertices for.
        default : any type, optional
            The value to return if the vertex is not found.

        Returns
        -------
        list
            A list of adjacent vertices or the default value.
        """
        return self._graph.get(vertex, default)
    
    def keys(self) -> List:
        """
        Returns the keys (source vertices) of the graph.

        Returns
        -------
        list
            A list of source vertices.
        """
        return list(self._graph.keys())
    
    def values(self) -> List:
        """
        Returns the values (destination vertices lists) of the graph.

        Returns
        -------
        list
            A list of lists of destination vertices.
        """
        return list(self._graph.values())

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
        return set(self._graph.keys()).union({edge for edges in self._graph.values() for edge in edges})
import pytest
from collections import defaultdict
from src.graph import Graph  # Replace this with the correct import path of your Graph class


def test_graph_initialization():
    """
    Test the initialization of the Graph class.

    Ensures that a newly created graph has an empty 
    defaultdict as its internal representation and that 
    the graph starts with no vertices.
    """
    g = Graph()
    assert isinstance(g._graph, defaultdict)
    assert len(g._graph) == 0

def test_add_edge():
    """
    Test adding a directed edge to the graph.

    Verifies that adding an edge from 'A' to 'B' correctly 
    adds 'B' to 'A's adjacency list and includes 'B' as 
    a vertex with an empty adjacency list.
    """
    g = Graph()
    g.add_edge("A", "B")
    assert g["A"] == ["B"]
    assert "B" in g._graph
    assert g["B"] == []

def test_add_edge_existing_vertex():
    """
    Test adding multiple edges from the same source vertex.

    Ensures that adding edges from 'A' to 'B' and 'A' to 'C'
    correctly updates 'A's adjacency list to include both 
    'B' and 'C'.
    """
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    assert g["A"] == ["B", "C"]

def test_remove_edge():
    """
    Test removing an existing edge from the graph.

    Ensures that after removing an edge from 'A' to 'B', 
    'A's adjacency list no longer contains 'B'.
    """
    g = Graph()
    g.add_edge("A", "B")
    g.remove_edge("A", "B")
    assert g["A"] == []

def test_remove_nonexistent_edge():
    """
    Test removing a non-existent edge from the graph.

    Verifies that attempting to remove an edge that does 
    not exist ('A' to 'C') does not alter the adjacency 
    list of 'A' when 'A' is already connected to 'B'.
    """
    g = Graph()
    g.add_edge("A", "B")
    g.remove_edge("A", "C")  # Removing a non-existing edge should do nothing
    assert g["A"] == ["B"]

def test_add_vertex():
    """
    Test adding a vertex to the graph.

    Ensures that adding a vertex 'A' adds 'A' as a key in 
    the graph with an empty adjacency list.
    """
    g = Graph()
    g.add_vertex("A")
    assert "A" in g._graph
    assert g["A"] == []

def test_remove_vertex():
    """
    Test removing a vertex from the graph.

    Verifies that removing a vertex 'A' also removes it 
    from the graph while retaining the adjacency lists of 
    other vertices like 'B'.
    """
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.remove_vertex("A")
    assert "A" not in g._graph
    assert "B" in g._graph
    assert g["B"] == ["C"]

def test_remove_vertex_with_incoming_edges():
    """
    Test removing a vertex with incoming edges.

    Ensures that removing vertex 'B' also removes any 
    references to 'B' in the adjacency lists of other 
    vertices like 'A' and 'C'.
    """
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("C", "B")
    g.remove_vertex("B")
    assert "B" not in g._graph
    assert g["A"] == []
    assert g["C"] == []

def test_get():
    """
    Test retrieving adjacency lists using the get method.

    Ensures that calling get() retrieves the adjacency list 
    for an existing vertex or returns a specified default 
    value if the vertex is not present in the graph.
    """
    g = Graph()
    g.add_edge("A", "B")
    assert g.get("A") == ["B"]
    assert g.get("B", []) == []
    assert g.get("C", "default") == "default"

def test_keys():
    """
    Test retrieving all keys (vertices) from the graph.

    Ensures that calling keys() returns a set of all vertices 
    present in the graph.
    """
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    assert set(g.keys()) == {"A", "B", "C"}

def test_values():
    """
    Test retrieving all adjacency lists from the graph.

    Ensures that calling values() returns the adjacency lists 
    of all vertices in the order they were added.
    """
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    assert g.values() == [['B'], ['C'], []]

def test_all_nodes():
    """
    Test retrieving all nodes (vertices) from the graph.

    Ensures that all_nodes() returns a set of all vertices, 
    including those without outgoing edges.
    """
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("D", "E")
    assert g.all_nodes() == {"A", "B", "C", "D", "E"}

def test_setitem():
    """
    Test setting the adjacency list for a vertex using item assignment.

    Verifies that using item assignment to set the adjacency list 
    for vertex 'A' correctly updates its list of adjacent vertices.
    """
    g = Graph()
    g["A"] = ["B", "C"]
    assert g["A"] == ["B", "C"]

def test_getitem():
    """
    Test retrieving the adjacency list for a vertex using item access.

    Ensures that using item access retrieves the correct adjacency 
    list for an existing vertex, and returns an empty list for a 
    vertex that has no adjacent vertices.
    """
    g = Graph()
    g.add_edge("A", "B")
    assert g["A"] == ["B"]
    assert g["B"] == []

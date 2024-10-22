import pytest
from src.graph import Graph
from src.graph.utils import reverse  # Replace with the correct import path of your Graph class and reverse function

def test_reverse_empty_graph():
    """
    Test reversing an empty graph.

    Ensures that reversing an empty graph returns another empty graph 
    with no vertices and no edges.
    """
    g = Graph()
    reversed_g = reverse(g)
    assert len(reversed_g.keys()) == 0

def test_reverse_single_edge():
    """
    Test reversing a graph with a single edge.

    Ensures that reversing a graph with an edge from 'A' to 'B' results 
    in a graph with an edge from 'B' to 'A'.
    """
    g = Graph()
    g.add_edge("A", "B")
    reversed_g = reverse(g)
    assert reversed_g["B"] == ["A"]
    assert reversed_g["A"] == []

def test_reverse_multiple_edges():
    """
    Test reversing a graph with multiple edges.

    Verifies that reversing a graph with edges from 'A' to 'B' and 
    'A' to 'C' results in 'B' and 'C' having edges back to 'A'.
    """
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    reversed_g = reverse(g)
    assert reversed_g["B"] == ["A"]
    assert reversed_g["C"] == ["A"]
    assert reversed_g["A"] == []

def test_reverse_bidirectional_edges():
    """
    Test reversing a graph with bidirectional edges.

    Ensures that reversing a graph with edges 'A' to 'B' and 'B' to 'A' 
    results in a graph with the same edges.
    """
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "A")
    reversed_g = reverse(g)
    assert reversed_g["A"] == ["B"]
    assert reversed_g["B"] == ["A"]

def test_reverse_disconnected_graph():
    """
    Test reversing a graph with disconnected vertices.

    Verifies that reversing a graph where 'A' has an edge to 'B', 
    and 'C' is a disconnected vertex results in a graph where 
    'B' has an edge to 'A', and 'C' remains disconnected.
    """
    g = Graph()
    g.add_edge("A", "B")
    g.add_vertex("C")
    reversed_g = reverse(g)
    assert reversed_g["B"] == ["A"]
    assert reversed_g["A"] == []
    assert reversed_g["C"] == []

def test_reverse_complex_graph():
    """
    Test reversing a more complex graph structure.

    Ensures that reversing a graph with multiple vertices and edges 
    like 'A' to 'B', 'B' to 'C', and 'C' to 'A' results in a correct 
    reversal with edges in the opposite direction.
    """
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("C", "A")
    reversed_g = reverse(g)
    assert reversed_g["B"] == ["A"]
    assert reversed_g["C"] == ["B"]
    assert reversed_g["A"] == ["C"]

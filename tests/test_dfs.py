import pytest
from src.graph.searching import dfs

def test_dfs_typical_graph():
    """
    Test that dfs explores all reachable nodes starting from a given vertex in a typical graph.
    """
    G = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    result = dfs(G, 'A')
    expected = {'A', 'B', 'C', 'D', 'E', 'F'}
    assert result == expected, f"Expected {expected}, got {result}"


def test_dfs_single_node():
    """
    Test that dfs handles a graph with a single node correctly.
    """
    G = {'A': []}
    result = dfs(G, 'A')
    expected = {'A'}
    assert result == expected, f"Expected {expected}, got {result}"

def test_dfs_disconnected_graph():
    """
    Test that dfs correctly identifies only the reachable nodes 
    when the graph has disconnected components.
    """
    G = {
        'A': ['B'],
        'B': [],
        'C': ['D'],
        'D': []
    }
    result = dfs(G, 'A')
    expected = {'A', 'B'}  # Should only discover nodes reachable from 'A'
    assert result == expected, f"Expected {expected}, got {result}"

def test_dfs_empty_graph():
    """
    Test that dfs returns an empty set when the graph is empty or 
    the start vertex is not present.
    """
    G = {}
    result = dfs(G, 'A')
    expected = set()
    assert result == expected, f"Expected {expected}, got {result}"

def test_dfs_non_existent_start_vertex():
    """
    Test that dfs handles the case where the start vertex does not exist in the graph.
    """
    G = {'A': ['B'], 'B': ['C'], 'C': []}
    result = dfs(G, 'X')  # 'X' is not in the graph
    expected = set()
    assert result == expected, f"Expected {expected}, got {result}"

def test_dfs_graph_with_cycle():
    """
    Test that dfs handles graphs with cycles correctly without getting stuck in an infinite loop.
    """
    G = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']  # Cycle back to 'A'
    }
    result = dfs(G, 'A')
    expected = {'A', 'B', 'C'}
    assert result == expected, f"Expected {expected}, got {result}"

def test_dfs_graph_with_multiple_edges():
    """
    Test that dfs handles graphs with multiple edges to the same vertex.
    """
    G = {
        'A': ['B', 'B'],
        'B': ['C', 'C'],
        'C': []
    }
    result = dfs(G, 'A')
    expected = {'A', 'B', 'C'}
    assert result == expected, f"Expected {expected}, got {result}"

import pytest
from src.graph.searching import dfs

def test_dfs():
    G = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    assert dfs(G, 'A') == {'A', 'B', 'C', 'D', 'E', 'F'}
    assert dfs(G, 'D') == {'D'}
    assert dfs(G, 'E') == {'E', 'F'}

def test_empty_graph():
    G = {}
    with pytest.raises(KeyError):
        dfs(G, 'A') == set()

def test_single_node():
    G = {'A': []}
    assert dfs(G, 'A') == {'A'}

from graphviz import Digraph


def plot_graph(graph, output_dir="./data"):
    dot = Digraph("dot", format="png")

    nodes = set(graph.keys()).union(
        {edge for edges in graph.values() for edge in edges}
    )

    # Explicitly add all nodes with consistent styling
    for node in nodes:
        dot.node(
            str(node),
            color="black",  # Outline color
            shape="box",  # Shape of the node
            style="filled",  # Fill the node with color
            fillcolor="lightblue",
        )  # Background color of the node

    # Add edges with square arrowhead style
    for node, edges in graph.items():
        for edge in edges:
            dot.edge(
                str(node),
                str(edge),
                color="blue",  # Color of the edge
                style="solid",  # Style of the edge
                label=f"{str(node)} → {str(edge)}",
                
            )  # Add a label to the edge

        # Render the graph to the specified directory
    return dot

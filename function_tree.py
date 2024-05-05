import functools as ft
import itertools as it
import operator as op

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, node_type: str, value: str=None, latex: str=None):
        self.node_type = node_type

        self.value = value
        self.latex = latex

        self.parent = None
        self.sibling = None
        self.left = None
        self.right = None

    @property
    def height(self):
        return self.parent.height + 1 if self.parent is not None else 1

    def traverse_prefix_order(self, node):
        if node is None:
            return ''
        self.traverse_prefix_order(node.left)
        self.traverse_prefix_order(node.right)

        return self.latex


class FunctionTree:
    def __init__(self, root):
        self.root = root
    
    def traverse(self):
        yield from self._traverse(self.root)

    def _traverse(self, node):
        if node is not None:
            yield node
            yield from self._traverse(node.left)
            yield from self._traverse(node.right)

    def levels(self):
        nodes = sorted(self.traverse(), key=op.attrgetter('height'))
        return {k: list(g) for k, g in it.groupby(nodes, key=op.attrgetter('height'))}
        
    @property
    def latex(self):
        return self.root.traverse_prefix_order(self.root)

    def visualize(self):
        G = nx.DiGraph()
        nodes = [node for node in self.traverse()]
        G.add_nodes_from([(node, {'height': node.height}) for node in nodes])
        self._add_edges(G, self.root)
        nx.draw(G, nx.multipartite_layout(G, subset_key='height', align='horizontal'), 
                with_labels=True, labels={node: node.value for node in nodes})
        plt.show()

    def _add_edges(self,graph, node, parent=None):
        if node is not None:
            if parent is not None:
                graph.add_edge(node, parent)
            self._add_edges(graph, node.left, parent=node)
            self._add_edges(graph, node.right, parent=node)
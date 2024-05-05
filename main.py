'''
    A "function tree" is a tree comprised of nodes which are either functions 
    or operators. An example of this is how a computer parses a mathematical 
    expression by decomposing the function into simple building blocks and then 
    evaluating it in a prefix or postfix order.

    In our case, a function tree is a binary tree since each node has at most
    two children (the function nodes have one child corresponding to one input,
    and the operator nodes have two children corresponding to two inputs).

    Some facts
    ----------
    - The tree is binary
    - The leaves of the tree are function nodes
'''

import random

import matplotlib.pyplot as plt
import networkx as nx

from gen import generate_random_node
from function_tree import Node, FunctionTree


def generate_random_function_tree(max_height: int=2):
    '''Generates a feasible function tree.
    
    max_height: int
        The height of the function tree, also the length of a longest path from
        the root to a leaf. Default value is 2.
    '''
    if max_height <= 0:
        raise ValueError(f'{max_height} is not a valid value for max_depth. It must be greater than 0.')
    if max_height == 1:
        return generate_random_node('function')

    # generate a random node
    node_type = random.choice(['operator', 'function'])
    root = generate_random_node(node_type)

    # every non-leaf node has a child
    root.left = generate_random_function_tree(max_height - 1)
    root.left.parent = root
    if node_type == 'operator':
        # operator nodes have two children
        root.right = generate_random_function_tree(max_height - 1)
        root.right.parent = root
        root.left.sibling, root.right.sibling = root.right, root.left

        # LaTeX for DIVISION node
        if root.node_type == 'DIVISION':
            root.latex = f'\\frac{{ {root.left.latex} }}{{ {root.right.latex} }}'
        else:
            root.latex = f'\\left( {root.left.latex} {root.latex} {root.right.latex} \\right)'
    else:
        root.latex = root.latex.replace('x', root.left.latex)
    return root


def main():
    function_tree = FunctionTree(generate_random_function_tree(max_height=4))
    print(function_tree.latex)
    function_tree.visualize()


if __name__ == "__main__":
    main()
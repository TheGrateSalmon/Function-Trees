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

from function_tree import AdditionNode, SubtractionNode, MultiplicationNode, DivisionNode
from function_tree import ConstantNode, MonomialNode, \
                          NaturalExpNode, ExpNode, NaturalLogNode, LogNode, \
                          TrigNode, InverseTrigNode
from function_tree import FunctionTree


def random_node(node_category: str, weights=None):
    """Generates a random node.

    Args
    ----
    node_category: str
        The category of the node. It can be either 'operator' or 'function'.
    weights: list
        The weights of the different node types. The default value is None.
    """
    OPERATOR_TYPE_MAP = {'ADDITION': AdditionNode,
                         'SUBTRACTION': SubtractionNode,
                         'MULTIPLICATION': MultiplicationNode,
                         'DIVISION': DivisionNode}
    FUNCTION_TYPE_MAP = {'CONSTANT': ConstantNode,
                         'MONOMIAL': MonomialNode,
                         'NATURAL EXP': NaturalExpNode,
                         'EXP': ExpNode,
                         'NATURAL LOG': NaturalLogNode,
                         'LOG': LogNode,
                         'TRIG': TrigNode,
                         'INVERSE TRIG': InverseTrigNode}

    node_type_maps = {'operator': OPERATOR_TYPE_MAP, 'function': FUNCTION_TYPE_MAP}
    if node_category not in node_type_maps:
        raise ValueError(f'{node_type} is an invalid node type.')
    node_type_map = node_type_maps[node_category]
    node_type = random.choices(list(node_type_map.keys()), weights=weights)[0]
    return node_type_map[node_type](node_type)


def random_function_tree(max_height: int=2):
    """Generates a feasible function tree.
    
    Args
    ----
    max_height: int
        The height of the function tree, also the length of a longest path from
        the root to a leaf. Default value is 2.
    """
    if max_height <= 0:
        raise ValueError(f'{max_height} is not a valid value for max_depth. It must be greater than 0.')
    if max_height == 1:
        return random_node('function')

    # generate a random node
    node_category = random.choice(['operator', 'function'])
    root = random_node(node_category)

    # every non-leaf node has a child
    root.left = random_function_tree(max_height - 1)
    root.left.parent = root
    if node_category == 'operator':
        # operator nodes have two children
        root.right = random_function_tree(max_height - 1)
        root.right.parent = root
        root.left.sibling, root.right.sibling = root.right, root.left
    return root


def main():
    function_tree = FunctionTree(random_function_tree(max_height=4))
    print(function_tree.latex())
    function_tree.visualize()


if __name__ == "__main__":
    main()
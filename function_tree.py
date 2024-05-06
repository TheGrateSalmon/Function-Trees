import functools as ft
import itertools as it
import operator as op

import matplotlib.pyplot as plt
import networkx as nx

from gen import random_coefficient, random_exponent, random_base, random_trig_function, random_inverse_trig_function


class Node:
    def __init__(self, node_type: str):
        self.node_type = node_type
        self.is_reduced = False

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


################################################################################
class OperatorNode(Node):
    def __init__(self, node_type):
        super().__init__(node_type)

    def simplify(self):
        if self.is_reduced:
            return self
        simplify_dispatch = {'ADDITION': self._simplify_addition,
                             'SUBTRACTION': self._simplify_subtraction,
                             'MULTIPLICATION': self._simplify_multiplication,
                             'DIVISION': self._simplify_division}
        return simplify_dispatch[self.node_type]()

    def _simplify_addition(self):
        if self.left.node_type == 'CONSTANT':
            if self.right.node_type == 'CONSTANT':
                constant_value = int(self.left.value) + int(self.right.value)
                return FunctionNode('CONSTANT', str(constant_value), str(constant_value))
        elif self.left.node_type == 'MONOMIAL':
            if self.right.node_type == 'MONOMIAL':
                if self.left.value == self.right.value:
                    coefficient = int(self.left.value)
                    return FunctionNode('MONOMIAL', str(coefficient), str(coefficient))

    def _simplify_subtraction(self):
        pass

    def _simplify_multiplication(self):
        pass

    def _simplify_division(self):
        pass
        

class AdditionNode(OperatorNode):
    def __init__(self, node_type):
        super().__init__(node_type)

    def __str__(self):
        return '+'
    
    @property
    def latex(self):
        return '+'
    

class SubtractionNode(OperatorNode):
    def __init__(self, node_type):
        super().__init__(node_type)

    def __str__(self):
        return '-'
    
    @property
    def latex(self):
        return '-'
    

class MultiplicationNode(OperatorNode):
    def __init__(self, node_type):
        super().__init__(node_type)

    def __str__(self):
        return '*'
    
    @property
    def latex(self):
        return ''

class DivisionNode(OperatorNode):
    def __init__(self, node_type):
        super().__init__(node_type)

    def __str__(self):
        return '/'
    
    @property
    def latex(self):
        return '\\frac{}{}'


################################################################################
class FunctionNode(Node):
    def __init__(self, node_type):
        super().__init__(node_type)
        self.coefficient = random_coefficient()

    @property
    def latex(self):
        return ''

    @staticmethod
    def _coefficient_str(coefficient):
        return '' if coefficient == 1 else f'{coefficient}'
    
    @staticmethod
    def _exponent_str(exponent):
        if exponent == 1:
            return ''
        if len(str(exponent)) >= 2:
            return f'^({exponent})'
        return f'^{exponent}'

    @staticmethod
    def _coefficient_latex(coefficient):
        return '' if coefficient == 1 else f'{coefficient}'
    
    @staticmethod
    def _exponent_latex(exponent):
        if exponent == 1:
            return ''
        if len(str(exponent)) >= 2:
            return f'^{{{exponent}}}'
        return f'^{exponent}'


class ConstantNode(FunctionNode):
    def __init__(self, node_type):
        super().__init__(node_type)
        
    def __str__(self):
        return f'{self.coefficient}'

    @property
    def latex(self):
        return f'{self.coefficient}'


class MonomialNode(FunctionNode):
    def __init__(self, node_type, is_integer=True):
        super().__init__(node_type)
        self.exponent = random_exponent(is_integer=is_integer)

    def __str__(self):
        return f'{self._coefficient_str(self.coefficient)}x{self._exponent_str(self.exponent)}'
    
    @property
    def latex(self):
        template_str = f'{self._coefficient_latex(self.coefficient)}x{self._exponent_latex(self.exponent)}'        
        return template_str if self.height == 1 else template_str.replace('x', '\\left( {x} \\right)')


class NaturalExpNode(FunctionNode):
    def __init__(self, node_type):
        super().__init__(node_type)
        
    def __str__(self):
        return f'{self._coefficient_str(self.coefficient)}e^x'

    @property
    def latex(self):
        return f'{self._coefficient_latex(self.coefficient)}e^{{x}}'


class ExpNode(FunctionNode):
    def __init__(self, node_type):
        super().__init__(node_type)
        self.base = random_base()

    def __str__(self):
        mult_str = '*' if self.coefficient != 1 else ''
        return f'{self._coefficient_str(self.coefficient)}{mult_str}{self.base}^x'
    
    @property
    def latex(self):
        mult_str = '\\cdot' if self.coefficient != 1 else ''
        return f'{self._coefficient_latex(self.coefficient)} {mult_str} {self.base}^{{x}}'


class NaturalLogNode(FunctionNode):
    def __init__(self, node_type):
        super().__init__(node_type)

    def __str__(self):
        return f'{self._coefficient_str(self.coefficient)}ln(x)'

    @property
    def latex(self):
        return f'{self._coefficient_latex(self.coefficient)}\\ln\\left( {{x}} \\right)'


class LogNode(FunctionNode):
    def __init__(self, node_type):
        super().__init__(node_type)
        self.base = random_base()

    def __str__(self):
        return f'{self._coefficient_str(self.coefficient)}log_{self.base}(x)'
    
    @property
    def latex(self):
        return f'{self._coefficient_latex(self.coefficient)}\\log_{self.base}\\left( {{x}} \\right)'


class TrigNode(FunctionNode):
    def __init__(self, node_type):
        super().__init__(node_type)
        self.trig_function = random_trig_function()

    def __str__(self):
        return f'{self._coefficient_str(self.coefficient)}{self.trig_function}(x)'
    
    @property
    def latex(self):
        return f'{self._coefficient_latex(self.coefficient)}\\{self.trig_function}\\left( {{x}} \\right)'


class InverseTrigNode(FunctionNode):
    def __init__(self, node_type):
        super().__init__(node_type)
        self.inverse_trig_function = random_trig_function()

    def __str__(self):
        return f'{self._coefficient_str(self.coefficient)}{self.inverse_trig_function}^(-1)(x)'
    
    @property
    def latex(self):
        return f'{self._coefficient_latex(self.coefficient)}\\{self.inverse_trig_function}\\left( {{x}} \\right)'


################################################################################
class FunctionTree:
    def __init__(self, root):
        self.root = root
    
    def latex(self, node=None):
        if node is None:
            node = self.root

        # leaf node
        if node.left is None and node.right is None:
            return node.latex
        
        # internal node
        if isinstance(node, OperatorNode):
            if node.node_type == 'DIVISION':
                return f'\\frac{{ {self.latex(node.left)} }}{{ {self.latex(node.right)} }}'
            else:
                return f'\\left( {self.latex(node.left)} {node.latex} {self.latex(node.right)} \\right)'
        elif isinstance(node, FunctionNode):
            return node.latex.replace('x', self.latex(node.left))
        else:
            raise ValueError(f'{type(node)} is not a valid node type.')

    @property
    def nodes(self):
        yield from self._traverse(self.root)

    def _traverse(self, node):
        if node is not None:
            yield node
            yield from self._traverse(node.left)
            yield from self._traverse(node.right)

    @property
    def levels(self):
        nodes = sorted(self.traverse(), key=op.attrgetter('height'))
        return {k: list(g) for k, g in it.groupby(nodes, key=op.attrgetter('height'))}
        
    @property
    def height(self):
        return max(self.levels.keys())

    def visualize(self):
        G = nx.DiGraph()
        nodes = [node for node in self.nodes]
        G.add_nodes_from([(node, {'height': node.height}) for node in nodes])
        self._add_edges(G, self.root)
        nx.draw(G, nx.multipartite_layout(G, subset_key='height', align='horizontal'), 
                with_labels=True, labels={node: str(node) for node in nodes})
        plt.show()

    def _add_edges(self,graph, node, parent=None):
        if node is not None:
            if parent is not None:
                graph.add_edge(node, parent)
            self._add_edges(graph, node.left, parent=node)
            self._add_edges(graph, node.right, parent=node)
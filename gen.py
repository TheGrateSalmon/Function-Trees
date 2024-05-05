from fractions import Fraction
import random

from formatting import _format_value, _format_latex
from function_tree import Node


def random_coefficient(min_value: int=1, max_value: int=10):
    """
    Generates a random coefficient within the specified range.

    Args
    ----
    min_value : (int, optional) 
        The minimum value of the coefficient. Defaults to 0.
    max_value : (int, optional)
        The maximum value of the coefficient. Defaults to 10.

    Returns
    -------
     : int 
        A random coefficient within the specified range.
    """
    return random.randint(min_value, max_value)


def random_int_exponent(min_value: int=1, max_value: int=10):
    """
    Generates a random power within the specified range.

    Args
    ----
    min_value : (int, optional) 
        The minimum value of the power. Defaults to 0.
    max_value : (int, optional)
        The maximum value of the power. Defaults to 10.

    Returns
    -------
     : int 
        A random power within the specified range.
    """
    return random.randint(min_value, max_value)


def random_frac_exponent(min_value: int=1, max_value: int=10):
    """
    Generates a random rational power within the specified range.

    Args
    ----
    min_value : (int, optional) 
        The minimum value of the power. Defaults to 1.
    max_value : (int, optional)
        The maximum value of the power. Defaults to 10.

    Returns
    -------
     : int 
        A random rational power within the specified range.
    """
    return Fraction(random.randint(min_value, max_value), random.randint(min_value, max_value))


def random_base(min_value: int=2, max_value: int=10):
    """
    Generates a random base within the specified range.

    Args
    ----
    min_value : (int, optional) 
        The minimum value of the base. Defaults to 2.
    max_value : (int, optional)
        The maximum value of the base. Defaults to 10.

    Returns
    -------
     : int 
        A random base within the specified range.
    """
    return random.randint(min_value, max_value)


def random_trig_function():
    """
    Generates a random trigonometric function.

    Returns
    -------
     : str 
        A random trigonometric function.
    """
    return random.choice(['sin', 'cos', 'tan', 'csc', 'sec', 'cot'])


def random_inverse_trig_function():
    """
    Generates a random inverse trigonometric function.

    Returns
    -------
     : str 
        A random inverse trigonometric function.
    """
    return random.choice(['sin^{-1}', 'cos^{-1}', 'tan^{-1}', 'csc^{-1}', 'sec^{-1}', 'cot^{-1}'])


def generate_random_operator_node():
    OPERATOR_NODES = ['ADDITION', 'SUBTRACTION', 'MULTIPLICATION', 'DIVISION']
    OPERATOR_WEIGHTS = [1/len(OPERATOR_NODES) for _ in OPERATOR_NODES]

    operator_type = random.choices(OPERATOR_NODES, weights=OPERATOR_WEIGHTS)[0]
    return Node(operator_type,
                _format_value(operator_type),
                _format_latex(operator_type))


def generate_random_function_node():
    FUNCTION_NODES = ['CONSTANT', 'INT MONOMIAL', 'FRAC MONOMIAL', 'NATURAL EXP', 'EXP', 'NATURAL LOG', 'LOG', 'TRIG', 'INVERSE TRIG']
    FUNCTION_WEIGHTS = [1/len(FUNCTION_NODES) for _ in FUNCTION_NODES]

    function_type = random.choices(FUNCTION_NODES, weights=FUNCTION_WEIGHTS)[0]
    return Node(function_type,
                _format_value(function_type),
                _format_latex(function_type, coefficient=random_coefficient(), 
                              int_exponent=random_int_exponent(), frac_exponent=random_frac_exponent(), 
                              base=random_base(), 
                              trig=random_trig_function(), inverse_trig=random_inverse_trig_function()))


def generate_random_node(node_type: str):
    if node_type == 'operator':
        return generate_random_operator_node()
    elif node_type == 'function':
        return generate_random_function_node()
    else:
        raise ValueError(f'{node_type} is an invalid node type.')
from fractions import Fraction
import random


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


def random_exponent(min_value: int=1, max_value: int=50, is_integer: bool=True):
    """
    Generates a random power within the specified range.

    Args
    ----
    min_value : (int, optional) 
        The minimum value of the power. Defaults to 0.
    max_value : (int, optional)
        The maximum value of the power. Defaults to 10.
    is_integer : (bool, optional)
        A boolean indicating whether the power should be an integer. Defaults to True.

    Returns
    -------
     : int 
        A random power within the specified range.
    """
    return random.randint(min_value, max_value) if is_integer else Fraction(random.randint(min_value, max_value), random.randint(min_value, max_value)) 


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
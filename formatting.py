def _format_value(node_type):
    if node_type in {'ADDITION', 'SUBTRACTION', 'MULTIPLICATION', 'DIVISION'}:
        return _format_operator_value(node_type)
    elif node_type in {'CONSTANT', 'INT MONOMIAL', 'FRAC MONOMIAL', 'NATURAL EXP', 'EXP', 'NATURAL LOG', 'LOG', 'TRIG', 'INVERSE TRIG'}:
        return _format_function_value(node_type)
    else:
        raise ValueError(f'{node_type} is an invalid node type.')
    

def _format_operator_value(operator_type: str):
    OPERATOR_VALUES = {'ADDITION': '+',
                       'SUBTRACTION': '-',
                       'MULTIPLICATION': '*',
                       'DIVISION': '/'}
    if operator_type not in OPERATOR_VALUES:
        raise ValueError(f'{operator_type} is an invalid operator type.')
    return OPERATOR_VALUES[operator_type]
    

def _format_function_value(function_type: str):
    FUNCTION_VALUES = {'CONSTANT': 'C',
                       'INT MONOMIAL': 'x^n',
                       'FRAC MONOMIAL': 'x^{m/n}',
                       'NATURAL EXP': 'e^x',
                       'EXP': 'a^x',
                       'NATURAL LOG': 'ln(x)',
                       'LOG': 'log_b(x)',
                       'TRIG': 'trig(x)',
                       'INVERSE TRIG': 'trig^{-1}(x)'}
    if function_type not in FUNCTION_VALUES:
        raise ValueError(f'{function_type} is an invalid function type.')
    return FUNCTION_VALUES[function_type]


def _format_latex(node_type: str, **kwargs):
    if node_type in {'ADDITION', 'SUBTRACTION', 'MULTIPLICATION', 'DIVISION'}:
        return _format_operator_latex(node_type)
    elif node_type in {'CONSTANT', 'INT MONOMIAL', 'FRAC MONOMIAL', 'NATURAL EXP', 'EXP', 'NATURAL LOG', 'LOG', 'TRIG', 'INVERSE TRIG'}:
        return _format_function_latex(node_type, **kwargs)
    else:
        raise ValueError(f'{node_type} is an invalid node type.')
    

def _format_operator_latex(operator_type: str):
    if operator_type == 'ADDITION':
        return '+'
    elif operator_type == 'SUBTRACTION':
        return '-'
    elif operator_type == 'MULTIPLICATION':
        return ''
    elif operator_type == 'DIVISION':
        return '/'
    else:
        raise ValueError(f'{operator_type} is an invalid operator type.')
    

def _format_function_latex(function_type: str, **kwargs):
    if function_type == 'CONSTANT':
        return _format_constant_latex(**kwargs)
    elif function_type == 'INT MONOMIAL':
        return _format_int_monomial_latex(**kwargs)
    elif function_type == 'FRAC MONOMIAL':
        return _format_frac_monomial_latex(**kwargs)
    elif function_type == 'NATURAL EXP':
        return _format_natural_exp_latex(**kwargs)
    elif function_type == 'EXP':
        return _format_exp_latex(**kwargs)
    elif function_type == 'NATURAL LOG':
        return _format_natural_log_latex(**kwargs)
    elif function_type == 'LOG':
        return _format_log_latex(**kwargs)
    elif function_type == 'TRIG':
        return _format_trig_latex(**kwargs)
    elif function_type == 'INVERSE TRIG':
        return _format_inverse_trig_latex(**kwargs)
    else:
        raise ValueError(f'{function_type} is an invalid function type.')
    

def _format_exponent_latex(exponent=1, **kwargs):
    return '' if exponent == 1 else f'{exponent}'


def _format_coefficient_latex(coefficient=1, **kwargs):
    return '' if coefficient == 1 else f'{coefficient}'


def _format_constant_latex(coefficient=1, **kwargs):
    return f'{coefficient}'


def _format_int_monomial_latex(coefficient=1, exponent=1, max_height=1, **kwargs):
    if max_height == 1:
        return f'{_format_coefficient_latex(coefficient)}x^{_format_exponent_latex(exponent)}'
    else:
        return f'{_format_coefficient_latex(coefficient)}\\left( {{x}} \\right)^{_format_exponent_latex(exponent)}'
    

def _format_frac_monomial_latex(coefficient=1, exponent=1, max_height=1, **kwargs):
    if max_height == 1:
        return f'{_format_coefficient_latex(coefficient)}x^{{{_format_exponent_latex(exponent)}}}'
    else:
        return f'{_format_coefficient_latex(coefficient)}\\left( {{x}} \\right)^{{{_format_exponent_latex(exponent)}}}'


def _format_natural_exp_latex(coefficient=1, **kwargs):
    return f'{_format_coefficient_latex(coefficient)}e^{{x}}'


def _format_exp_latex(coefficient=1, base=2, **kwargs):
    return f'{_format_coefficient_latex(coefficient)} \\cdot {base}^{{x}}'


def _format_natural_log_latex(coefficient=1, **kwargs):
    return f'{_format_coefficient_latex(coefficient)}\\ln\\left( {{x}} \\right)'


def _format_log_latex(coefficient=1, base=2, **kwargs):
    return f'{_format_coefficient_latex(coefficient)}\\log_{base}\\left( {{x}} \\right)'


def _format_trig_latex(coefficient=1, trig='sin', **kwargs):
    return f'{_format_coefficient_latex(coefficient)}\\{trig}\\left( {{x}} \\right)'


def _format_inverse_trig_latex(coefficient=1, inverse_trig='sin^{-1}', **kwargs):
    return f'{_format_coefficient_latex(coefficient)}\\{inverse_trig}\\left( {{x}} \\right)'
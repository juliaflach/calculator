import math
import statistics


def division(params: list) -> float:
    return params[0]/params[1]


def mean(params: list) -> float:
    """
    Return the simple arithmetic mean of a list of floats.
    """
    return statistics.mean(params)


def pow(params: list) -> float:
    """
    Calculate x to the power of y.
    """
    return params[0]**params[1]


def stdev(params: list) -> float: 
    """
    Measure the amount of variation or dispersion of a list of floats.
    """
    return statistics.stdev(params)


def sqrt(params: list) -> float:
    """
    Calculate the square root of a float.
    """
    return params[0]**(1/2)


def add(params: list) -> float:
    """
    Return the sum of a list of floats.
    """
    return sum(params)
    

def sin(params: list) -> float:
    return round(math.sin(math.radians(params[0])),2)


def cos(params: list) -> float:
    return round(math.cos(math.radians(params[0])),2)


def tan(params: list) -> float:
    return round(math.tan(math.radians(params[0])),2)
        

def bhaskara(params: list) -> dict:
    """ 
    Find the real roots of a quadratic equation using the bhaskara formula.
    Args:
        params: A list of one string in the form 'ax2 + bx + c = 0'.
    
    Returns:
        A dictionary with the values of the real roots (x1 and x2)
        or 'non real roots' if there are none.
    """
    eq = params[0]
    if 'x2' not in eq or ('=0' not in eq and '= 0' not in eq): # Checks if the expression is valid. 
        return 'invalid expression'

    if eq[0] == 'x':
        eq = '1' + eq

    eq2 = eq.replace(' ','').replace('x2',' ') # This will be used to check if there were two 'x' in the expression.

    abc = eq2.replace('x',' ').replace('=',' ').split()
    if abc[0] == '+' or abc[0] == '-':
        abc[0] += '1'
    if abc[1] == '+' or abc[1] == '-':
        abc[1] += '1'

    if 'x' not in eq2: # If there wasn't a second 'x' in the original expression, then b = 0.
        abc.insert(1,0)

    a, b, c = [int(i) for i in abc[:3]]

    delta = ((b**2) - 4*a*c)
    raiz = delta**(1/2)
    if delta < 0:
        return 'non real roots'
    x1 = (- b + raiz)/2*a
    x2 = (- b - raiz)/2*a
    return {'x1': x1, 'x2': x2}


def get_change(params: list) -> list:
    """
    Calculate the change between the current and the previous values of a list.
    Args:
        params: A list of floats that do not contain zeros.
    Returns:
        A list of the changes (in percent) for each two values of the list.

    """
    out = ['None']
    for i in range(1,len(params)):
        if params[i-1] == 0:
            return 'error: zero found'
        change = f"{int((params[i]/params[i-1])*100 - 100)}%"
        out.append(change)
    return out
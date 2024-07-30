# example function:
def additionFunction(a, b):

    c = a + b
    return c


# Type annotations included:
def additionFunctionWithTypeAnnotation(a: int, b: int) -> int:
    """This fu ntiontake sin 2 parameters and returns the sum of the paraeter.

    Args:
        a (int): random variables
        b (int): user input

    Returns:
        c (int): sum of input parameters
    """

    c = a + b
    return c


def get_data(cart: bool = False, products: bool = False, users: bool = False):

    # get your initial data

    if cart == True:
        pass

    elif products == True:
        pass

    else:
        pass


get_data(products=True)
get_data(users=True)
get_data(cart=True)

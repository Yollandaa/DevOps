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


my_varable = ""  # train case: my_variable_is_very_cool_and_holds_info
myVar = ""  # camel case: weWouldWriteOurVariablesLikeThis
str_myVar = ""
int_myVar = 1
float_myVar = 1.0
bool_myVar = True
str_my_var = ""


str_myVar = "7"
int_myVar = 7
float_myVar = 7.0

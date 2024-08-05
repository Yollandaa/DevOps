# ---------- legacy code ----------

import json
import os
import requests

resources_dir = "./resources"


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


# ---------- new code ----------

# ---------- Library Imports ----------
import os
import requests
import json

# ---------- Module Imports ----------


# ---------- Global variables ----------


# ---------- Script ----------


class Example:

    resources_dir = "./resources"

    @classmethod
    def additionFunction(a, b):
        c = a + b
        return c

    @classmethod
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

    @staticmethod
    def subtractionFunction(a, b):
        return a - b


my_variable = Example.additionFunction(2, 3)
res_dir = Example.resources_dir


Example.resources_dir = "newpath/to/dir"

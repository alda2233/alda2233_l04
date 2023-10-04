"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-10-04"
-------------------------------------------------------
"""
# Imports
from functions import total_change
# Constants


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


Nick = int(input("nickles"))
Dime = int(input("nickles"))
Quart = int(input("nickles"))
Loon = int(input("nickles"))
Toon = int(input("nickles"))

total = total_change(Nick, Dime, Quart, Loon, Toon)
print(total)

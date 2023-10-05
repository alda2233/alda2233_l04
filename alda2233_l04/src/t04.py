"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-10-05"
-------------------------------------------------------
"""
# Imports
from functions import square_pyramid
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


base = float(input("Base:"))
height = float(input("height:"))

sh, area, vol = square_pyramid(base, height)
print(sh, area, vol)

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
from functions import time_values
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


seconds = int(input("Sec:"))

days, hours, minutes = time_values(seconds)
print(days, hours, minutes)

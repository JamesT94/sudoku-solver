"""
Created on Dec 5th 2020

@authors: James Taylor, Jack Taylor
"""

import math
import numpy as np


# Function to create a blank puzzle object @Jack


def create_puzzle():
    puzzle = np.zeros((9, 9), int)

    return puzzle


# Function to populate a puzzle with initial numbers @Jack
def populate_puzzle(puzzle):
    # Random test numbers
    puzzle[1, 1] = 3
    puzzle[3, 4] = 9
    puzzle[7, 8] = 2
    puzzle[4, 6] = 6
    puzzle[4, 1] = 4

    return puzzle


# Function to print a puzzle to the console in a way that is readable @Jack
# Function to take a puzzle with initial numbers and complete it @James
x = create_puzzle()
y = populate_puzzle(x)
print(y)

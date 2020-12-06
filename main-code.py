"""
Created on Dec 5th 2020

@authors: James Taylor, Jack Taylor
"""

import pygame
import numpy as np


# Create a blank puzzle object @Jack
def create_puzzle():

    puzzle = np.zeros((9, 9), int)
    return puzzle


# Populate a puzzle object with initial numbers @Jack
def populate_puzzle(puzzle):

    # Random test numbers
    puzzle[1, 1] = 3
    puzzle[3, 4] = 9
    puzzle[7, 8] = 2
    puzzle[4, 6] = 6
    puzzle[4, 1] = 4

    return puzzle


# Locate the next empty square of the puzzle @James
def find_square(puzzle):

    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j


# Check if a value can go in a square @James
def validate(puzzle, value, location):

    for i in range(9):  # Rows
        if puzzle[location[0]][i] == value and location[1] != i:
            return False

    for i in range(9):  # Columns
        if puzzle[i][location[1]] == value and location[0] != i:
            return False

    # Boxes
    box_x = location[1] // 3
    box_y = location[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if puzzle[i][j] == value and (i, j) != location:
                return False

    return True


# Take a puzzle with initial numbers and complete it @James
def solve_puzzle(puzzle):

    empty_square = find_square(puzzle)

    if not empty_square:
        return True
    else:
        x, y = empty_square

    for i in range(1, 10):
        if validate(puzzle, i, (x, y)):
            puzzle[x][y] = i

            if solve_puzzle(puzzle):
                return True

            puzzle[x][y] = 0

    return False


empty = create_puzzle()
print(empty)
filled = populate_puzzle(empty)
print(filled)
solve_puzzle(filled)
print(filled)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~ Display a puzzle in a Pygame window ~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
pygame.init()

# Define constants and create game window
WIN_WIDTH = 800
WIN_HEIGHT = 800
scaling = 800 / 9
STAT_FONT = pygame.font.SysFont("calibri", 50)
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Sudoku Solver")
clock = pygame.time.Clock()


def draw():  # Draw the Sudoku board
    for i in range(9):
        for j in range(9):
            # Filling the squares in, can change this to just certain squares and different colours
            pygame.draw.rect(win, (255, 255, 255), (int(i * scaling), int(j * scaling),
                                                    int(scaling + 1), int(scaling + 1)))

    for i in range(10):  # Drawing the lines with varying thickness, and horrible colours
        if i % 3 == 0:
            thickness = 5
        else:
            thickness = 1
        pygame.draw.line(win, (0, 0, 0), (0, i * scaling), (9 * scaling, i * scaling), thickness)
        pygame.draw.line(win, (0, 0, 0), (i * scaling, 0), (i * scaling, 9 * scaling), thickness)


# Main loop
run = False
while run:
    clock.tick(1)  # 1 frame(s) per second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

    draw()

    pygame.display.update()

pygame.quit()

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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~ Display a puzzle in a Pygame window ~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
pygame.init()

# Define constants and create game window
WIN_WIDTH = 800
WIN_HEIGHT = 800
scaling = WIN_WIDTH / 9
FONT = pygame.font.SysFont("calibri", 50)
clock = pygame.time.Clock()


class Puzzle:
    board = populate_puzzle(create_puzzle())

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]

    def draw(self, display):  # Draw the Sudoku board

        for i in range(10):  # Draw the lines
            if i % 3 == 0:
                thickness = 5
            else:
                thickness = 1
            pygame.draw.line(display, (0, 0, 0), (0, i * scaling), (9 * scaling, i * scaling), thickness)
            pygame.draw.line(display, (0, 0, 0), (i * scaling, 0), (i * scaling, 9 * scaling), thickness)

        for i in range(self.rows):  # Draw the cubes
            for j in range(self.cols):
                self.cubes[i][j].draw(display)

    def update_cubes(self, board):
        for i in range(self.rows):  # Draw the cubes
            for j in range(self.cols):
                self.cubes[i][j].value = board[i][j]

    def solve_puzzle(self, board):
        empty_square = find_square(board)

        if not empty_square:
            self.update_cubes(board)
            return True

        else:
            x, y = empty_square

        for i in range(1, 10):
            if validate(board, i, (x, y)):
                board[x][y] = i

                if self.solve_puzzle(board):
                    self.update_cubes(board)
                    return True

                board[x][y] = 0

        return False


class Cube:

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, display):

        x = self.col * scaling
        y = self.row * scaling

        if self.temp != 0 and self.value == 0:
            text = FONT.render(str(self.temp), True, (128, 128, 128))
            display.blit(text, (x + (scaling / 2 - text.get_width() / 2), y + (scaling / 2 - text.get_height() / 2)))
        elif not (self.value == 0):
            text = FONT.render(str(self.value), True, (0, 0, 0))
            display.blit(text, (x + (scaling / 2 - text.get_width() / 2), y + (scaling / 2 - text.get_height() / 2)))

    def set(self, value):
        self.value = value

    def set_temp(self, value):
        self.temp = value


def redraw_window(display, puzzle):
    display.fill((255, 255, 255))
    puzzle.draw(display)


def main():  # Main loop

    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Sudoku Solver")
    puzzle = Puzzle(9, 9, 800, 800)
    run = True

    while run:
        clock.tick(10)  # 1 frame(s) per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    puzzle.solve_puzzle(puzzle.board)
                    print("Trying to solve...")

        redraw_window(win, puzzle)
        pygame.display.update()
    pygame.quit()


main()

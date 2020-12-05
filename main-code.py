"""
Created on Dec 5th 2020

@authors: James Taylor, Jack Taylor
"""

import math
import numpy
import pygame

# Function to create a blank puzzle object @Jack

# Function to populate a puzzle with initial numbers @Jack

# Function to print a puzzle to the console in a way that is readable @Jack

# Function to take a puzzle with initial numbers and complete it @James

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~ Display a puzzle in a Pygame window ~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
pygame.init()

# Define constants and create game window
WIN_WIDTH = 800
WIN_HEIGHT = 800
dif = 500 / 9
STAT_FONT = pygame.font.SysFont("calibri", 50)
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Sudoku Solver")
clock = pygame.time.Clock()


def draw():  # Draw the Sudoku board
    for i in range(9):
        for j in range(9):
            # Filling the squares in, can change this to just certain squares and different colours
            pygame.draw.rect(win, (255, 255, 255), (i * dif, j * dif, dif + 1, dif + 1))

    for i in range(10):  # Drawing the lines with varying thickness, and horrible colours
        if i % 3 == 0:
            thickness = 5
        else:
            thickness = 1
        pygame.draw.line(win, (255, 0, 0), (0, i * dif), (500, i * dif), thickness)
        pygame.draw.line(win, (255, 255, 0), (i * dif, 0), (i * dif, 500), thickness)


# Main loop
run = True
while run:
    clock.tick(20)  # 20 frames per second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

    number = STAT_FONT.render(str(5), 1, (255, 255, 255))
    numberRect = number.get_rect()
    win.blit(number, numberRect)

    draw()

    pygame.display.update()

pygame.quit()

import sys
import pygame
from pygame.locals import *
from itertools import product

# on doit "initialiser" PyGame
pygame.init()

# et définir la taille de la fenêtre (400x400)
screen = pygame.display.set_mode((400, 400))

CELL_SIZE = (20, 20)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)



def draw_cell(board_pos, color=WHITE):
    for screen_pos in screen_positions(board_pos):
            screen.set_at(screen_pos, color)

def screen_positions(board_pos):
    x, y = board_pos
    cell_width, cell_height = CELL_SIZE
    return (
      (cell_width*x + col, cell_height*y+line)
      for line, col
      in product(range(cell_height),range(cell_width))
    )

while True:
  for event in pygame.event.get():
    if event.type == KEYDOWN:
        if event.key == K_q:
          pygame.display.quit()
          pygame.quit()

  screen.fill(BLACK)
  draw_cell((2, 2), WHITE)
  pygame.display.update()

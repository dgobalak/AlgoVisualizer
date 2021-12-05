from sorting.bubble_sort import *
from sorting.selection_sort import *
from helpers import *
import pygame

def main(ALGO):
    pygame.init()
    pygame.display.set_caption(TITLE)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    matrix = np.ones((NUM_ROWS, NUM_COLS))
    
    if ALGO == "SELECTION":
        selection_sort(screen, matrix, clock)
    elif ALGO == "BUBBLE":
        bubble_sort(screen, matrix, clock) 


if __name__ == '__main__':
    main("BUBBLE")

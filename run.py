from path_finding.dfs import *
from path_finding.bfs import *

import pygame
import numpy as np


def main():
    pygame.init()
    pygame.display.set_caption(TITLE)

    START = (0, 0)
    END = (15, 15)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    matrix = np.ones((NUM_ROWS, NUM_COLS))
    matrix[START] = 0
    matrix[END] = 2

    dfs(screen, matrix.copy(), START, END)
    bfs(screen, matrix.copy(), START, END)


if __name__ == '__main__':
    main()

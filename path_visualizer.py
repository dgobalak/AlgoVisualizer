from path_finding.dfs import *
from path_finding.bfs import *
from path_finding.dijkstra import *

import pygame
import numpy as np
import time


def main(ALGO):
    start_time = time.time()
    pygame.init()
    pygame.display.set_caption(TITLE)

    START = (0, 0)
    END = (10, 25)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    matrix = np.ones((NUM_ROWS, NUM_COLS))

    if ALGO == "DFS":
        dfs(screen, matrix.copy(), START, END)
    elif ALGO == "BFS":
        bfs(screen, matrix.copy(), START, END)
    elif ALGO == "DIJKSTRA":
        dijkstra(screen, matrix.copy(), START, END)

    end_time = time.time()
    time.sleep(FINAL_DELAY)
    print(f"{ALGO}-> {end_time - start_time} sec")

if __name__ == '__main__':
    main("DFS")
    main("BFS")
    main("DIJKSTRA")

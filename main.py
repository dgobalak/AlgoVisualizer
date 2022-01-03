from path_finding.dfs import *
from path_finding.bfs import *
from path_finding.dijkstra import *

from sorting.bubble_sort import *
from sorting.selection_sort import *
from sorting.insertion_sort import *
from sorting.quick_sort import *
from sorting.merge_sort import *
from sorting.heap_sort import *
from sorting.counting_sort import *

from sorting.sorting_helpers import *

import pygame
import numpy as np
import time

def main():
    algorithm = ""
    while algorithm not in ("S", "P"):
        algorithm = input(
            "Enter S for sorting algorithms or P for path-finding algorithms: ").upper()
    
    pygame.init()
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    matrix = np.ones((NUM_ROWS, NUM_COLS))

    if algorithm == "S":
        nums = randomize_sorting_matrix(matrix)

        selection_sort(screen, matrix.copy(), nums.copy())
        bubble_sort(screen, matrix.copy(), nums.copy())
        insertion_sort(screen, matrix.copy(), nums.copy())
        quick_sort(screen, matrix.copy(), nums.copy(), 0, len(nums)-1)
        merge_sort(screen, matrix.copy(), nums.copy(), 0, len(nums)-1)
        heap_sort(screen, matrix.copy(), nums.copy())
        counting_sort(screen, matrix.copy(), nums.copy())    
        
    else:
        START = (13, 13)
        END = (2, 2)

        dfs(screen, matrix.copy(), START, END)
        bfs(screen, matrix.copy(), START, END)
        dijkstra(screen, matrix.copy(), START, END)

    time.sleep(2)   # Pause visualizer at the end

if __name__ == '__main__':
    main()

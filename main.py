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

from settings import *

from path_finding.path_helpers import *
import pygame
import numpy as np
import time


def main():
    # User chooses the algorithms they want to visualize
    # TODO: Add this user input to the GUI
    algorithm = ""
    while algorithm not in ("S", "P"):
        algorithm = input(
            "Enter S for sorting algorithms or P for path-finding algorithms: ").upper()

    pygame.init()
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    matrix = np.ones((NUM_ROWS, NUM_COLS))

    # Sorting Algorithms
    if algorithm == "S":
        nums = randomize_sorting_matrix(matrix)

        selection_sort(screen, matrix.copy(), nums.copy())
        bubble_sort(screen, matrix.copy(), nums.copy())
        insertion_sort(screen, matrix.copy(), nums.copy())
        quick_sort(screen, matrix.copy(), nums.copy(), 0, len(nums)-1)
        merge_sort(screen, matrix.copy(), nums.copy(), 0, len(nums)-1)
        heap_sort(screen, matrix.copy(), nums.copy())
        counting_sort(screen, matrix.copy(), nums.copy())

    # Pathfinding Algorithms
    else:
        # Get the start and end position from the user
        clicked_pos = []
        while len(clicked_pos) < 2:
            ev = pygame.event.get()
            for event in ev:
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    x //= NODE_WIDTH
                    y //= NODE_HEIGHT

                    clicked_pos.append((y, x))

                    if len(clicked_pos) == 1:
                        matrix[(y, x)] = 0
                    else:
                        matrix[(y, x)] = 2

                    draw_matrix(screen, matrix)

        START = clicked_pos[0]
        END = clicked_pos[1]

        dfs(screen, matrix.copy(), START, END)
        bfs(screen, matrix.copy(), START, END)
        dijkstra(screen, matrix.copy(), START, END)

    # Pause visualizer at the end
    time.sleep(2)


if __name__ == '__main__':
    main()

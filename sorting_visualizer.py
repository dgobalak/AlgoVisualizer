from sorting.bubble_sort import *
from sorting.selection_sort import *
from sorting.insertion_sort import *
from sorting.quick_sort import *
from sorting.merge_sort import *
from sorting.heap_sort import *
from sorting.counting_sort import *

from sorting_helpers import *
import pygame
import time


def main(ALGO):
    start = time.time()
    pygame.init()
    pygame.display.set_caption(TITLE)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    matrix = np.ones((NUM_ROWS, NUM_COLS))
    nums = randomize_sorting_matrix(matrix)

    if ALGO == "SELECTION":
        selection_sort(screen, matrix, nums)
    elif ALGO == "BUBBLE":
        bubble_sort(screen, matrix, nums)
    elif ALGO == "INSERTION":
        insertion_sort(screen, matrix, nums)
    elif ALGO == "QUICK":
        quick_sort(screen, matrix, nums, 0, len(nums)-1)
    elif ALGO == "MERGE":
        merge_sort(screen, matrix, nums, 0, len(nums)-1)
    elif ALGO == "HEAP":
        heap_sort(screen, matrix, nums)
    elif ALGO == "COUNTING":
        counting_sort(screen, matrix, nums)

    end = time.time()
    time.sleep(FINAL_DELAY)
    print(f"{ALGO}-> {end - start} sec")


if __name__ == '__main__':
    main("INSERTION")
    main("BUBBLE")
    main("SELECTION")
    main("QUICK")
    main("MERGE")
    main("HEAP")
    main("COUNTING")

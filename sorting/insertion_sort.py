from helpers import *
import pygame
import sys


def insertion_sort(screen, matrix):
    nums = randomize_sorting_matrix(matrix)
    screen.fill(BLACK)

    for i in range(1, len(nums)):
        screen.fill(BLACK)

        val = nums[i]
        j = i

        while j > 0 and nums[j-1] > val:
            nums[j] = nums[j-1]
            j -= 1

            matrix_from_nums(nums, matrix)
            draw_matrix(screen, matrix)
            pygame.display.flip()

        nums[j] = val

        matrix_from_nums(nums, matrix)
        draw_matrix(screen, matrix)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

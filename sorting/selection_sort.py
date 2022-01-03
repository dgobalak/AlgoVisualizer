from sorting.sorting_helpers import *
import pygame
import sys


def selection_sort(screen, matrix, nums):
    screen.fill(BLACK)

    for i in range(len(nums)):
        screen.fill(BLACK)

        min_i, min_val = i, nums[i]
        for j in range(i, len(nums)):
            if nums[j] <= min_val:
                min_i, min_val = j, nums[j]
                matrix_from_nums(nums, matrix)
                draw_matrix(screen, matrix)
                pygame.display.flip()

        nums[i], nums[min_i] = nums[min_i], nums[i]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        matrix_from_nums(nums, matrix)
        draw_matrix(screen, matrix)
        pygame.display.flip()

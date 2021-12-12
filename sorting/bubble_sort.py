from sorting_helpers import *
import pygame
import sys


def bubble_sort(screen, matrix, nums):
    screen.fill(BLACK)

    sorted = False
    for i in range(len(nums)-1):
        screen.fill(BLACK)

        if sorted:
            break

        sorted = True
        for j in range(0, len(nums)-i-1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if nums[j+1] < nums[j]:
                sorted = False
                nums[j], nums[j+1] = nums[j+1], nums[j]

                matrix_from_nums(nums, matrix)
                draw_matrix(screen, matrix)
                pygame.display.flip()

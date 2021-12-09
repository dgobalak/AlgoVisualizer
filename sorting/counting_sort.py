from helpers import *
import pygame
import sys


def counting_sort(screen, matrix, nums):
    n = len(nums)
    m = max(nums) + 1

    count = [0] * m

    # Store count of each element
    for i in range(0, n):
        count[nums[i]] += 1

    # Store rolling sum
    for i in range(1, m):
        count[i] += count[i - 1]

    nums[0:count[1]] = [0] * len(nums[0:count[1]])
    for i, val in enumerate(count):
        if i < len(count) - 1:
            nums[val:count[i+1]] = [i+1] * len(nums[val:count[i+1]])
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            matrix_from_nums(nums, matrix)
            draw_matrix(screen, matrix)
            pygame.display.flip()


from helpers import *
import pygame
import sys


def counting_sort(screen, matrix, nums):
    nums_size = len(nums)
    count_size = max(nums) + 1

    count = [0] * count_size

    # Store element counts in count array
    for i in range(0, nums_size):
        count[nums[i]] += 1

    # Calculate cumulative sum of count
    for i in range(1, count_size):
        count[i] += count[i - 1]

    nums[0: count[1]] = 0
    for i, val in enumerate(count):
        if i + 1 < len(count):
            nums[val: count[i+1]] = i+1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            matrix_from_nums(nums, matrix)
            draw_matrix(screen, matrix)
            pygame.display.flip()

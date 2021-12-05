from helpers import *
import pygame 

def selection_sort(screen, matrix, clock):
    nums = randomize_sorting_matrix(matrix)
    screen.fill(BLACK)
    clock.tick(FPS)

    for i in range(len(nums)):
        screen.fill(BLACK)
        clock.tick(FPS)

        min_i, min_val = i, nums[i]
        for j in range(i, len(nums)):
            if nums[j] <= min_val:
                min_i, min_val = j, nums[j]

        nums[i], nums[min_i] = nums[min_i], nums[i]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        matrix_from_nums(nums, matrix)
        draw_matrix(screen, matrix)
        pygame.display.flip()
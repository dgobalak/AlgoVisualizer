from helpers import *
import pygame 

def bubble_sort(screen, matrix, clock):
    nums = randomize_sorting_matrix(matrix)
    screen.fill(BLACK)
    clock.tick(FPS)

    for i in range(len(nums)-1):
        screen.fill(BLACK)
        clock.tick(FPS)

        for j in range(0, len(nums)-i-1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            if nums[j+1] < nums[j]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

            matrix_from_nums(nums, matrix)
            draw_matrix(screen, matrix)
            pygame.display.flip()
from helpers import *
import pygame 

def insertion_sort(screen, matrix, clock):
    nums = randomize_sorting_matrix(matrix)
    screen.fill(BLACK)
    clock.tick(FPS)

    for i in range(1, len(nums)):
        screen.fill(BLACK)
        clock.tick(FPS)
        
        val = nums[i]
        
        for j in range(i-1, -1, -1):
            if nums[j] > val:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                continue
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        matrix_from_nums(nums, matrix)
        draw_matrix(screen, matrix)
        pygame.display.flip()
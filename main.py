import pygame
import time
import random

LIGHT_GREEN = (199, 240, 216)
DARK_GREEN = (67, 82, 61)

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True

snake_x = random.randint(1,500)
snake_y = random.randint(1,500)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(LIGHT_GREEN)

    pygame.draw.rect(screen, (255, 0, 0), (snake_x, snake_y, 10, 10))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        print("Left arrow key pressed")
    elif keys[pygame.K_RIGHT]:
        print("Right arrow key pressed")
    elif keys[pygame.K_UP]:
        print("Up arrow key pressed")
    elif keys[pygame.K_DOWN]:
        print("Down arrow key pressed")

    pygame.display.flip()
    clock.tick(30)
pygame.quit()

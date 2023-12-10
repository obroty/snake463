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
snake_x_change = 0
snake_y_change = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(LIGHT_GREEN)

    pygame.draw.rect(screen, (255, 0, 0), (snake_x, snake_y, 10, 10))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        snake_x_change = -5
        snake_y_change = 0
    elif keys[pygame.K_RIGHT]:
        snake_x_change = 5
        snake_y_change = 0
    elif keys[pygame.K_UP]:
        snake_y_change = -5
        snake_x_change = 0
    elif keys[pygame.K_DOWN]:
        snake_y_change = 5
        snake_x_change = 0

    snake_x += snake_x_change
    snake_y += snake_y_change

    pygame.display.flip()
    clock.tick(30)
pygame.quit()

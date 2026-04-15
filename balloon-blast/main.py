import pygame
import numpy as np
from balloon import Balloon
from utils import draw_text

# Initialize
pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Blast Game")

clock = pygame.time.Clock()

balloons = []
score = 0

# Game loop
running = True

while running:
    screen.fill((255, 255, 255))

    # Spawn balloons randomly
    if np.random.rand() < 0.03:
        balloons.append(Balloon(WIDTH))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for balloon in balloons[:]:
                if balloon.is_clicked(pos):
                    balloons.remove(balloon)
                    score += 1

    # Update balloons
    for balloon in balloons[:]:
        balloon.move()
        balloon.draw(screen)

        if balloon.y > HEIGHT:
            balloons.remove(balloon)

    draw_text(screen, f"Score: {score}", 30, 10, 10)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
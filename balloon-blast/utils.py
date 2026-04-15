import pygame

def draw_text(screen, text, size, x, y):
    font = pygame.font.SysFont(None, size)
    render = font.render(text, True, (0, 0, 0))
    screen.blit(render, (x, y))
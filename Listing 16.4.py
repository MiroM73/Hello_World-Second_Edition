import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
pygame.draw.circle(screen, [255, 0, 0], [60, 60], 30, 0)
pygame.draw.rect(screen, [255, 0, 0], [60, 110, 150, 100], 0)
my_list = [60, 220, 150, 100]
pygame.draw.rect(screen, [255, 0, 0], my_list, 0)
my_rect = pygame.Rect(60, 330, 150, 100)
pygame.draw.rect(screen, [255, 0, 0], my_rect, 0)


pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
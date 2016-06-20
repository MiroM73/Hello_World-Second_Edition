import pygame, math
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])

# loops from left to right x = 0 to 639
for x in range(0, 640):
    # calculates the y position (vertical) of each point
    y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)
    # draws the point using a small rectangle [x, y, 1, 1]
    # To draw each point, we used a rectangle 1 pixel wide by 1 pixel high.
    # Note that we also used a line width of 1, not 0.
    # If we used a line width of 0, nothing would show up, because there's
    # no "middle" to fill in.
    pygame.draw.rect(screen,[0, 0, 0], [x, y, 1, 1], 1)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
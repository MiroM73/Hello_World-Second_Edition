import pygame, math, time
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255,255,255])
pygame.display.flip()
time.sleep(2)
plotPoints = []
plotPoints.append([0, (int(math.sin( 0 / 640.0 * 4 * math.pi) * 200 + 240))])

for x in range(1, 640):
    y = int(math.sin( x / 640.0 * 4 * math.pi) * 200 + 240)
    # adds each point to the list
    plotPoints.append([x, y])
    # draws the whole curve with the draw.lines() function
    # if we increase the line width to 2, it looks even better
    pygame.draw.lines(screen,[0, 0, 0], False, plotPoints, 2)
    pygame.display.flip()
    time.sleep(0.01)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
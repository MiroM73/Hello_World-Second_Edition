# the logarithmic function for X with base 2
import pygame, math, time
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
time.sleep(2)

i = 0
line_y = 300
dots = []
dots.append([320, (480 - (int(math.log(1,2) * 30 + 150)))])

pygame.draw.line(screen,[0, 0, 0],[0, 330],[640, 330], 3)
pygame.draw.line(screen,[0, 0, 0],[320, 0],[320, 480], 3)
pygame.display.flip()

for x in range(2, 320):
    y = 480 - (int(math.log(x,2) * 30 + 150))
    dots.append([(x+320), y])
    pygame.draw.lines(screen,[255, 0, 0], False, dots, 2)
    i = i + 1
    if i == 30:
        for j in range(0, 160):
            pygame.draw.rect(screen, [0, 0, 0], [j*4, line_y, 1, 1], 1)
        line_y -= i
        i = 0
    pygame.display.flip()
    time.sleep(0.01)
    del dots[0]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
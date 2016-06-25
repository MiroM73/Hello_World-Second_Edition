import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load("beach_ball.png")
x = 50
y = 50
x_speed = 10

running = True
# ball moves from side to side after putting code into the endlees while loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(20)
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
    x += x_speed
    # here we are controlling, if ball hits either edge of the window
    if x > screen.get_width() - 90 or x < 0:
        # when the ball hits the edge, reverse direction for move is set by the oposite sign
        x_speed = - x_speed
    screen.blit(my_ball, [x, y])
    pygame.display.flip()

pygame.quit()
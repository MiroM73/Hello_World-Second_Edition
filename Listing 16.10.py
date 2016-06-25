import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])

# loads the image beach_ball from disk and creates an object my_ball
my_ball = pygame.image.load("beach_ball.png")
# the method blit copies the object my_ball onto the screen
screen.blit(my_ball, [50, 50])
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
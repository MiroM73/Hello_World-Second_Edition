import pygame

pygame.init()
screen = pygame.display.set_mode([640, 480])

# fills the windows with the white background
screen.fill([255,255,255])

# draws a circle
pygame.draw.circle(screen,[255, 0, 0], [100, 100], 30, 0)


# flips your monitor ower .... just kidding!
# What's the "flip"?
# The display object in Pygame (ours is called screen, which
# we created in line 3 of listing 16.3) has two copies of
# whatever is displayed in the Pygame window. The
# reason is that, when we start doing animation, we
# want to make it as smooth and fast as possible. So
# instead of updating the display every time we make a small change to our
# graphics, we can make a number of changes and then "flip" to the new version of
# the graphics. This makes the changes appear all at once, instead of one by one. This way we
# don't get half-drawn circles (or aliens, or whatever) on our display.
# Think of the two copies as being a current screen and a "next" screen. The current screen is
# what you see right now. The "next" screen is what you'll see when you do a flip. You make
# all your changes on the "next" screen and then flip to it so you can see them.
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
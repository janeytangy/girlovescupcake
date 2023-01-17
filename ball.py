import sys, pygame              # import pygame
pygame.init()                   # initializes the pygame modules

size = width, height = 320, 240 # set screen size
speed = [4, 2]                  # [x = horizonal speed, y = vertical speed]
black = 0, 0, 0

screen = pygame.display.set_mode(size) # create a graphical window

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()      # gets rectangle for ball movement coordinates

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()       # method makes everything drawn on the screen visible
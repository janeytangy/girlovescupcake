import pygame
import random

pygame.init()
pygame.mixer.init()

size = width, height = 800, 800
screen = pygame.display.set_mode(size)

image = pygame.image.load("kitchen.jpeg")

cupcake = pygame.image.load("cupcake.png")
cupcakerect = cupcake.get_rect()

speed_x = random.randint(1, 2)
speed_y = random.randint(1, 2) 
speed = [speed_x, speed_y]
# speed = [2, 2] 

gir = pygame.image.load("gir.png")
gir_x = 325
gir_y = 325
girrect = gir.get_rect(center=(325, 325))

yum = pygame.mixer.Sound("yum.ogg")

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    cupcakerect = cupcakerect.move(speed)
    if cupcakerect.left < 0 or cupcakerect.right > width:
        speed[0] = -speed[0]
    if cupcakerect.top < 0 or cupcakerect.bottom > height:
        speed[1] = -speed[1]

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: girrect.move_ip(0, -1)
    if pressed[pygame.K_DOWN]: girrect.move_ip(0, 1)
    if pressed[pygame.K_LEFT]: girrect.move_ip(-1, 0)
    if pressed[pygame.K_RIGHT]: girrect.move_ip(1, 0)

    collide = cupcakerect.colliderect(girrect)
    if collide == True:
        speed = [0,0]
        cupcakerect.left = -1000
        yum.play()

    screen.blit(image, (0, 0))
    screen.blit(cupcake, cupcakerect)
    screen.blit(gir, girrect)
    pygame.display.flip()       # method makes everything drawn on the screen visible

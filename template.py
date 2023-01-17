import sys, pygame                                  # imports pygame
pygame.init()                                       # initialize pygame

screen = pygame.display.set_mode((800,400))         # set display screen

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT                # if you close the window,
            pygame.quit()                           # you will quit the game
            exit()                                  # and exit the window.
    
    """
    draw elements and update variables
    """

    pygame.display.update()                         # displays all drawn elements
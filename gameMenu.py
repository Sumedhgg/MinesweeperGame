import pygame,sys
from pygame.locals import *
pygame.init()
BLUE = (0, 0, 255)
def displayMenu(gameWindow):
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    pygame.display.set_caption("Welcome To Minesweeper!")
    font = pygame.font.SysFont('Corbel',35)
    exit = font.render('QUIT', True, RED)
    start = font.render('START', True, RED)
    rrun = 1
    run = True
    while run:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 0 <= pos[0] <= 40  and 360 <= pos[1] <= 400:
                    run = False
                    rrun = 5
                elif 260 <= pos[0] <= 300 and 360 <= pos[1] <= 400:
                    run = False
        gameimage = pygame.image.load('Sprites/gameMenu.png')
        gameWindow.blit(gameimage,(0,0))
        if 0 <= pos[0] <= 40  and 380 <= pos[1] <= 400:
            pygame.draw.rect(gameWindow, BLUE, [0, 360, 100, 40])
        elif  260 <= pos[0] <= 300 and 380 <= pos[1] <= 400:
            pygame.draw.rect(gameWindow, BLUE, [220, 360, 120, 40])
        gameWindow.blit(exit, (220,360))
        gameWindow.blit(start, (1,360))
        pygame.display.update()
    if rrun == 5:
        return False
    else:
        return True

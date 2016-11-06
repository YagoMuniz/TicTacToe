import pygame, sys, os, time
from pygame.locals import *

# Definições do pygame
clock = pygame.time.Clock()

pygame.init()
pygame.font.init()

font_name = pygame.font.get_default_font()
game_font = pygame.font.SysFont(font_name, 175)
winner_font = pygame.font.SysFont(font_name, 48)
label_font = pygame.font.SysFont(font_name, 35)


window = pygame.display.set_mode((700, 400))

screen = pygame.display.get_surface()
pygame.display.set_caption("Teste")

def main():
    backMenu_file = os.path.join("Images", "Field.png")
    backMenu = pygame.image.load(backMenu_file)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(backMenu, (0, 0))

    gambs = 10

    while running:

        gambs += 10
        pygame.display.flip()
        run()


#=============================================================

def add(x, y, xi, yi):
    global n
    global habilitado
    if tab[x][y] == 0:
        screen.blit(vez[n], (xi, yi))
        tab[x][y] = n
        if winner(n):
            text = winner_font.render("VENCEDOR X" if n == 1 else "VENCEDOR O", 1, (255, 0, 0))
            screen.blit(text, (450, 25))
            habilitado = False
        n *= -1

"""
00 01 02
10 11 12
20 21 22
"""

def winner(vez):
    global tab
    pontos = vez*3

    return (sum(tab[0]) == pontos or sum(tab[1]) == pontos
        or sum(tab[2]) == pontos
        or tab[0][0] + tab[1][0] + tab[2][0] == pontos
        or tab[0][1] + tab[1][1] + tab[2][1] == pontos
        or tab[0][2] + tab[1][2] + tab[2][2] == pontos
        or tab[0][0] + tab[1][1] + tab[2][2] == pontos
        or tab[0][2] + tab[1][1] + tab[2][0] == pontos)

def run():
    
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif habilitado:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] >= 0 and event.pos[0] <= 110:
                    if event.pos[1] >= 0 and event.pos[1] <= 115:
                        add(0, 0, 10, 0)
                    elif event.pos[1] > 115 and event.pos[1] <= 267:
                        add(1, 0, 10, 140)
                    elif event.pos[1] > 267 and event.pos[1] <= 400:
                        add(2, 0, 10, 275)
                elif event.pos[0] > 110 and event.pos[0] <= 260:
                    if event.pos[1] >= 0 and event.pos[1] <= 115:
                        add(0, 1, 140, 0)
                    elif event.pos[1] > 115 and event.pos[1] <= 267:
                        add(1, 1, 140, 140)
                    elif event.pos[1] > 267 and event.pos[1] <= 400:
                        add(2, 1, 140, 275)
                elif event.pos[0] > 260 and event.pos[0] <= 400:
                    if event.pos[1] >= 0 and event.pos[1] <= 115:
                        add(0, 2, 290, 0)
                    elif event.pos[1] > 115 and event.pos[1] <= 267:
                        add(1, 2, 290, 140)
                    elif event.pos[1] > 267 and event.pos[1] <= 400:
                        add(2, 2, 290, 275)



running = True
habilitado = True

tab = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

vez = {
    1 : game_font.render("X", 1, (0, 0, 0)),
    -1 : game_font.render("O", 1, (0, 0, 0))
}
n = 1

if __name__ == "__main__":
    main()

pygame.display.quit()

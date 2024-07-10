import pygame
from constant import *
import game

pygame.init()

window = pygame.display.set_mode((X,Y), 0, 32)
pygame.display.set_caption("Tic Tac Toe")

def main():
    while True:
        game.menu(window)


if __name__ == "__main__":
    main()
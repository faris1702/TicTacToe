import pygame, sys
from pygame.locals import *
import ttt
import math
from constant import *

pygame.init()




#used to print text on screen
def print_text(text, color, size, x_pos, y_pos, win, highlight=None):
    font = pygame.font.SysFont(None, size)
    text = font.render(text, True, color, highlight)
    txtRct = text.get_rect()
    txtRct.center = (x_pos, y_pos)
    win.blit(text, txtRct)

def update_board(player, x_pos, y_pos, win):
    if x_pos >= 3:
        x_pos = int(math.floor(x_pos // 140))
        y_pos = int(math.floor(y_pos // 140))
        if (x_pos == 3):
            x_pos = 2
        if (y_pos == 3):
            y_pos = 2

    x_pos = (x_pos * 140) + 70
    y_pos = (y_pos * 140) + 70

    if player == 'X':
        color = blue
    else:
        color = black
    print_text(player, color, 80, x_pos, y_pos, win)
    pygame.display.update()

def displayGrid(grid, win):
    win.fill(white)
    pygame.draw.line(win, black, (X//3, 0), (X//3, Y), 3)
    pygame.draw.line(win, black, ((X//3)*2, 0), ((X//3)*2, Y), 3)
    pygame.draw.line(win, black, (0, Y//3), (X, Y//3), 3)
    pygame.draw.line(win, black, (0, (Y//3)*2), (X, (Y//3)*2), 3)

def printWin(win, type):
    pygame.draw.rect(win, white, pygame.Rect(0, Y/2 - 45, X, 90))
    if type == 'X':
        type = 1
    else:
        type = 2
    print_text(f"Player {type} won", green, 90, X/2, Y/2, win)
    pygame.display.update()

def printDraw(win):
    pygame.draw.rect(win, white, pygame.Rect(0, Y/2 - 45, X, 90))
    print_text("It is a draw", red, 90, X/2, Y/2, win)
    pygame.display.update()

def printLose(win):
    pygame.draw.rect(win, white, pygame.Rect(0, Y/2 - 45, X, 90))
    print_text(f"AI won", red, 90, X/2, Y/2, win)
    pygame.display.update()

def print_menu(win):
    win.fill(white)
    pygame.draw.line(win, black, (X/3,0), (X/3, Y), 1)
    pygame.draw.line(win, black, ((X/3)*2,0), ((X/3)*2, Y), 1)
    print_text("1 Player", black, 40, 70, Y/2, win)
    print_text("2 Player", black, 40, 210, Y/2, win)
    print_text("Quit", black, 40, 350, Y/2, win)
    pygame.display.update()

def print_difficulty(win):
    win.fill(white)
    pygame.draw.line(win, black, (X/3,0), (X/3, Y), 1)
    pygame.draw.line(win, black, ((X/3)*2,0), ((X/3)*2, Y), 1)
    print_text("Easy", black, 40, 70, Y/2, win)
    print_text("Medium", black, 40, 210, Y/2, win)
    print_text("Hard", black, 40, 350, Y/2, win)
    pygame.display.update()

def print_line(win, lst):
    x1 = lst[0][0]
    x2 = lst[2][0]
    y1 = lst[0][1]
    y2 = lst[2][1]

    x1 = (x1 * 140) + 70
    x2 = (x2 * 140) + 70
    y1 = (y1 * 140) + 70
    y2 = (y2 * 140) + 70

    
    pygame.draw.line(win, red, (x1, y1),(x2, y2), 6)
    pygame.display.update()

    

    
            


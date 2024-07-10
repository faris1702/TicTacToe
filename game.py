import pygame, sys
from pygame.locals import *
import ttt
import gui
from constant import *


def menu(win):
    gui.print_menu(win)
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x < X/3:  #1 player chosen
                    select_diff(win)
                elif x < (X/3)*2:  #2 player chosen
                    init_game(win, 2)
                else:
                    pygame.quit()
                    sys.exit()

def select_diff(win):
    gui.print_difficulty(win)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x < X/3:
                    diff = 1
                elif x < (X/3)*2:
                    diff = 3
                else:
                    diff = 8
                init_game(win, 1, diff)

def init_game(win, game_type, diff = 0):
    grid = ttt.createGrid()
    gui.displayGrid(grid, win)
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)

    while True:
        player = ttt.getTurn(grid) 

        #if 1 player vs AI
        if game_type == 1 and player == 'O':
            pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
            pygame.time.delay(500)
            bMove = ttt.bestMove(grid, diff)
            ttt.choose(player, grid, bMove[0], bMove[1])
            gui.update_board(player, bMove[0], bMove[1], win)
            pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                flag = ttt.choose(player, grid, x, y)
                if flag != False:  #if valid input
                    gui.update_board(player, x, y, win)

            #check end game
            result, lst = ttt.checkWin(grid)
            if result == True:
                gui.print_line(win, lst)
                pygame.time.delay(1000)
                print(f"type: {game_type}")
                if player == 'X' or game_type == 2:
                    gui.printWin(win, grid[lst[0][0]][lst[0][1]])
                else:
                    gui.printLose(win)
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                pygame.time.delay(1000)
                menu(win)

            elif ttt.checkDraw(grid):
                gui.printDraw(win)
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                pygame.time.delay(1000)
                menu(win)

                    
            pygame.display.update()


    

        
            

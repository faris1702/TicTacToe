from constant import *
import math

def createGrid():
    grid = []
    for i in range(size):
        row = [' ' for j in range(size)]
        grid.append(row)
    return grid


def display(grid):
    for i in range(size):
        for j in range(size):
            print(grid[i][j], end = ' ')
            if (j != size - 1):
                print('|', end = ' ')
            else:
                print('')
        if i != size - 1:
            print('-'*(((size-2)*4)+5))
    print()


def choose(player, grid, x_pos, y_pos):
    if (x_pos >= 3 or y_pos >= 3):
        x_pos = int(math.floor(x_pos // 140))
        y_pos = int(math.floor(y_pos // 140))
        if (x_pos == 3):
            x_pos = 2
        if (y_pos == 3):
            y_pos = 2

    #choose used spot
    if grid[x_pos][y_pos] != ' ': 
        return False

    grid[x_pos][y_pos] = player
    return True

def checkWin(grid):
    lst1 = [] #used to temporarily store vertical, horizontal and diagonal columns
    lst2 = []
    pos_lst1 = []
    pos_lst2 = []

    for i in range(size):
        for j in range(size):
            lst1.append(grid[i][j])
            lst2.append(grid[j][i])
            pos_lst1.append([i,j])
            pos_lst2.append([j,i])

        #check row
        result = all(k == lst1[0] for k in lst1) and lst1[0] != ' '
        if result == True:
            return True, pos_lst1
        
        #check col
        result = all(k == lst2[0] for k in lst2) and lst2[0] != ' '
        if result == True:
            return True, pos_lst2
        
        lst1 = []
        lst2 = []
        pos_lst1 = []
        pos_lst2 = []

    #check diagonal
    for i in range(size):
        lst1.append(grid[i][i])
        pos_lst1.append([i,i])
    result = all(k == lst1[0] for k in lst1) and lst1[0] != ' '
    if result == True:
        return True, pos_lst1
    
    #check anti-diagonal
    temp = size - 1
    for i in range(size):
        lst2.append(grid[i][temp])
        pos_lst2.append([i,temp])
        temp -= 1
    result = all(k == lst2[0] for k in lst2) and lst2[0] != ' '
    if result == True:
        return True, pos_lst2
    
    return False, None
            
def checkDraw(grid):
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ' ':
                return False
    return True

def getTurn(grid):
    count_x = 0
    count_y = 0
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 'X':
                count_x += 1
            elif grid[i][j] == 'O':
                count_y += 1

    if count_x > count_y:
        return 'O'
    return 'X'


#-------------------------MINIMAX PART-----------------------------
# return +10 if AI wins
# return -10 if AI loses
# return 0 if draw
def evaluate(grid):  #works
    lst1 = [] #used to temporarily store vertical, horizontal and diagonal columns
    lst2 = []

    for i in range(size):
        for j in range(size):
            lst1.append(grid[i][j])
            lst2.append(grid[j][i])

        #check row
        result = all(k == lst1[0] for k in lst1)
        if result == True and lst1[0] == 'O':
            return 10 
        elif result == True and lst1[0] == 'X':
            return -10 
        
        #check col
        result = all(k == lst2[0] for k in lst2)
        if result == True and lst2[0] == 'O':
            return 10 
        elif result == True and lst2[0] == 'X':
            return -10
        
        lst1 = []
        lst2 = []

    #check diagonal
    for i in range(size):
        lst1.append(grid[i][i])
    result = all(k == lst1[0] for k in lst1)
    if result == True and lst1[0] == 'O':
        return 10 
    elif result == True and lst1[0] == 'X':
        return -10 
    
    #check anti-diagonal
    temp = size - 1
    for i in range(size):
        lst2.append(grid[i][temp])
        temp -= 1
    result = all(k == lst2[0] for k in lst2)
    if result == True and lst2[0] == 'O':
        return 10 
    elif result == True and lst2[0] == 'X':
        return -10 
    
    return 0



def bestMove(grid, depth):
    bValue = -1000
    bMove = (-1, -1)

    for i in range(size):
         for j in range(size):
            if grid[i][j] == ' ':
                grid[i][j] = 'O'
                moveValue = minimax(grid, 0, False, depth, -float("inf"), float("inf"))
                grid[i][j] = ' '
                if (moveValue > bValue):
                    bValue = moveValue
                    bMove = (i, j)
        
    return bMove

def haveMove(grid):
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ' ':
                return True
            
    return False



def minimax(grid, depth, maxTurn, maxDepth, alpha, beta):
    global count  
    score = evaluate(grid)

    if score == 10:  #AI win
        return 10 - depth
    
    elif score == -10:  #AI lose
        return -10 + depth
    
    elif haveMove(grid) == False:  #AI draw
        return 0
    
    elif depth > maxDepth:  #reached max depth
        return 0
    
    flag = False
    if (maxTurn):  #AI/maximizer turn
        maxValue = -float("inf")
        for i in range(size):
            if flag:
                break
            for j in range(size):
                if grid[i][j] == ' ':
                    grid[i][j] = 'O'
                    value = minimax(grid, depth+1, not maxTurn, maxDepth, alpha, beta)
                    grid[i][j] = ' '
                    maxValue = max(maxValue, value)

                    #alpha-beta pruning
                    alpha = max(alpha, maxValue)
                    if beta <= alpha:
                        flag = True
                        break

        return maxValue

    else:  #player/minimizer turn
        minValue = float("inf")
        for i in range(size):
            if flag:
                break
            for j in range(size):
                if grid[i][j] == ' ':
                    grid[i][j] = 'X'
                    value = minimax(grid, depth+1, not maxTurn, maxDepth, alpha, beta)
                    grid[i][j] = ' '
                    minValue = min(minValue, value)

                    #alpha-beta pruning
                    beta = min(beta, minValue)
                    if beta <= alpha:
                        flag = True
                        break
        return  minValue



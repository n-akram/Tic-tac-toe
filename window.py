'''
A simple window based tic-tac-toe
Note:   1. numpad based

Date: 31.07.2019
'''

import pygame
import easygui
import sys
import random
from pygame.locals import *

# Hide the pygame prompt
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

#easygui.msgbox("This is a message!", title="simple gui")

FLAG = True
STATUS = "IDLE"
BOXES = []
TRANSLATEDORDER = [7, 4, 1, 8, 5, 2, 9, 6, 3]
BOARD_CONTENT = ['','','','','','','','','']
copyBd = BOARD_CONTENT.copy()

background_colour = (100,80,60)
text_colour = (90,230,65)
 
def getCharacter():
    global FLAG
    global BOARD_CONTENT
    BOARD_CONTENT = ['','','','','','','','','']
    t = easygui.ynbox(msg='What do you want to be?', 
            title='Welcome to Tic-Tac-Toe ', choices=('[<F1>]X', '[<F2>]O'), 
            image=None, cancel_choice='[<F2>]No')
    if t == True:
        return('X', 'O')
    elif t == False:
        return('O', 'X')
    FLAG = False
    return('_', '_')
    
def drawOnBoard(screen, t, pos):
    myfont = pygame.font.SysFont('Comic Sans MS', 100)
    textsurface = myfont.render(t, False, (0, 0, 0))
    screen.blit(textsurface,(pos[0]+15,pos[1]-25))
    pygame.display.update()
    
def updateStatus(screen):
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = myfont.render(STATUS, False, text_colour)
    pygame.draw.rect(screen,background_colour,(10,500,550,100))
    screen.blit(textsurface,(10,500))
    pygame.display.update()
    
def playAgain():
    t = easygui.ynbox(msg='Do you want to play again?', 
            title='Welcome to Tic-Tac-Toe ', choices=('[<F1>]Yes', '[<F2>]No'), 
            image=None, cancel_choice='[<F2>]No')
    if t == True:
        return True
    else:
        return False
        
def chooseRandomMoveFromList(movesList):

    # Returns a valid move from the passed list on the passed board.

    # Returns None if there is no valid move.
    
    board = BOARD_CONTENT
    
    possibleMoves = []

    for i in movesList:

        if isSpaceFree(i):

            possibleMoves.append(i)



    if len(possibleMoves) != 0:

        return random.choice(possibleMoves)

    else:

        return None

def getComputerMove(computerLetter):
    copyBd = BOARD_CONTENT.copy()
    
    # Given a board and the computer's letter, determine where to move and return that move.

    if computerLetter == 'X':

        playerLetter = 'O'

    else:

        playerLetter = 'X'
        
    # Here is our algorithm for our Tic Tac Toe AI:

    # First, check if we can win in the next move

    for i in range(1, 10):

        if isSpaceFree(i):

            makeMove(computerLetter, i, copyBd)

            if isWinner(computerLetter, copyBd):

                return i

    # Check if the player could win on their next move, and block them.

    for i in range(1, 10):

        #copy = board

        if isSpaceFree(i):

            makeMove(playerLetter, i, copyBd)

            if isWinner(playerLetter, copyBd):

                return i
                

    # Try to take one of the corners, if they are free.

    move = chooseRandomMoveFromList([1, 3, 7, 9])

    if move != None:

        return move



    # Try to take the center, if it is free.

    if isSpaceFree(5):

        return 5



    # Move on one of the sides.

    return chooseRandomMoveFromList([2, 4, 6, 8])

def resetBoard():
    global STATUS
    global BOXES
    pygame.init()
    pygame.font.init()
    (Twidth, Theight) = (550, 550) # total size
    BLUEish=(100,200,255)
    WHITE=(255,255,255)
    screen = pygame.display.set_mode((Twidth, Theight))
    screen.fill(background_colour)
    updateStatus(screen)
    pygame.display.flip()
    pygame.display.set_caption('Tic-Tac-Toe')
    itol = 0
    for i in range(3):
        jtol = 0
        for j in range(3):
            x = i*100 + 50 + itol
            y = j*100 + 50 + jtol
            pygame.draw.rect(screen,BLUEish,(x, y,100,100))
            jtol += 50
            BOXES.append([x,y])
        itol += 50
    pygame.display.update()
    return(screen)

#easygui.egdemo()

def isSpaceFree(move):
    if move == 0:
        return False
    else:
        return BOARD_CONTENT[move-1] == ''
    
def makeMove(letter, move, bd = BOARD_CONTENT):
    bd[move-1] = letter

def getPlayerMove(screen):
    move = 0
    global STATUS
    STATUS = 'What is your next move? (1-9 of at numpad layout)'
    updateStatus(screen)
    while move not in [1,2,3,4,5,6,7,8,9] or not isSpaceFree(move):
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_KP1]:
                move = 1
            if pressed[pygame.K_KP2]:
                move = 2
            if pressed[pygame.K_KP3]:
                move = 3
            if pressed[pygame.K_KP4]:
                move = 4
            if pressed[pygame.K_KP5]:
                move = 5
            if pressed[pygame.K_KP6]:
                move = 6
            if pressed[pygame.K_KP7]:
                move = 7
            if pressed[pygame.K_KP8]:
                move = 8
            if pressed[pygame.K_KP9]:
                move = 9
    return move
    
def updateBoard(screen):
    i = 1
    for ele in BOARD_CONTENT:
        drawOnBoard(screen, ele, BOXES[TRANSLATEDORDER.index(i)])
        i += 1

def isWinner(le, bo=BOARD_CONTENT):

    # Given a board and a player’s letter, this function returns True if that player has won.

    # We use bo instead of board and le instead of letter so we don’t have to type as much.

    return ((bo[7-1] == le and bo[8-1] == le and bo[9-1] == le) or # across the top

    (bo[4-1] == le and bo[5-1] == le and bo[6-1] == le) or # across the middle

    (bo[1-1] == le and bo[2-1] == le and bo[3-1] == le) or # across the bottom

    (bo[7-1] == le and bo[4-1] == le and bo[1-1] == le) or # down the left side

    (bo[8-1] == le and bo[5-1] == le and bo[2-1] == le) or # down the middle

    (bo[9-1] == le and bo[6-1] == le and bo[3-1] == le) or # down the right side

    (bo[1-1] == le and bo[5-1] == le and bo[9-1] == le) or # diagonal

    (bo[7-1] == le and bo[5-1] == le and bo[3-1] == le)) # diagonal

def isBoardFull():
    # Return True if every space on the board has been taken. Otherwise return False.

    for i in range(1, 10):

        if isSpaceFree(i):

            return False

    return True
    
    
def whoGoesFirst():

    # Randomly choose the player who goes first.

    if random.randint(0, 1) == 0:

        return 'computer'

    else:

        return 'player'

while True:
    screen = resetBoard()
    playerLetter, computerLetter = getCharacter()
    if not(FLAG):
        break
    
    turn = whoGoesFirst()
    myfont = pygame.font.SysFont('Comic Sans MS', 15)
    state = turn + ' goes first. Player character is ' + playerLetter
    textsurface = myfont.render(state, False, text_colour)
    screen.blit(textsurface,(10,10))
    pygame.display.update()
    updateStatus(screen)

    gameIsPlaying = True
    
    while gameIsPlaying:
        if turn == 'player':

            # Player’s turn.

            updateBoard(screen)

            move = getPlayerMove(screen)

            makeMove(playerLetter, move, BOARD_CONTENT)

            if isWinner(playerLetter, BOARD_CONTENT):

                updateBoard(screen)

                STATUS = 'Hooray! You have won the game!'
                updateStatus(screen)

                gameIsPlaying = False

            else:

                if isBoardFull():

                    updateBoard(screen)

                    STATUS = 'The game is a tie!'
                    updateStatus(screen)

                    break

                else:

                    turn = 'computer'

        else:

            # Computer’s turn.

            move = getComputerMove(computerLetter)

            makeMove(computerLetter, move, BOARD_CONTENT)
            
            if isWinner(computerLetter, BOARD_CONTENT):
                updateBoard(screen)

                STATUS = 'The computer has beaten you! You lose.'
                updateStatus(screen)
                
                gameIsPlaying = False

            else:
                if isBoardFull():

                    updateBoard(screen)

                    STATUS = 'The game is a tie!'
                    updateStatus(screen)
                    
                    break

                else:
                    turn = 'player'
    
    if not playAgain():

        break
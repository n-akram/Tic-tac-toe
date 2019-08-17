'''
Engine for GUI based tic-tac-toe
Date: 03.08.2019
'''
from gui.variables import *

import random
import winsound

def resetVar():
    global FLAG
    global STATUS
    global BOXES
    global BOARD_CONTENT
    global copyBd
    
    global BG_IMAGE
    global X_IMAGE 
    global O_IMAGE 
    
    FLAG = True
    STATUS = "IDLE"
    BOXES = []
    
    BOARD_CONTENT = ['','','','','','','','','']
    copyBd = BOARD_CONTENT.copy()
    
    BG_IMAGE = None
    X_IMAGE = None
    O_IMAGE = None
    
def resetGameVar():
    global BOXES
    global BOARD_CONTENT
    global copyBd
    
    global BG_IMAGE
    global X_IMAGE 
    global O_IMAGE 
    
    
    BOARD_CONTENT = ['','','','','','','','','']
    BOXES = []
    copyBd = BOARD_CONTENT.copy()
    
def isSpaceFree(move):
    global BOARD_CONTENT
    if move == 0:
        return False
    else:
        return BOARD_CONTENT[move-1] == ''

def makeMove(move, char = ''):
    global BOARD_CONTENT
    global player_character
    global Sound
    if char == '':
        if player_character[0] == 1:
            BOARD_CONTENT[move-1] = 'X'
        else:
            BOARD_CONTENT[move-1] = 'O'
    else:
        BOARD_CONTENT[move-1] = char
    if Sound[0]:
        #print(Sound[1])
        winsound.Beep(Sound[3],200)
    return(BOARD_CONTENT)

def makeDummyMove(computerLetter, i, copyBd):
    copyBd[i-1] = computerLetter
    return(copyBd)

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def getCharacter():
    global player_character
    if player_character[0] == 1:
        return('X', 'O')
    else:
        return('O', 'X')

def isWinner(le, bo):
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
    global BOARD_CONTENT
    copyBd = BOARD_CONTENT.copy()
    
    # Given a board and the computer's letter, determine where to move and return that move.

    if computerLetter == 'X':

        playerLetter = 'O'

    else:

        playerLetter = 'X'
        
    # Here is our algorithm for our Tic Tac Toe AI:

    # First, check if we can win in the next move

    for i in range(1, 10):
        copyBd = BOARD_CONTENT.copy()
        if isSpaceFree(i):

            copyBd = makeDummyMove(computerLetter, i, copyBd)

            if isWinner(computerLetter, copyBd):

                return i

    # Check if the player could win on their next move, and block them.

    for i in range(1, 10):
        copyBd = BOARD_CONTENT.copy()
        #copy = board

        if isSpaceFree(i):

            copyBd = makeDummyMove(playerLetter, i, copyBd)

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

def isBoardFull():
    global BOARD_CONTENT
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(i):
            return False
    return True
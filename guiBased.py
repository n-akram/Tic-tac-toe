'''
GUI based based tic-tac-toe
Note:   1. GUI based
        2. Credits in GAME CREDITS

Date: 03.08.2019
'''
import pygame
import sys
import random
from pygame.locals import *
import time
import sys

from gui.constants import *
from gui.variables import *

from gui.engine import *
from gui.gui_functions import *
from gui.menu import *

pygame.init()
#pygame.font.init()
screen = pygame.display.set_mode((Twidth, Theight))


def PlayerMove():
    global BOARD_CONTENT
    L = BOARD_CONTENT.count('')
    flag = True
    while flag:
        event = pygame.event.wait()
        BOARD_CONTENT = checkEvent(event)
        if event.type == pygame.QUIT:
            flag = False  # Be interpreter friendly
            pygame.quit()
            sys.exit()
        if BOARD_CONTENT.count('') < L:
            flag = False


def run_game_loop():
    resetBoard(screen)
    playerLetter, computerLetter = getCharacter()
    turn = whoGoesFirst()
    # other code
    gameIsPlaying = True
    global BOARD_CONTENT
    global GAME_SONG
    global Music
    if Music:
        pygame.mixer.music.load(GAME_SONG[0])
        pygame.mixer.music.play(-1)

    while gameIsPlaying:
        if turn == 'player':
            # Player’s turn.
            PlayerMove()
            if isWinner(playerLetter, BOARD_CONTENT):
                STATUS = 'Hooray! You have won the game!'
                
                displayEnd(STATUS, screen, 1)
                gameIsPlaying = False
            else:
                if isBoardFull():
                    STATUS = 'The game is a tie!'
                    displayEnd(STATUS, screen, 2)
                    gameIsPlaying = False
                else:
                    turn = 'computer'
        else:
            # Computer’s turn.
            move = getComputerMove(computerLetter)
            BOARD_CONTENT = makeMove(move, computerLetter)
            updateScreen(screen)
            if isWinner(computerLetter, BOARD_CONTENT):
                STATUS = 'The computer has beaten you! You lose.'
                displayEnd(STATUS, screen, 3)
                gameIsPlaying = False
            else:
                if isBoardFull():
                    STATUS = 'The game is a tie!'
                    displayEnd(STATUS, screen, 2)
                    gameIsPlaying = False
                else:
                    turn = 'player'

def resetVarHere():
    global BOARD_CONTENT
    BOARD_CONTENT = ['','','','','','','','','']

WelcomeAnimation(screen) # Welcome animation only Once
while True:
    resetVarHere()
    resetGameVar()
    running = displayMenu()
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False  # Be interpreter friendly
        pygame.quit()
        sys.exit()
    run_game_loop()
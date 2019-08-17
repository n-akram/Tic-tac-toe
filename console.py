'''
A simple console based tic-tac-toe
Note:   1. Uses engine : engine.py

Date: 31.07.2019

source : https://inventwithpython.com/chapter10.html
'''

import engine as e

print('Welcome to Tic Tac Toe!')


while True:

    # Reset the board

    theBoard = [' '] * 10

    playerLetter, computerLetter = e.inputPlayerLetter()

    turn = e.whoGoesFirst()

    print('The ' + turn + ' will go first.')

    gameIsPlaying = True



    while gameIsPlaying:

        if turn == 'player':

            # Player’s turn.

            e.drawBoard(theBoard)

            move = e.getPlayerMove(theBoard)

            e.makeMove(theBoard, playerLetter, move)



            if e.isWinner(theBoard, playerLetter):

                e.drawBoard(theBoard)

                print('Hooray! You have won the game!')

                gameIsPlaying = False

            else:

                if e.isBoardFull(theBoard):

                    e.drawBoard(theBoard)

                    print('The game is a tie!')

                    break

                else:

                    turn = 'computer'



        else:

            # Computer’s turn.

            move = e.getComputerMove(theBoard, computerLetter)

            e.makeMove(theBoard, computerLetter, move)



            if e.isWinner(theBoard, computerLetter):

                e.drawBoard(theBoard)

                print('The computer has beaten you! You lose.')

                gameIsPlaying = False

            else:

                if e.isBoardFull(theBoard):

                    e.drawBoard(theBoard)

                    print('The game is a tie!')

                    break

                else:

                    turn = 'player'



    if not e.playAgain():

        break
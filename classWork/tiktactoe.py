import random

board = [' ' for x in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[1], board[2], board[3]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[4], board[5], board[6]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[7], board[8], board[9]))
    print("     |     |")



def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or \
           (bo[4] == le and bo[5] == le and bo[6] == le) or \
           (bo[1] == le and bo[2] == le and bo[3] == le) or \
           (bo[1] == le and bo[4] == le and bo[7] == le) or \
           (bo[2] == le and bo[5] == le and bo[8] == le) or \
           (bo[3] == le and bo[6] == le and bo[9] == le) or \
           (bo[1] == le and bo[5] == le and bo[9] == le) or \
           (bo[3] == le and bo[5] == le and bo[7] == le)


def playerMove():
    run = True
    while run:
        move = input("Enter the position you want to play 'X' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('This space is occupied.')
            else:
                print('Please enter a number within the range!')
        except ValueError:
            print('Please enter a valid number.')


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = random.choice(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = random.choice(edgesOpen)
        return move

    return move


def isBoardFull(board):
    return board.count(' ') <= 1


def main():
    print('Welcome to Tic Tac Toe')
    printBoard(board)

    while not isBoardFull(board):
        if not isWinner(board, 'O'):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not isWinner(board, 'X'):
            move = compMove()
            if move == 0:
                print('Tie Game')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position:', move)
                printBoard(board)
        else:
            print('Sorry, X\'s won this time!')
            break

    if isBoardFull(board):
        print('Tie Game!')


main()

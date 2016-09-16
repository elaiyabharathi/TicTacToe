from __future__ import print_function
from IPython.display import clear_output
import random

def display_board(board):
    clear_output(board)
    for l in board:
        print(l)

def player_input():
    print('Choose marker X or O for player 1')
    marker = raw_input()
    if marker == 'X' or marker == 'O':
        print('player 1 assigned ')
        return marker
    else:
        print('incorrect assignment retry')
        player_input()

def get_row(postion):
    return (postion - 1) / 3

def get_col(position):
    return (position - 1) % 3

def place_marker(board, marker, position):
    row = get_row(position)
    col = get_col(position)
    if space_check(board, position):
        board[row][col] = marker
    display_board(board)


def other(mark):
    if mark == 'X':
        return 'O'
    else:
        return 'X'

def win_check(board, mark):
    ld = []
    rd = []
    #check across
    for l in board:
        if other(mark) not in l and '_' not in l:
            return True
    #check left diagonal
    for i in range(0,3):
        ld.append(board[i][i])
    if other(mark) not in ld and '_' not in ld:
        return True
    #check right diagonal
    j = 0
    for i in range(2,-1,-1):
        rd.append(board[j][i])
        j += 1
    if other(mark) not in rd and '_' not in rd:
        return True
    #check down
    transpose = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    for l in transpose:
        if other(mark) not in l and '_' not in l:
            return True
    return False

def space_check(board, position):
    row = get_row(position)
    col = get_col(position)
    if board[row][col] == '_':
        return True
    else:
        return False

def full_board_check(board):
    for l in board:
        if '_' in l:
            return False
    return True

def player_choice(board):
    print('enter the position where you want to mark')
    pos = int(raw_input())
    if space_check(board, pos):
        return pos
    else:
        print('position is not empty enter another')
        return player_choice(board)

def replay():
    print('Game over. press y for replay or n for quit')
    play = raw_input()
    if play == 'y':
        return True
    else:
        return False

print('Welcome to Tic Tac Toe')

while True:
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    player1_marker = player_input()
    player2_marker = other(player1_marker)
    game_on = True
    # print board
    display_board(board)
    while game_on:
        if full_board_check(board):
            break
        #player 1 input
        print('player 1')
        player1_pos = player_choice(board)
        place_marker(board, player1_marker, player1_pos)
        if win_check(board, player1_marker):
            print('player 1 won')
            break
        if full_board_check(board):
            break
        #player 2 input
        print('player 2')
        player2_pos = player_choice(board)
        place_marker(board, player2_marker, player2_pos)
        if win_check(board, player2_marker):
            print('player 2 won')
            break
        if full_board_check(board):
            break
    if not replay():
        break

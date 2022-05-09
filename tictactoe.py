"""
Tic Tac Toe Player
"""

import math
import copy
import sys
sys.setrecursionlimit(10000)
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcount=0
    ocount=0
    for row in board:
        for column in row:
            if column==X:
                xcount+=1
            elif column==O:
                ocount+=1
           
    if xcount>ocount:
        #print("ocount is"+str(ocount))
        ##rint("O")
        return O
    else:
        #print("x")
        return X
   


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionslist=set()
    for x,x_axis in enumerate(board):
        for y, y_axis in enumerate(x_axis):
            if y_axis == EMPTY:
                actionslist.add((y, x))

    print(actionslist)
    return actionslist
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    if action in actions(board):
         (i, j) = action
         current_player = player(board)
         new_board = copy.deepcopy(board)
         new_board[i][j] = current_player
         return new_board
    else:
        raise Exception


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # Check horizontal lines
     if (board[i][0] == board[i][1] == board[i][2]) and (board[i][0]==X or board[i][0]==O):
            return board[i][0]
        # check vertical lines
     if (board[0][i] == board[1][i] == board[2][i]) and (board[0][i]==X or board[0][i]==O):
            return board[0][i]
    if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]) and (board[1][1]==X or board[1][1]==O):
        return board[1][1]

    return None

    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board)==X or winner(board)==O) or(EMPTY not in board[0] and EMPTY not in board[1] and EMPTY not in board[2]):
        return True
    else:
        return False
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0
    #raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board)==True:
        return None
    for action in actions(board):
        if actions(board)!=None:
            min_val(result(board,action),action)
        else:
            if utility(result(action))==-1:
                return action

def min_val(board,action):
    max_val=1
    if actions(board)!=None:
        if utility(result(board,action))<max_val:
            boardd=result(board,action)
            minimax(boardd)
    else:
        return action
"""
Tic Tac Toe Player
"""

import math
import copy


X = "X"
O = "O"
EMPTY = None

board = [[X, O, X],
        [O, EMPTY, X],
        [EMPTY, EMPTY, O]]



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
    x_count = 0
    o_count = 0

    output = []

    #transform a 3d list to a simple list
    for temp in board:
        for elem in temp:
            output.append(elem)
   
    
    for i in range(len(output)):
        if output[i] == 'X':
            x_count += 1
        elif output[i] == 'O':
            o_count += 1
    """
    print("x -> " + str(x_count))
    print("o -> " + str(o_count))
    """
    if x_count == o_count:
        return 'X'
    else:
        return 'O'

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    i = -1
    j = -1
    total = 0
    cood = set()


    for x in board:

        i+=1
        j=-1
        for z in x:

            j+=1

            if z == None:
                total+=1
                cood.add((i,j))
    


    return cood
            
    

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board): raise ValueError

    
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """


    column0 = []
    column1 = []
    column2 = []

    diag0 = [board[0][0], board[1][1], board[2][2]]
    diag1 = [board[0][2], board[1][1], board[2][0]]
    


    for row in board:
        column0.append(row[0])
        
    for row in board:
        column1.append(row[1])

    for row in board:
        column2.append(row[2])




    if board[0][0]== X and board[0][1]== X and board[0][2] == X:
        return 'X'
    elif board[0][0]== O and board[0][1]== O and board[0][2] == O:
        return 'O'
    
    elif board[1][0]== X and board[1][1]== X and board[1][2] == X:
        return 'X'
    elif board[1][0]== O and board[1][1]== O and board[1][2] == O:
        return 'O'

    elif board[2][0]== X and board[2][1]== X and board[2][2] == X:
        return 'X'
    elif board[2][0]== O and board[2][1]== O and board[2][2] == O:
        return 'O'

    elif column0[0]== X and column0[1]== X and column0[2] == X:
        return 'X'
    elif column0[0]== O and column0[1]== O and column0[2] == O:
        return 'O'
    elif column1[0]== X and column1[1]== X and column1[2] == X:
        return 'X'
    elif column1[0]== O and column1[1]== O and column1[2] == O:
        return 'O'
    elif column2[0]== X and column2[1]== X and column2[2] == X:
        return 'X'
    elif column2[0]== O and column2[1]== O and column2[2] == O:
        return 'O'

    elif diag0[0]== O and diag0[1]== O and diag0[2] ==O:
        return 'O'
    elif diag0[0]== X and diag0[1]== X and diag0[2] ==X:
        return 'X'
    elif diag1[0]== O and diag1[1]== O and diag1[2] ==O:
        return 'O'
    elif diag1[0]== X and diag1[1]== X and diag1[2] ==X:
        return 'X'
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    values = []

    if winner(board) == 'X' or winner(board) == 'O': return True
    
    for x in board:
        for data in x:
            values.append(data)

    if None in values: return False
    else: return True 


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == 'X': return 1
        elif winner(board) == 'O': return -1
        else: return 0


def minimax(board):

    #Returns the optimal action for the current player on the board.

    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move

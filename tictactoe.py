"""
Tic Tac Toe Player
"""

import math

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
    #flat board
    flat_board = [i for x in board for i in x]
    
    if flat_board.count(O) >= flat_board.count(X):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = []
    i = 0
    j = 0

    for i in (range(len(board))):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                action.append([i,j])
            j += 1
        i += 1
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action [1]
    
    if board[i][j] != EMPTY:
        raise Exception("Movimento inválido")
        
    new_board = copy(board)
    new_board[i][j] = player(board)
    return new_board

def copy(board):
    new_board =[]

    i = 0
    j = 0

    for i in (range(len(board))):
        linha = []
        for j in range(len(board[i])):
            linha.append(board[i][j])
            j += 1
        new_board.append(linha)
        i += 1
    
    return  new_board

def winner(board):
    #Verify lines
    for i in (range(len(board))):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]

    #verify column        
    for j in (range(len(board))):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j] and board[0][j] != EMPTY:
            return board[0][j]

    #Verify Diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #check if winner
    if winner(board) != None:
        return True
    #check if tie   
    return isTie(board)


def isTie(board):
    
    i = 0
    j = 0
    n = 0


    for i in (range(len(board))):
        for j in range(len(board[i])):
            if board[i][j] != None:
                n += 1
            j += 1
        i += 1

    if n == 9 :
        return True
    else:
        return False
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == X:
        return 1
    
    if winner(board) == O:
        return -1
    
    if isTie(board):
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    valor = None    

    if player(board) == X:
        for action in actions(board):
            if winner(result(board,action)):
                return action
            if valor == None:
                valor = maxValue(result(board,action))
                acao = action
                
            proxValor = maxValue(result(board,action))
            if proxValor > valor:
                valor = proxValor
                acao = action
        return acao


    if player(board) == O:
        for action in actions(board):
            if winner(result(board,action)):
                return action
            if valor == None:
                valor = minValue(result(board,action))
                acao = action
                
            proxValor = minValue(result(board,action))
            if proxValor < valor:
                valor = proxValor
                acao = action  
        return acao

def maxValue(board):
    v = -float('inf')
    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = max(v, minValue(result(board, action)))

    return v

def minValue(board):
    v = float('inf')
    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = min(v, maxValue(result(board, action)))

    return v
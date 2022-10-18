import random

board = []

for y in range(4):
    board.append([])
    for x in range(4):
        board[y].append('.')

#board[random.randint(0, 3)][random.randint(0, 3)] = 'T'

def displayBoard(board):
    for y in range(4):
        for x in range(4):
            print(board[x][y], end='')
        print()

def getPlayerMove(board, sym):
    try:
        move = input('Enter your move: ').split(' ')
        move = list(map(lambda x: int(x), move))
        x, y = move
        
        if x not in range(4) or y not in range(4):
            return getPlayerMove(board, sym)
        elif board[x][y] in ['X', 'O', 'T']:
            return getPlayerMove(board, sym)
    except:
        print('Invalid move.')
        return getPlayerMove(board, sym)
    else:
        return [sym, move]

x = getPlayerMove(board, 'X')
print(x)
            



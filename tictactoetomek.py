import random

def makeBoard():
    bo = []
    for y in range(4):
        bo.append([])
        for x in range(4):
            bo[y].append('.')
    bo[random.randint(0, 3)][random.randint(0, 3)] = 'T'
    return bo

def displayBoard(bo):
    print('  0 1 2 3')
    for y in range(4):
        print(y, end=' ')
        for x in range(4):
            print(bo[x][y], end=' ')
        print()

def getPlayerMove(bo, turn):
    try:
        move = input(f'Player {turn} enter your move: ').strip().split(' ')
        move = list(map(lambda x: int(x), move))
        x, y = move
        
        if x not in range(4) or y not in range(4) or bo[x][y] != '.':
            print('Space taken.')
            return getPlayerMove(bo, turn)
    except:
        print('Invalid move.')
        return getPlayerMove(bo, turn)
    else:
        return move

def checkWin(bo, sym):
    chars = [sym, 'T']
    return ((bo[0][0] in chars and bo[1][0] in chars and bo[2][0] in chars and bo[3][0] in chars) or
    (bo[0][1] in chars and bo[1][1] in chars and bo[2][1] in chars and bo[3][1] in chars) or
    (bo[0][2] in chars and bo[1][2] in chars and bo[2][2] in chars and bo[3][2] in chars) or
    (bo[0][3] in chars and bo[1][3] in chars and bo[2][3] in chars and bo[3][3] in chars) or

    (bo[0][0] in chars and bo[0][1] in chars and bo[0][2] in chars and bo[0][3] in chars) or
    (bo[1][0] in chars and bo[1][1] in chars and bo[1][2] in chars and bo[1][3] in chars) or
    (bo[2][0] in chars and bo[2][1] in chars and bo[2][2] in chars and bo[2][3] in chars) or
    (bo[3][0] in chars and bo[3][1] in chars and bo[3][2] in chars and bo[3][3] in chars) or

    (bo[0][0] in chars and bo[1][1] in chars and bo[2][2] in chars and bo[3][3] in chars) or
    (bo[3][0] in chars and bo[2][1] in chars and bo[1][2] in chars and bo[0][3] in chars)
    )

def checkDraw(bo):
    for y in range(4):
        for x in range(4):
            if bo[x][y] == '.':
                return False
    return True

def main():
    board = makeBoard()
    turnx = True
    displayBoard(board)
    print()

    while True:
        if turnx:
            turn = 'X'
        else:
            turn = 'O'

        print()
        x, y = getPlayerMove(board, turn)
        board[x][y] = turn
        print()
        displayBoard(board)

        if checkWin(board, turn):
            print(f'{turn} won the game!')
            break
        elif checkDraw(board):
            print('The game is a draw!')
            break
        turnx = not turnx
    
main()

theBoard = {'top_L': ' ', 'top_M': ' ', 'top_R': ' ',
            'mid_L': ' ', 'mid_M': ' ', 'mid_R': ' ',
            'low_L': ' ', 'low_M': ' ', 'low_R': ' '
            }
def pboard(board):
    print(board['top_L']+'|'+board['top_M']+'|'+board['top_R'])
    print('-+-+-')
    print(board['mid_L'] + '|' + board['mid_M'] + '|' + board['mid_R'])
    print('-+-+-')
    print(board['low_L'] + '|' + board['low_M'] + '|' + board['low_R'])

turn = 'X'
for i in range(len(theBoard)):
    print("Turn for "+turn)
    move = input("The area where u want to put\n")
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    print(pboard(theBoard))


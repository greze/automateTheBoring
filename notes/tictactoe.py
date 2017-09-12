# a terminal based tic-tac-toe game.
# It only works for two players, and doesn't do anything when you win.
# Yeah. 

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
  'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
  'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
  
def printBoard(board):
  print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
  print('-+-+-')
  print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
  print('-+-+-')
  print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)

turn = 'x'
for i in range(9):
  printBoard(theBoard)
  print('Turn for ' + turn + '. Where you gonna move, girl?')
  print("Legal moves are 'top-L', 'top-M', 'top-R', 'mid-...', 'low...', etc.")
  print("Yes, you have to type a single quote around everything. This is coding practice, not a real game.")
  move = str(input())
  theBoard[move] = turn
  if turn == 'x':
    turn = 'o'
  else:
    turn = 'x'
print(theBoard)

def IsMoveLegal(fromX, toX, fromY, toY):

    if fromX == toX and fromY == toY:
      return False

    if board[fromY][fromX] == 'p' or board[fromY][fromX] == 'P':
      yRange = toY - fromY
      xRange = toX - fromX
      if currentWhite == True and xRange == 0 and yRange == -1:
        if board[toY][toX] == '.' and fromX == toX:
          return True
      elif currentWhite == False and xRange == 0 and yRange == 1:
        if board[toY][toX] == '.' and fromX == toX:
          return True
      elif (yRange == 2 or yRange == -2) and xRange == 0:
        if board[toY][toX] == '.' and fromY == 1 and toY == fromY + 2:
          if IsClearPath(fromX, toX, fromY, toY):
            return True
        elif board[toY][toX] == '.' and fromY == 6 and toY == fromY - 2:
          if IsClearPath(fromX, toX, fromY, toY):
            return True
      elif (xRange == 1 or xRange == -1) and (yRange == 1 or yRange == -1):
        if currentWhite == True:
          if board[toY][toX].islower():
            return True
        elif currentWhite == False:
          if board[toY][toX].isupper():
            return True


    elif board[fromY][fromX] == "r" or board[fromY][fromX] == "R":
      if fromX == toX or fromY == toY:
        if board[toY][toX] == '.' or ((currentWhite == False and board[toY][toX].isupper()) or (currentWhite == True and board[toY][toX].islower())):
          if IsClearPath(fromX, toX, fromY, toY):
            return True

    elif board[fromY][fromX] == 'b' or board[fromY][fromX] == 'B':
      if fromX-fromY == toX-toY or fromX+fromY == toX+toY:
        if board[toY][toX] == '.' or ((currentWhite == False and board[toY][toX].isupper()) or (currentWhite == True and board[toY][toX].islower())):
          if IsClearPath(fromX, toX, fromY, toY):
            return True

    elif board[fromY][fromX] == 'q' or board[fromY][fromX] == 'Q':
      #rook logic
      if fromX == toX or fromY == toY:
        if board[toY][toX] == '.' or ((currentWhite == False and board[toY][toX].isupper()) or (currentWhite == True and board[toY][toX].islower())):
          if IsClearPath(fromX, toX, fromY, toY):
            return True
      #bishop logic
      if fromX-fromY == toX-toY or fromX+fromY == toX+toY:
        if board[toY][toX] == '.' or ((currentWhite == False and board[toY][toX].isupper()) or (currentWhite == True and board[toY][toX].islower())):
          if IsClearPath(fromX, toX, fromY, toY):
            return True

    elif board[fromY][fromX] == 't' or board[fromY][fromX] == 'T':
      colDif = toX - fromX
      rowDif = toY - fromY
      if board[toY][toX] == '.' or ((currentWhite == True and board[toY][toX].islower()) or (currentWhite == False and board[toY][toX].isupper())):
        if (colDif == 1 and rowDif == -2) or (colDif == 2 and rowDif == -1) or (colDif == 2 and rowDif == 1) or (colDif == 1 and rowDif == 2):
          return True
        elif (colDif == -1 and rowDif == -2) or (colDif == -2 and rowDif == -1) or (colDif == -2 and rowDif == 1) or (colDif == -1 and rowDif == 2):
          return True

    elif board[fromY][fromX] == 'k' or board[fromY][fromX] == 'K':
      colDif = toX - fromX
      rowDif = toY - fromY
      if board[toY][toX] == '.' or ((currentWhite == False and board[toY][toX].isupper()) or (currentWhite == True and board[toY][toX].islower())):
        if (abs(colDif) == 1 and abs(rowDif) == 0) or (abs(colDif) == 0 and abs(rowDif) == 1) or (abs(colDif) == 1 and abs(rowDif) == 1):
          return True

    return False



def GetListOfLegalMoves(fromX, fromY):
  legalMoves = []
  
  for count,y in enumerate(board):
    for count2,x in enumerate(y):
      toX = count2
      toY = count
      result = IsMoveLegal(fromX, toX, fromY, toY)
      if result:
        result2 = DoesMovePutPlayerInCheck(fromX, toX, fromY, toY)
        if result2 == False:
          legalMoves.append([count,count2])
  return legalMoves

  

def GetPiecesWithLegalMoves():
  
  pieces = []
  temp = []
  for count, y in enumerate(board):
    for count2, x in enumerate(y):
      if currentWhite == True and board[count][count2].isupper():
        temp = GetListOfLegalMoves(count2, count)
        if temp:
          pieces.append([count, count2])
      elif currentWhite == False and board[count][count2].islower():
        temp = GetListOfLegalMoves(count2, count)
        if temp:
          pieces.append([count, count2])
  return pieces


def IsCheckmate():
  
  legalMoves = GetPiecesWithLegalMoves()
  if legalMoves:
    return True
  else:
    return False



def IsInCheck():
  
  kingInY = 0
  kingInX = 0
  for count, y in enumerate(board):
    for count2, x in enumerate(y):
      if currentWhite == False and board[count][count2] == 'k':
        kingInY = count
        kingInX = count2
      elif currentWhite == True and board[count][count2] == 'K':
        kingInY = count
        kingInX = count2

  for count,y in enumerate(board):
    for count2,x in enumerate(y):
      if currentWhite == True and (board[count][count2] != '.' and board[count][count2].islower()):
        value = IsMoveLegal(count2, kingInX, count, kingInY)
        if value:
          return True
      elif currentWhite == False and (board[count][count2] != '.' and board[count][count2].isupper()):
        value = IsMoveLegal(count2, kingInX, count, kingInY)
        if value:
          return True
  return False


def IsClearPath(fromX, toX, fromY, toY):
  
  yRange = fromY - toY
  xRange = fromX - toX
  if xRange in range(-1,1) and yRange in range(-1,1):
    return True
  else:
    if yRange > 0 and xRange == 0:
      newSqX = fromX
      newSqY = fromY - 1
    elif yRange < 0 and xRange == 0:
      newSqX = fromX
      newSqY = fromY + 1
    elif xRange < 0 and yRange == 0:
      newSqX = fromX + 1
      newSqY = fromY
    elif xRange > 0 and yRange == 0:
      newSqX = fromX - 1
      newSqY = fromY
    elif yRange < 0 and xRange < 0:
      newSqX = fromX + 1
      newSqY = fromY + 1
    elif yRange < 0 and xRange > 0:
      newSqX = fromX - 1
      newSqY = fromY + 1
    elif yRange > 0 and xRange < 0:
      newSqX = fromX + 1
      newSqY = fromY - 1
    elif yRange > 0 and xRange > 0:
      newSqX = fromX - 1
      newSqY = fromY - 1
  
  if board[newSqY][newSqX] != '.':
    return False
  else:
    return IsClearPath(newSqX, toX, newSqY, toY)



def DoesMovePutPlayerInCheck(fromX, toX, fromY, toY):
  global board
  tempBoard = copy.deepcopy(board)
  MovePiece(fromX, toX, fromY, toY)
  value = IsInCheck()
  board = copy.deepcopy(tempBoard)
  return value



def GetRandomMove():
    # pick a random piece and a random legal move for that piece
    pieces = GetPiecesWithLegalMoves()
    #print(pieces)
    piece = random.choice(pieces)
    #print(piece)
    moves = GetListOfLegalMoves(piece[1], piece[0])
    #print(moves)
    move = random.choice(moves)
    #print(move)
    value = [piece, move]
    return value




def evl():
  whiteScore = 0
  blackScore = 0
  for count, y in enumerate(board):
    for count2, x in enumerate(y):
      if board[count][count2].isupper() and board[count][count2] == 'P':
          whiteScore += 1
      elif board[count][count2].isupper() and board[count][count2] == 'R':
          whiteScore += 5
      elif board[count][count2].isupper() and board[count][count2] == 'T':
          whiteScore += 3
      elif board[count][count2].isupper() and board[count][count2] == 'B':
          whiteScore += 3
      elif board[count][count2].isupper() and board[count][count2] == 'Q':
          whiteScore += 9
      elif board[count][count2].islower() and board[count][count2] == 'p':
          blackScore += 1
      elif board[count][count2].islower() and board[count][count2] == 'r':
          blackScore += 5
      elif board[count][count2].islower() and board[count][count2] == 't':
          blackScore += 3
      elif board[count][count2].islower() and board[count][count2] == 'b':
          blackScore += 3
      elif board[count][count2].islower() and board[count][count2] == 'q':
          blackScore += 9
  if currentWhite == True:
    return whiteScore
  elif currentWhite == False:
    return blackScore


def GetMinMaxMove():
  global board
  global currentWhite
  score = 0
  bestEnemyMove = 999
  worstEnemyMove = 0
  repeats = 0
  pieces = GetPiecesWithLegalMoves()
  for piece in pieces:
    moves = GetListOfLegalMoves(piece[1], piece[0])
    for move in moves:
      tempBoard = copy.deepcopy(board)
      board = MovePiece(piece[1], move[1], piece[0], move[0])
      currentWhite = not currentWhite
      enemyPieces = GetPiecesWithLegalMoves()
      for enemyPiece in enemyPieces:
        enemyMoves = GetListOfLegalMoves(enemyPiece[1], enemyPiece[0])
        for enemyMove in enemyMoves:
          tempBoard2 = copy.deepcopy(board)
          board = MovePiece(enemyPiece[1], enemyMove[1], enemyPiece[0], enemyMove[0])
          res = evl()
          if res > score:
            score = res
            bestMove = [piece, move]
          if res < bestEnemyMove:
            bestEnemyMove = res
            enMove = enemyMove
            repeats = 0
          if bestEnemyMove == res:
            repeats += 1
          board = tempBoard2
        
      board = tempBoard
      currentWhite = not currentWhite
  return bestMove



board = ChessBoardSetup()
turns = 0
N = 75

while turns < N:

  DrawBoard(board)

  if currentWhite == False:
    move = GetRandomMove()
  elif currentWhite == True:
    move = GetMinMaxMove()
  print(move)
  board = MovePiece(move[0][1], move[1][1], move[0][0], move[1][0])
  if(board[move[1][0]][move[1][1]]) == '.':
    turns += 1
  else:
    turns = 0
  
  DrawBoard(board)
  currentWhite = not currentWhite
  time.sleep(.5)


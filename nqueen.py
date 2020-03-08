import random
import copy
from colorama import init
from termcolor import colored
init()
def heuristicCost(board):
  cost = 0
  for i in range(len(board)):
    for j in range(i+1, len(board)):  # check only the forward  cols i.e. i=0 1-3,2-3,3-3
      if board[i] == board[j]:  #same row queens
        cost+=1
      diagonal=j-i
      if board[i]==(board[j]-diagonal) or board[i]==(board[j]+diagonal):
        cost += 1
  return cost

#main
n=5 # n queen problem
# board=[random.randint(0,n-1) for i in range(n)]
# board=[3,0,1,0]
bestCost=float('inf')
for iterations in range(20):
  board=[random.randint(0,n-1) for i in range(n)]
  # board=[3,2,1,2]
  while(1):
    bestMove=(-1,-1)
    needToChange=False
    bestCost=heuristicCost(board)  # consider initial arrangement as the one with best/min heuristic cost
    if bestCost==0:
      break
    tempBoard=[]
    # print(board,end=' '); print(bestCost)  # initial arrangement and it's cost
    for i in range(n):    # column
      tempBoard=copy.deepcopy(board) # start with original board arrangement
      print(tempBoard,end=' '); print(heuristicCost(tempBoard),end=' ')
      for j in range(n-1):  
        tempBoard[i]=(tempBoard[i]+1)%n # changing row number
        currentCost=heuristicCost(tempBoard)
        print(tempBoard,end=' '); print(currentCost,end=' '); print(bestCost,end=' ')
        if currentCost < bestCost:
          bestCost=heuristicCost(tempBoard)
          bestMove=(i,tempBoard[i])
          needToChange=True
        # print("col "+str(i)+" row "+str(j)+" current Cost "+str(currentCost)+" best Cost "+str(bestCost))
        # print(colored("replaced "+str(i)+" with "+str(j)))
      print()
      # print(str(tempBoard) + str(bestCost))
    if needToChange:
      print("Best Move is "+str(bestMove))
      tempBoard=copy.deepcopy(board)
      tempBoard[bestMove[0]]=bestMove[1]
      board=copy.deepcopy(tempBoard)
      print(colored(str(tempBoard) + str(bestCost), "green"))
    else:
      print("No more improvement possible\n")
      break
  if bestCost==0:
    break
print(colored(str(tempBoard) + str(bestCost), "red"))
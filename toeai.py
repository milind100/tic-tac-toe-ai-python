import random

def drawBoard(board):
    print("   |   |   ")
    print(" "+board[1] + " | "+board[2]+" | "+board[3])
    print("   |   |   ")
    print("===========")
    print("   |   |   ")
    print(" "+board[4] + " | "+board[5]+" | "+board[6])
    print("   |   |   ")
    print("===========")
    print("   |   |   ")
    print(" "+board[7] + " | "+board[8]+" | "+board[9])
    print("   |   |   ")

def Iswinner(b,l):
    return (
        (b[1]==l and b[2]==l and b[3]==l)  or
        (b[4]==l and b[5]==l and b[6]==l)  or
        (b[7]==l and b[8]==l and b[9]==l)  or

        (b[1]==l and b[4]==l and b[7]==l)  or
        (b[2]==l and b[5]==l and b[8]==l)  or
        (b[3]==l and b[6]==l and b[9]==l)  or

        (b[1]==l and b[5]==l and b[9]==l)  or
        (b[3]==l and b[5]==l and b[7]==l)  
    )

def cheackValidinput(turn):
    if turn.strip().isdigit():
        turn = int(turn)
        if int(turn) > 0 and int(turn) < 10 :
            return True
        
def isSpacefree(board,turn):
    if board[turn]==' ' :
        return True

def isBoardfull(board):
    cheack = 0
    for i in range(1,10):
        if  board[i]== " ":
            cheack=cheack+1

    if cheack > 0:
        return False        
    else: return True

def availableSpace(board):
    ava = []
    for i in range(1,10):
        if board[i]== " ":
            ava.append(i)
    return ava


def computerMove(board):
    turn = 0
    possibleMoves = availableSpace(board)
    for i in possibleMoves:
        boardcopy = board[:]
        boardcopy[i] = "O"
        
        if  Iswinner(boardcopy,"O"):
            turn = i
            return turn

    cornersOpen = []
    edgesOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen)>0:
        turn  = random.choice(cornersOpen)
        return turn

    if 5 in possibleMoves:
        turn = 5
        return 5

    
    for i in possibleMoves:
        if i in [2,4,6,8]:edgesOpen.append(i)

    if len(edgesOpen)>0:
        turn = random.choice(edgesOpen)
        return turn





theBoard =[" "]*10

quit = False 
while quit==False:
    
    print("Welcome To the game")
    drawBoard(theBoard)
    letter ="O"
    while letter == "O":
        turn = input("Its Os Turn please select input from 1 to 9 and q to quit:")
        if turn == "q":
            print("Thanks for playing")
            quit = True
            break
        if not cheackValidinput(turn):
            
            print("Please Enter number beetween 1 to 9 only") 
            continue
        
        turn = int(turn)
        if isSpacefree(theBoard,turn):
            theBoard[turn]=letter
            drawBoard(theBoard)
            
            if Iswinner(theBoard,letter):
                print("player 1 is winner")
                quit = True
                break

            elif isBoardfull(theBoard):
                print("The Game is tie")
                quit = True
                break
            letter = "X"

    while letter == "X":


        turn = computerMove(theBoard)
        print(turn)

        theBoard[turn]=letter
        drawBoard(theBoard)
        if Iswinner(theBoard,letter):
            print("player 2 is winner")
            quit = True
            break

        elif isBoardfull(theBoard):
            print("The Game is tie")
            quit = True
            break

        letter = "O"


        


    

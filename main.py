# tictactoe.py v1.0.0
# Programmer: Emmet Spencer
# Block: 1 HNRS PYTHON
# Date: 12/5/19
# Description: Play Tic Tac Toe!

#****************************************#
#           IMPORT STATEMENTS            #
#****************************************#

import random

#****************************************#
#        FUNCTION DEFINITIONS            #
#****************************************#

def Board():
    strBoard = f"""
    {strBoardSlot[0]}|{strBoardSlot[1]}|{strBoardSlot[2]}
    -----------------
    {strBoardSlot[3]}|{strBoardSlot[4]}|{strBoardSlot[5]}
    -----------------
    {strBoardSlot[6]}|{strBoardSlot[7]}|{strBoardSlot[8]}
    """
    return strBoard


def CopyBoard():
    for i in range(9):
        strTempBoardSlot[i] = strBoardSlot[i]
    print strTempBoardSlot
def strTempBoard(strTempBoardSlot):
    strTempBoardGraphic = f"""
    {strTempBoardSlot[0]}|{strTempBoardSlot[1]}|{strTempBoardSlot[2]}
    -----------------
    {strTempBoardSlot[3]}|{strTempBoardSlot[4]}|{strTempBoardSlot[5]}
    -----------------
    {strTempBoardSlot[6]}|{strTempBoardSlot[7]}|{strTempBoardSlot[8]}
    """
    return strTempBoardGraphic

def Go_First_and_Character():
    while strNotCompleted=="Yes":
        strGoFirst = input("Do you want to go first? [Yes/No]: ")
        strCharacter = input("What character do you want to be? [x/o]: ")
        if strGoFirst.title() == "Yes" or strGoFirst.title() == "No" and strCharacter.title() == "x" or strCharacter.title() == "o":
            lstFirstCharacter = [strGoFirst, strCharacter]
            return lstFirstCharacter
            strNotCompleted == "No"

    if strGoFirst.title() == "Yes":
        strPlayer1[0] = "First"
    if strGoFirst.title() == "No":
        strPlayer1[0] = "Second"
    if strCharacter.lower() == "x":
        strPlayer1[1] = "x"
    if strCharacter.lower() == "o":
        strPlayer1[1] = "o"

def AI(strBoard, strBoardSlot):
    strTempBoardSlot=["     ","     ","     ","     ","     ","     ","     ","     ","     "]
    AITurn = True
    if strPlayer1[1] == "o":
        strAIChar = "x"
    if strPlayer1[1] == "x":
        strAIChar = "o"
    print(strAIChar)
    while AITurn:
        for i in range(9):
            for i in range(9):
                strTempBoardSlot[i] = strBoardSlot[i]
            strTempBoardGrapic = strTempBoard(strTempBoardSlot)
            print(strTempBoardGrapic)
            if strBoardSlot[i] == "     ":
                strTempBoardSlot[i] = "  " + strAIChar + "  "
                lstTempWinner = TempCheckWinner(strBoard, strBoardSlot, strAIChar)
                print(type(lstTempWinner))
                print(lstTempWinner)
                if lstTempWinner[1] == True:
                    print("[AI] > Taken turn.")
                    strBoardSlot[i] = f"  {strAIChar}  "
                    print(strBoard)
                    AITurn = False
                if lstTempWinner[1] != True:
                    print("[AI] > No found win.")
                    continue
                else:
                    print("[AI] > Error.")
                    continue
        AITurn = False









def CheckWinner(strBoard, strBoardSlot, strAIChar):
# Check if User won
    lstPlayerWinReturn = ["",""]
    #print(strPlayer1[1])
    if strBoardSlot[0] == f"  {strPlayer1[1]}  " and strBoardSlot[1] == f"  {strPlayer1[1]}  " and strBoardSlot[2] == f"  {strPlayer1[1]}  ":
        print("You won by getting the top row!")
        lstPlayerWinReturn[0] = True
    if strBoardSlot[3] == f"  {strPlayer1[1]}  " and strBoardSlot[4] == f"  {strPlayer1[1]}  " and strBoardSlot[5] == f"  {strPlayer1[1]}  ":
        print("You won by getting the middle row!")
        lstPlayerWinReturn[0] = True
    if strBoardSlot[6] == f"  {strPlayer1[1]}  " and strBoardSlot[7] == f"  {strPlayer1[1]}  " and strBoardSlot[8] == f"  {strPlayer1[1]}  ":
        print("You won by getting the bottom row!")
        lstPlayerWinReturn[0] = True
    if strBoardSlot[0] == f"  {strPlayer1[1]}  " and strBoardSlot[3] == f"  {strPlayer1[1]}  " and strBoardSlot[6] == f"  {strPlayer1[1]}  ":
        print("You won by getting the first row down!")
        lstPlayerWinReturn[0] = True
    if strBoardSlot[1] == f"  {strPlayer1[1]}  " and strBoardSlot[4] == f"  {strPlayer1[1]}  " and strBoardSlot[7] == f"  {strPlayer1[1]}  ":
        print("You won by getting the middle row down!")
        lstPlayerWinReturn[0] = True
    if strBoardSlot[2] == f"  {strPlayer1[1]}  " and strBoardSlot[5] == f"  {strPlayer1[1]}  " and strBoardSlot[8] == f"  {strPlayer1[1]}  ":
        print("You won by getting the last row down!")
        lstPlayerWinReturn[0] = True
    if strBoardSlot[0] == f"  {strPlayer1[1]}  " and strBoardSlot[4] == f"  {strPlayer1[1]}  " and strBoardSlot[8] == f"  {strPlayer1[1]}  ":
        print("You won by getting a diagonal!")
        lstPlayerWinReturn[0] = True
    if strBoardSlot[2] == f"  {strPlayer1[1]}  " and strBoardSlot[4] == f"  {strPlayer1[1]}  " and strBoardSlot[6] == f"  {strPlayer1[1]}  ":
        print("You won by getting a diagonal!")
        lstPlayerWinReturn[0] = True
    #print(lstPlayerWinReturn)
# Check if AI won
    if strPlayer1[1] == "x":
        strAIChar = "o"
    if strPlayer1[1] == "o":
        strAIChat = "x"
    if strBoardSlot[0] == f"  {strAIChar}  " and strBoardSlot[1] == f"  {strAIChar}  " and strBoardSlot[2] == f"  {strAIChar}  ":
        print("The AI won by getting the top row!")
        lstPlayerWinReturn[1] = True
    if strBoardSlot[3] == f"  {strAIChar}  " and strBoardSlot[4] == f"  {strAIChar}  " and strBoardSlot[5] == f"  {strAIChar}  ":
        print("The AI won by getting the middle row!")
        lstPlayerWinReturn[1] = True
    if strBoardSlot[6] == f"  {strAIChar}  " and strBoardSlot[7] == f"  {strAIChar}  " and strBoardSlot[8] == f"  {strAIChar}  ":
        print("The AI won by getting the bottom row!")
        lstPlayerWinReturn[1] = True
    if strBoardSlot[0] == f"  {strAIChar}  " and strBoardSlot[3] == f"  {strAIChar}  " and strBoardSlot[6] == f"  {strAIChar}  ":
        print("The AI won by getting the first row down!")
        lstPlayerWinReturn[1] = True
    if strBoardSlot[1] == f"  {strAIChar}  " and strBoardSlot[4] == f"  {strAIChar}  " and strBoardSlot[7] == f"  {strAIChar}  ":
        print("The AI won by getting the middle row down!")
        lstPlayerWinReturn[1] = True
    if strBoardSlot[2] == f"  {strAIChar}  " and strBoardSlot[5] == f"  {strAIChar}  " and strBoardSlot[8] == f"  {strAIChar}  ":
        print("The AI won by getting the last row down!")
        lstPlayerWinReturn[1] = True
    if strBoardSlot[0] == f"  {strAIChar}  " and strBoardSlot[4] == f"  {strAIChar}  " and strBoardSlot[8] == f"  {strAIChar}  ":
        print("The AI won by getting a diagonal!")
        lstPlayerWinReturn[1] = True
    if strBoardSlot[2] == f"  {strAIChar}  " and strBoardSlot[4] == f"  {strAIChar}  " and strBoardSlot[6] == f"  {strAIChar}  ":
        print("The AI won by getting a diagonal!")
        lstPlayerWinReturn[1] = True
    #print(lstPlayerWinReturn)
    return lstPlayerWinReturn

def TempCheckWinner(strBoard, strBoardSlot, strAIChar):
# Check if User won
    lstTempPlayerWinReturn = ["",""]
    lstPlayerWinReturn = ["",""]
    #print(strPlayer1[1])
    #print(lstPlayerWinReturn)
# Check if AI won
    if strPlayer1[1] == "x":
        strAIChar = "o"
    if strPlayer1[1] == "o":
        strAIChat = "x"
    if strBoardSlot[0] == f"  {strAIChar}  " and strBoardSlot[1] == f"  {strAIChar}  " and strBoardSlot[2] == f"  {strAIChar}  ":
        lstPlayerWinReturn[1] = True
    if strBoardSlot[3] == f"  {strAIChar}  " and strBoardSlot[4] == f"  {strAIChar}  " and strBoardSlot[5] == f"  {strAIChar}  ":
        lstPlayerWinReturn[1] = True
    if strBoardSlot[6] == f"  {strAIChar}  " and strBoardSlot[7] == f"  {strAIChar}  " and strBoardSlot[8] == f"  {strAIChar}  ":
        lstPlayerWinReturn[1] = True
    if strBoardSlot[0] == f"  {strAIChar}  " and strBoardSlot[3] == f"  {strAIChar}  " and strBoardSlot[6] == f"  {strAIChar}  ":
        lstPlayerWinReturn[1] = True
    if strBoardSlot[1] == f"  {strAIChar}  " and strBoardSlot[4] == f"  {strAIChar}  " and strBoardSlot[7] == f"  {strAIChar}  ":
        lstPlayerWinReturn[1] = True
    if strBoardSlot[2] == f"  {strAIChar}  " and strBoardSlot[5] == f"  {strAIChar}  " and strBoardSlot[8] == f"  {strAIChar}  ":
        lstPlayerWinReturn[1] = True
    if strBoardSlot[0] == f"  {strAIChar}  " and strBoardSlot[4] == f"  {strAIChar}  " and strBoardSlot[8] == f"  {strAIChar}  ":
        lstPlayerWinReturn[1] = True
    if strBoardSlot[2] == f"  {strAIChar}  " and strBoardSlot[4] == f"  {strAIChar}  " and strBoardSlot[6] == f"  {strAIChar}  ":
        lstPlayerWinReturn[1] = True
    #print(lstPlayerWinReturn)
    print(lstPlayerWinReturn)
    lstPlayerWinReturn = lstTempPlayerWinReturn
    return lstTempPlayerWinReturn


def TicTacToe(strPlayer1, strPlayerAI, intTurns, intUsedNumbers):
    strBoard = Board()
    if strPlayer1[0] == "First":
        print("You chose to go first!")
        Player1 = True
    if strPlayer1[0] == "Second":
        print("You wanted the AI to go first!")
        PlayerAI = False
    Playing = True
    lstPlayerWinReturn = ["",""]
    strAPlayerWon = ""
    print(strBoard)
    while Playing:
        while Player1:
            if lstPlayerWinReturn[0] == True:
                print("You have won the game!")
                PlayerAI = False
                Player1 = False
                Playing = False
                strAPlayerWon = "No"
            elif lstPlayerWinReturn[1] == True:
                print("The AI has won the game!")
                PlayerAI = False
                Player1 = False
                Playing = False
                strAPlayerWon = "No"
            if strAPlayerWon == "":
                LocationUsed = int(input("Which tile would you like to take? [1-9]: "))
                if strBoardSlot[LocationUsed-1] == "  x  " or strBoardSlot[LocationUsed-1] == "  o  ":
                    print("That board space is already being used!")
                if strBoardSlot[LocationUsed-1] == "     ":
                    strBoardSlot[LocationUsed-1] = f"  {str(strPlayer1[1])}  "
                    strBoard = Board()
                    print(strBoard)
                    PlayerAI = True
                    Player1 = False
                    intTurns = intTurns + 1
                    if intTurns == 9:
                        Player1 = False
                        PlayerAI = False
                    #print(intTurns)
                    if strPlayer1[1] == "o":
                        strAIChar = "x"
                    if strPlayer1[1] == "x":
                        strAIChar = "o"
                    #print("AI Character: " + strAIChar)
                    lstPlayerWinReturn = CheckWinner(strBoard, strBoardSlot, strAIChar)
        while PlayerAI:
            strAIChar = AI(strBoard, strBoardSlot)
            Player1 = True
            PlayerAI = False
            intTurns = intTurns + 1
            if intTurns == 9:
                Player1 = False
                PlayerAI = False
            #print(intTurns)
            #print(strAIChar)
            lstPlayerWinReturn = CheckWinner(strBoard, strBoardSlot, strAIChar)








#****************************************#
#         VARIABLE DECLARATION &         #
#           INITIALIZATION               #
#****************************************#
strPlayer1 = ["",""]
strPlayerAI = ["",""]
intTurns = 0
strAIChar = ""
strBoardSlot=["     ","     ","     ","     ","     ","     ","     ","     ","     "]
intUsedNumbers = []
blnPlaying = False
blnPlayer1Win = False
lstPlayerWinReturn= []
strNotCompleted = "Yes"
#****************************************#
#                EXECUTION               #
#****************************************#
strPlayGame = input("Do you want to play TicTacToe?: ")
if strPlayGame.title() == "Yes":
    print("Loading...")
    blnPlaying = True
elif strPlayGame.title() == "No":
    print(":(")

lstFirstCharacter = Go_First_and_Character()
print(lstFirstCharacter)
strGoFirst = lstFirstCharacter[0]
strCharacter = lstFirstCharacter[1]
if strGoFirst.title() == "Yes":
    strPlayer1[0] = "First"
elif strGoFirst.title() == "No":
    strPlayer1[0] = "Second"
if strCharacter.lower() == "x":
    strPlayer1[1] = "x"
elif strCharacter.lower() == "o":
    strPlayer1[1] = "o"
print(lstFirstCharacter)
strGoFirst = lstFirstCharacter[0]
strCharacter = lstFirstCharacter[1]

strBoard = TicTacToe(strPlayer1, strPlayerAI, intTurns, intUsedNumbers)




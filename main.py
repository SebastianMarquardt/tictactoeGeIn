#!/usr/bin/env python3

player1 = input("Name Spieler 1 (X): ")
player2 = input("Name Spieler 2 (O): ")

Feld = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
Won = ""

def checkTiles():
    if Feld[1] == "X" and Feld[2] == "X" and Feld[3] == "X":
        print(player1 + " hat gewonnen")
        return False
    elif Feld[1] == "O" and Feld[2] == "O" and Feld[3] == "O":
        print(player2 + " hat gewonnen")
        return False
    elif Feld[4] == "X" and Feld[5] == "X" and Feld[6] == "X":
        print(player1 + " hat gewonnen")
        return False
    elif Feld[4] == "O" and Feld[5] == "O" and Feld[6] == "O":
        print(player2 + " hat gewonnen")
        return False
    elif Feld[7] == "X" and Feld[8] == "X" and Feld[9] == "X":
        print(player1 + " hat gewonnen")
        return False
    elif Feld[7] == "O" and Feld[8] == "O" and Feld[9] == "O":
        print(player2 + " hat gewonnen")
        return False
    elif Feld[1] == "X" and Feld[4] == "X" and Feld[7] == "X":
        print(player1 + " hat gewonnen")
        return False
    elif Feld[1] == "O" and Feld[4] == "O" and Feld[7] == "O":
        print(player2 + " hat gewonnen")
        return False
    elif Feld[2] == "X" and Feld[5] == "X" and Feld[8] == "X":
        print(player1 + " hat gewonnen")
        return False
    elif Feld[2] == "O" and Feld[5] == "O" and Feld[8] == "O":
        print(player2 + " hat gewonnen")
        return False
    elif Feld[3] == "X" and Feld[6] == "X" and Feld[9] == "X":
        print(player1 + " hat gewonnen")
        return False
    elif Feld[3] == "O" and Feld[6] == "O" and Feld[9] == "O":
        print(player2 + " hat gewonnen")
        return False
    elif Feld[1] == "X" and Feld[5] == "X" and Feld[9] == "X":
        print(player1 + " hat gewonnen")
        return False
    elif Feld[1] == "O" and Feld[5] == "O" and Feld[9] == "O":
        print(player2 + " hat gewonnen")
        return False
    elif Feld[3] == "X" and Feld[5] == "X" and Feld[7] == "X":
        print(player1 + " hat gewonnen")
        return False
    elif Feld[3] == "O" and Feld[5] == "O" and Feld[7] == "O":
        print(player2 + " hat gewonnen")
        return False
    else:
        return True

def printTiles():
    print(" Col     A     B     C")
    print("Row   -------------------")
    print("   1  |  " + Feld[1] + "  |  " + Feld[2] + "  |  " + Feld[3] + "  |")
    print("      -------------------")
    print("   2  |  " + Feld[4] + "  |  " + Feld[5] + "  |  " + Feld[6] + "  |")
    print("      -------------------")
    print("   3  |  " + Feld[7] + "  |  " + Feld[8] + "  |  " + Feld[9] + "  |")
    print("      -------------------")

notWon = True
while notWon:
    
    printTiles()
    
    invalidInput1 = True
    while invalidInput1:
        firstInput = input(player1 + " bitte eingeben (z.B. A2): ")
        if firstInput != "A1" and firstInput != "A2" and firstInput != "A3" and firstInput != "B1" and firstInput != "B2" and firstInput != "B3" and firstInput != "C1" and firstInput != "C2" and firstInput != "C3":
            invalidInput1 = True
            print("nicht möglich")
        elif (firstInput == "A1" and Feld[1] == "X") or (firstInput == "B1" and Feld[2] == "X") or (firstInput == "C1" and Feld[3] == "X") or (firstInput == "A2" and Feld[4] == "X") or (firstInput == "B2" and Feld[5] == "X") or (firstInput == "C2" and Feld[6] == "X") or (firstInput == "A3" and Feld[7] == "X") or (firstInput == "B3" and Feld[8] == "X") or (firstInput == "C3" and Feld[9] == "X"):
            invalidInput1 = True
            print("nicht möglich")
        elif (firstInput == "A1" and Feld[1] == "O") or (firstInput == "B1" and Feld[2] == "O") or (firstInput == "C1" and Feld[3] == "O") or (firstInput == "A2" and Feld[4] == "O") or (firstInput == "B2" and Feld[5] == "O") or (firstInput == "C2" and Feld[6] == "O") or (firstInput == "A3" and Feld[7] == "O") or (firstInput == "B3" and Feld[8] == "O") or (firstInput == "C3" and Feld[9] == "O"):
            invalidInput1 = True
            print("nicht möglich")
        else: invalidInput1 = False

    if firstInput == "A1":
        Feld[1] = "X"
    if firstInput == "A2":
        Feld[4] = "X"
    if firstInput == "A3":
        Feld[7] = "X"
    if firstInput == "B1":
        Feld[2] = "X"
    if firstInput == "B2":
        Feld[5] = "X"
    if firstInput == "B3":
        Feld[8] = "X"
    if firstInput == "C1":
        Feld[3] = "X"
    if firstInput == "C2":
        Feld[6] = "X"
    if firstInput == "C3":
        Feld[9] = "X"

    printTiles()

    notWon = checkTiles()
    if notWon == False:
        break

    invalidInput2 = True
    while invalidInput2:
        secondInput = input(player2 + " bitte eingeben (z.B. A2): ")
        if secondInput != "A1" and secondInput != "A2" and secondInput != "A3" and secondInput != "B1" and secondInput != "B2" and secondInput != "B3" and secondInput != "C1" and secondInput != "C2" and secondInput != "C3":
            invalidInput2 = True
            print("nicht möglich")
        elif (secondInput == "A1" and Feld[1] == "X") or (secondInput == "B1" and Feld[2] == "X") or (secondInput == "C1" and Feld[3] == "X") or (secondInput == "A2" and Feld[4] == "X") or (secondInput == "B2" and Feld[5] == "X") or (secondInput == "C2" and Feld[6] == "X") or (secondInput == "A3" and Feld[7] == "X") or (secondInput == "B3" and Feld[8] == "X") or (secondInput == "C3" and Feld[9] == "X"):
            invalidInput2 = True
            print("nicht möglich")
        elif (secondInput == "A1" and Feld[1] == "O") or (secondInput == "B1" and Feld[2] == "O") or (secondInput == "C1" and Feld[3] == "O") or (secondInput == "A2" and Feld[4] == "O") or (secondInput == "B2" and Feld[5] == "O") or (secondInput == "C2" and Feld[6] == "O") or (secondInput == "A3" and Feld[7] == "O") or (secondInput == "B3" and Feld[8] == "O") or (secondInput == "C3" and Feld[9] == "O"):
            invalidInput2 = True
            print("nicht möglich")
        else: invalidInput2 = False

    if secondInput == "A1":
        Feld[1] = "O"
    if secondInput == "A2":
        Feld[4] = "O"
    if secondInput == "A3":
        Feld[7] = "O"
    if secondInput == "B1":
        Feld[2] = "O"
    if secondInput == "B2":
        Feld[5] = "O"
    if secondInput == "B3":
        Feld[8] = "O"
    if secondInput == "C1":
        Feld[3] = "O"
    if secondInput == "C2":
        Feld[6] = "O"
    if secondInput == "C3":
        Feld[9] = "O"
    
    notWon = checkTiles()

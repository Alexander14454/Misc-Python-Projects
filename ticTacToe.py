# tic tac toe.py
# function to check if any one has won and announces who the winner is when some a if or elif statement is triggered
def checkSpots(playGround):
    global gameOn
    global switchPlayer
    # ////////////////// spots 1, 4 ,7 
    if playGround[1] != "1" and playGround[4] != "4" and playGround[7] != "7":
        if playGround[1] == "X" and playGround[4] == "X" and playGround[7] == "X":
            print("Player 1 wins!!!")
            print(" ", playGround[1], "|", playGround[2], "|", playGround[3], "\n ", playGround[4], "|", playGround[5], "|", playGround[6], "\n ", playGround[7], "|", playGround[8], "|", playGround[9], "\n ",)
            gameOn += 1

        elif playGround[1] == "O" and playGround[4] == "O" and playGround[7] == "O":
            print("Player 2 wins!!!")
            print(" ", playGround[1], "|", playGround[2], "|", playGround[3], "\n ", playGround[4], "|", playGround[5], "|", playGround[6], "\n ", playGround[7], "|", playGround[8], "|", playGround[9], "\n ",)
            gameOn += 1

    # ////////////////// spots 2, 5 ,8 
    if playGround[2] != "2" and playGround[5] != "5" and playGround[8] != "8":
        if playGround[2] == "X" and playGround[5] == "X" and playGround[8] == "X":
            print("Player 1 wins!!!")
            print(" ", playGround[1], "|", playGround[2], "|", playGround[3], "\n ", playGround[4], "|", playGround[5], "|", playGround[6], "\n ", playGround[7], "|", playGround[8], "|", playGround[9], "\n ",)
            gameOn += 1

        elif playGround[2] == "O" and playGround[5] == "O" and playGround[8] == "O":
            print("Player 2 wins!!!")
            print(" ", playGround[1], "|", playGround[2], "|", playGround[3], "\n ", playGround[4], "|", playGround[5], "|", playGround[6], "\n ", playGround[7], "|", playGround[8], "|", playGround[9], "\n ",)
            gameOn += 1

    # ////////////////// spots 3, 6 ,9 
    if playGround[3] != "3" and playGround[6] != "6" and playGround[9] != "9":
        if playGround[3] == "X" and playGround[6] == "X" and playGround[9] == "X":
            print("Player 1 wins!!!")
            print(" ", playGround[1], "|", playGround[2], "|", playGround[3], "\n ", playGround[4], "|", playGround[5], "|", playGround[6], "\n ", playGround[7], "|", playGround[8], "|", playGround[9], "\n ",)
            gameOn += 1

        elif playGround[3] == "O" and playGround[6] == "O" and playGround[9] == "O":
            print("Player 2 wins!!!")
            print(" ", playGround[1], "|", playGround[2], "|", playGround[3], "\n ", playGround[4], "|", playGround[5], "|", playGround[6], "\n ", playGround[7], "|", playGround[8], "|", playGround[9], "\n ",)
            gameOn += 1

    # ////////////////// spots 1, 2 ,3 
    if playGround[1] != "1" and playGround[2] != "2" and playGround[3] != "3":
        if playGround[1] == "X" and playGround[2] == "X" and playGround[3] == "X":
            print("Player 1 wins!!!")
            print(" ", playGround[1], "|", playGround[2], "|", playGround[3], "\n ", playGround[4], "|", playGround[5], "|", playGround[6], "\n ", playGround[7], "|", playGround[8], "|", playGround[9], "\n ",)
            gameOn += 1

        elif playGround[1] == "O" and playGround[2] == "O" and playGround[3] == "O":
            print("Player 2 wins!!!")
            print(" ", playGround[1], "|", playGround[2], "|", playGround[3], "\n ", playGround[4], "|", playGround[5], "|", playGround[6], "\n ", playGround[7], "|", playGround[8], "|", playGround[9], "\n ",)
            gameOn += 1 

    # ////////////////// spots 4, 5 ,6 
    if playGround[4] != "4" and playGround[5] != "5" and playGround[6] != "6":
        if playGround[4] == "X" and playGround[5] == "X" and playGround[6] == "X":
            print("Player 1 wins!!!")
            print(" ", playGround[1], "|", playGround[2], "|", playGround[3], "\n ", playGround[4], "|", playGround[5], "|", playGround[6], "\n ", playGround[7], "|", playGround[8], "|", playGround[9], "\n ",)
            gameOn += 1

        elif playGround[4] == "O" and playGround[5] == "O" and playGround[6] == "O":
            print("Player 2 wins!!!")
            print(" ", playGround[1], "|", playGround[2], "|", playGround[3], "\n ", playGround[4], "|", playGround[5], "|", playGround[6], "\n ", playGround[7], "|", playGround[8], "|", playGround[9], "\n ",)
            gameOn += 1

    # ////////////////// spots 7, 8 ,9   
    if playGround[7] != "7" and playGround[8] != "8" and playGround[9] != "9":
        if playGround[7] == "X" and playGround[8] == "X" and playGround[9] == "X":
            print("Player 1 wins!!!")
            print(" ", playGround[1], "|", playGround[2], "|", playGround[3], "\n ", playGround[4], "|", playGround[5], "|", playGround[6], "\n ", playGround[7], "|", playGround[8], "|", playGround[9], "\n ",)
            gameOn += 1

        elif playGround[7] == "O" and playGround[8] == "O" and playGround[9] == "O":
            print("Player 2 wins!!!")
            print(" ", playGround[1], "|", playGround[2], "|", playGround[3], "\n ", playGround[4], "|", playGround[5], "|", playGround[6], "\n ", playGround[7], "|", playGround[8], "|", playGround[9], "\n ",)
            gameOn += 1   

    # ////////////////// spots 1, 5 ,9 
    if playGround[1] != "1" and playGround[5] != "5" and playGround[9] != "9":
        if playGround[1] == "X" and playGround[5] == "X" and playGround[9] == "X":
            print("Player 1 wins!!!")
            print(" ", playGround[1], "|", playGround[2], "|", playGround[3], "\n ", playGround[4], "|", playGround[5], "|", playGround[6], "\n ", playGround[7], "|", playGround[8], "|", playGround[9], "\n ",)
            gameOn += 1

        elif playGround[1] == "O" and playGround[5] == "O" and playGround[9] == "O":
            print("Player 2 wins!!!")
            print(" ", playGround[1], "|", playGround[2], "|", playGround[3], "\n ", playGround[4], "|", playGround[5], "|", playGround[6], "\n ", playGround[7], "|", playGround[8], "|", playGround[9], "\n ",)
            gameOn += 1

    # ////////////////// spots 3, 5 ,7 
    if playGround[3] != "3" and playGround[5] != "5" and playGround[7] != "7":
        if playGround[3] == "X" and playGround[5] == "X" and playGround[7] == "X":
            print("Player 1 wins!!!")
            print(" ", playGround[1], "|", playGround[2], "|", playGround[3], "\n ", playGround[4], "|", playGround[5], "|", playGround[6], "\n ", playGround[7], "|", playGround[8], "|", playGround[9], "\n ",)
            gameOn += 1

        elif playGround[3] == "O" and playGround[5] == "O" and playGround[7] == "O":
            print("Player 2 wins!!!")
            print(" ", playGround[1], "|", playGround[2], "|", playGround[3], "\n ", playGround[4], "|", playGround[5], "|", playGround[6], "\n ", playGround[7], "|", playGround[8], "|", playGround[9], "\n ",)
            gameOn += 1

    # if all spots are taken and their are no winners 
    if playGround[1] != "1" and playGround[2] != "2" and playGround[3] != "3" and playGround[4] != "4" and playGround[5] != "5" and playGround[6] != "6" and playGround[7] != "7" and playGround[8] != "8" and playGround[9] != "9":
        print("All spaces are taken, no one wins this game")
        print(" ", playGround[1], "|", playGround[2], "|", playGround[3], "\n ", playGround[4], "|", playGround[5], "|", playGround[6], "\n ", playGround[7], "|", playGround[8], "|", playGround[9], "\n ",)
        gameOn += 1

# function to let the current player pick a spot and check if that spot is possible or not
def placePoint(playground):
    # setup values for choosing the mark and mark position
    global playGround
    global switchPlayer 
    switchPlayer += 1
    mark = " "
    mark = str(mark)
    currentPlayer = " "
    currentPlayer = str(currentPlayer)

    # decides which player is currently choosing and makes it so that it places thier mark
    if switchPlayer % 2 == 1:
        mark = "X"
        currentPlayer = "1"
    elif switchPlayer % 2 == 0:
        mark = "O"
        currentPlayer = "2"

    print("Player", currentPlayer, ", choose a spot")
    placedMark = input()
    placedMark = str(placedMark)
    whileOff = 0

    # while loop for current possition 
    while whileOff == 0:
        # elif statement incase the user enters a letter or special character
        if str(placedMark).isalpha():
            print("Choice can not include alphabetical elements")
            placedMark = input()
            placedMark = str(placedMark)
        else:
        #if statement for numbers that are within the brounds of the playGround, more than 0 and less than 10
            if int(placedMark) >= 1 and int(placedMark) <= 9:
            # if statement for choices that are correct 
                if playGround[int(placedMark)] != "O" and playGround[int(placedMark)] != "X":
                    playGround[int(placedMark)] = mark
                    print(" ", playGround[1], "|", playGround[2], "|", playGround[3], "\n ", playGround[4], "|", playGround[5], "|", playGround[6], "\n ", playGround[7], "|", playGround[8], "|", playGround[9], "\n ",)
                    whileOff = 1

                # elif statment if the spot is already owned by current player
                elif playGround[int(placedMark)] == mark:
                    print("This spot is already owned by you")
                    placedMark = input()
                    placedMark = str(placedMark)

                # elif statment if the spot is already owned by other player
                elif playground[int(placedMark)] != mark and playGround[int(placedMark)] == "X" or playGround[int(placedMark)] == "O":
                    print("This spot is already owned by the other player")
                    placedMark = input()
                    placedMark = str(placedMark)

            # elif statement for numbers that are out of brounds of the playGround
            elif int(placedMark) < 1 or int(placedMark) > 9:
                print("Out of bounds, try again")
                placedMark = input()
                placedMark = str(placedMark) 

# ////////////////// declare and assign each of the main characters
playGround = { 1:"1", 2:"2", 3:"3",
               4:"4", 5:"5", 6:"6",
               7:"7", 8:"8", 9:"9" }
gameOn = 0
switchPlayer = 0
print(" ", playGround[1], "|", playGround[2], "|", playGround[3], "\n ", playGround[4], "|", playGround[5], "|", playGround[6], "\n ", playGround[7], "|", playGround[8], "|", playGround[9], "\n ",)

# ////////////////// main code line to be exicuted until player has won or there is not more space left on the board
while gameOn == 0:
    checkSpots(playGround)
    if gameOn == 0:
        placePoint(playGround)
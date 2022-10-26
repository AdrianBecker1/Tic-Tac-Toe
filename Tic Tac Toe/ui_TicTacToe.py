# Sprites

ui_wall_vert = "|"
ui_wall_hor = "-"
ui_circle = "o"
ui_cross = "x"
ui_empty = " "


######################################################################################################################################################################################################

# Function that prints the map
def ui_print(map):

    print("")

    for row in map:
        for piece in range(1):
            for column in row:
                if column == '|':
                    print(ui_wall_vert[piece], end='')
                if column == '-':
                    print(ui_wall_hor[piece], end='')
                if column == 'o':
                    print(ui_circle[piece], end='')
                if column == 'x':
                    print(ui_cross[piece], end='')
                if column == " ":
                    print (ui_empty[piece], end='') 
                if column.isdigit() == True:
                    print (ui_empty[piece], end='')

            print("")
    
    print("")

# Function that gets the key-input from the player and stores it in the input list
def ui_key(list, list_player):

    while True:
        try:

            print("---")
            print("Please choose a number between 1-9:")
            key = int(input())
            
            if key not in list and 1 <= key <= 9:
                break

        except ValueError:
            pass

    
    # store input in list
    list.append(key)
    list_player.append(key)

    return key, list, list_player

######################################################################################################################################################################################################

# Function that prints the tutorial map
def ui_tutorial():

    print("Welcome to Tic Tac Toe! The number corresponds to the number the player presses to place a cross")
    print ("")

    tutorial = [
    " 1 | 2 | 3 ",
    "-----------",
    " 4 | 5 | 6 ",
    "-----------",
    " 7 | 8 | 9 "
    ]   
    
    for row in tutorial:
        for piece in range(1):
            for column in row:
                if column == '|':
                    print(ui_wall_vert[piece], end='')
                if column == '-':
                    print(ui_wall_hor[piece], end='')
                if column == 'o':
                    print(ui_circle[piece], end='')
                if column == 'x':
                    print(ui_cross[piece], end='')
                if column == " ":
                    print (ui_empty[piece], end='') 
                if column.isdigit() == True:
                    print (str(column[piece]), end='')

            print("")
    
    print ("")
    
# Function that asks which difficulty the player wants to play
def ui_choose_difficulty():

    print("Please choose your difficulty:")
    print(" *easy* | *medium* | *hard* ")

    difficulty = str(input())

    # check wrong input
    while difficulty != "easy" and difficulty != "medium" and difficulty != "hard":
        print("---")
        print("Please try again!")
        print("---")
        difficulty = str(input())

        
    return difficulty

#Function that asks if the player wants to start
def ui_choose_start():

    print("Do you want to start? (Y or N)")
    answer = str(input())

    # check for wrong input
    while answer != "Y" and answer != "N":
        print("---")
        print("Please try again:")
        answer = str(input())

    if answer =="Y":
        return True
    else:
        return False
    
# Gets the intitial map
def get_map():

    map = [
    " 1 | 2 | 3 ",
    "-----------",
    " 4 | 5 | 6 ",
    "-----------",
    " 7 | 8 | 9 "
    ] 

    return map
    
######################################################################################################################################################################################################

# Function that shows the gameover screen if the player won
def ui_msg_win(wins, ties, losses, difficulty):

    print("---")
    print("You Won!")
    print("Difficulty: "+ difficulty)
    print ("Wins: "+ str(wins)+ " | Ties: " + str(ties) + " | Losses: " + str(losses))
    print("---")
    
# Function that shows the gameover screen if the player tied
def ui_msg_tie(wins, ties, losses, difficulty):

    print("---")
    print("You Tied!")
    print("Difficulty: "+ difficulty)
    print ("Wins: "+ str(wins)+ " | Ties: " + str(ties) + " | Losses: " + str(losses))
    print("---")
    
# Function that shows the gameover screen if the player lost
def ui_msg_loss(wins, ties, losses, difficulty):

    print("---")
    print("You Lost!")
    print("Difficulty: "+ difficulty)
    print ("Wins: "+ str(wins)+ " | Ties: " + str(ties) + " | Losses: " + str(losses))
    print("---")

######################################################################################################################################################################################################

# Function that asks the player if he would like to play again
def play_again():
    print("Do you want to play again? (Y or N)")
    answer = str(input())
    
    # check for wrong input
    while answer != "Y" and answer != "N":
        print("---")
        print("Please try again:")
        answer = str(input())

    if answer =="Y":
        return True
    else:
        return False


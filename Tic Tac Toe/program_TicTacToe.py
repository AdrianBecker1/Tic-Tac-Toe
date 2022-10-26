import random
from ui_TicTacToe import ui_msg_win, ui_msg_tie, ui_msg_loss

######################################################################################################################################################################################################
# Function that lets the bot play a turn based on the difficulty chosen
def play_bot(map, input_list, input_list_bot, input_list_player, difficulty):

    if difficulty == "easy":
        map, input_list, input_list_bot = play_easy(map, input_list, input_list_bot)
    
    if difficulty == "medium":
        map, input_list, input_list_bot = play_medium(map, input_list, input_list_bot, input_list_player)

    if difficulty == "hard":
        map, input_list, input_list_bot = play_hard(map, input_list, input_list_bot)

    return map, input_list, input_list_bot

######################################################################################################################################################################################################

# Bot randomly chooses 1-9: 
def play_easy(map, list, list_bot):
    
    # random function
    map, list, list_bot = play_random (map, list, list_bot)

    return map, list, list_bot

# Bot randomly chooses 1-9, but wins & blocks if possible
def play_medium(map, list, list_bot, list_player):

    # check if bot has 2 in row
    bot_with_2, win_line = check_3_row (list_bot, 2)

    # ...and finish line if last space is open
    # win == True if such a turn is possible
    win, map, list, list_bot = play_specific (map, list, list_bot, bot_with_2, win_line)

    # finish game if winnable move possible
    if win == True:
        return map, list, list_bot


    ### after check for win comes check for block
    # check if player has 2 in row
    player_with_2, block_line = check_3_row (list_player, 2)

    # ...and finish line if last space is open
    # block == True if such a turn is possible
    block, map, list, list_bot = play_specific (map, list, list_bot, player_with_2, block_line)

    # block row if move possible
    if block == True:
        return map, list, list_bot


    # play random if there is no way to win or to block a win by the player
    map, list, list_bot = play_random (map, list, list_bot)

    return map, list, list_bot

#        
def play_hard(map, list, list_bot):

    input = random.randrange(1,10,1)

    # if the number has already been used, try again
    while input in list:
        input = random.randrange(1,10,1)

    map = update_map (map, input, "o")

    list.append(input)
    list_bot.append(input)

    return map, list, list_bot

######################################################################################################################################################################################################

# Random select a field
def play_random(map, list, list_bot):

    input = random.randrange(1,10,1)

    # if the number has already been used, try again
    while input in list:
        input = random.randrange(1,10,1)

    map = update_map (map, input, "o")

    list.append(input)
    list_bot.append(input)

    return map, list, list_bot

# Finish or block 3 in a row
# returns True if such a move is possible
def play_specific(map, list, list_bot, line_with_2, line):

    if line_with_2 == True:
        
        for number in line:

            if number not in list:

                map = update_map (map, number, "o")

                list.append(number)
                list_bot.append(number)

                return True, map, list, list_bot
        return False, map, list, list_bot
    return False, map, list, list_bot

######################################################################################################################################################################################################

# Function that places the x according to the input the player gave
def play_player (map, key):

    map = update_map (map, key, "x")

    return map 

######################################################################################################################################################################################################

# Function that places x or o on the corresponding number-flied the player or bot has chosen
def update_map (map, input, symbol):  ### Symbol = o or x

    # look for the corresponding number
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == str(input):

                # ... and replace number with symbol (x or o)
                everything_to_the_left = map[x][0:y]
                everything_to_the_right = map[x][y+1:]
                map[x] = everything_to_the_left + str(symbol) + everything_to_the_right
    
    return map

######################################################################################################################################################################################################

def check_gameover(input_list, specific_list, symbol, wins, ties, losses, difficulty):

    player_win = False
    player_tie = False
    player_loss = False

    # check for tie or loss after the bot made a move
    if symbol == "o":
        player_loss, winning_list = check_3_row(specific_list, 3)
        player_tie = check_tie(input_list)
        

    # check for tie or win after the player made a move
    if symbol == "x":
        player_win, winning_list = check_3_row(specific_list, 3)
        player_tie = check_tie(input_list)


    # check if game is won
    if player_win == True:

        wins = wins + 1        
        ui_msg_win(wins, ties, losses, difficulty)

        return True, wins, ties, losses
    
    # check if game is lost
    if player_loss == True :

        losses = losses + 1
        ui_msg_loss(wins, ties, losses, difficulty)

        return True, wins, ties, losses

    # check if game is a tie (has to be the last if function so a win or loss are prompted after 9 turns)
    if player_tie == True :

        ties = ties + 1
        ui_msg_tie(wins, ties, losses, difficulty)

        return True, wins, ties, losses

    return False, wins, ties, losses

###########################################################################################################################################################################################################
# Function tha checks if the player has on of 8 possible lines
def check_3_row(specific_list, counter):

    # 8 Possibilities
    list_3_in_one_row = [[1,2,3],[1,5,9],[1,4,7],[4,5,6],[7,8,9],[7,5,3],[2,5,8],[3,6,9]]

    line_count = 0
    list_counter = 0

    # go through every list inside list and check if payer or bot has 3 resp 2 of them:
    # returns True if there are 2 or 3 in one line and the list that contains said line
    for list in list_3_in_one_row:
        for number in list:

            list_counter = list_counter + 1
            
            # Add 1 if number occurs
            if number in specific_list:

                line_count = line_count + 1
            
            # there are 2 or 3 in one line depending on the counter
            if line_count == counter:

                return True, list
                            
            # resets the line_count if not every number of one possible win-list is in input list
            if list_counter == 3:

                list_counter = 0
                line_count = 0

    return False, list


# tie if 9 turns have been made
def check_tie(list):

    if len(list) == 9:
        return True
    
    else:
        return False
from program_TicTacToe import play_bot, play_player, check_gameover
from ui_TicTacToe import ui_print, ui_key, ui_tutorial, ui_choose_difficulty, ui_choose_start, get_map, play_again


def play_tictactoe ():

    player = True

    # scores
    wins = 0
    ties = 0
    losses = 0

    ############### loop that runs as long as the player wants to play ###############
    while player:
        
        # Promts the tutorial
        ui_tutorial()

        # Get the map the player wants to play
        difficulty = ui_choose_difficulty()  ### easy, medium, hard (str)
        
        # ask if the player wants to start
        start = ui_choose_start ()  ### True (start), False (dont start)

        # Get starting map
        map = get_map()

        game_finished = False
        input_list =  []
        input_list_bot = []
        input_list_player = []

        ########### loop that runs until the game is over #############################
        while not game_finished:

            ### Bot Turn
            # if player does not start, let computer place first o and print the map afterwards
            if start == False:
                
                # get the next input from bot and place o on map
                map, input_list, input_list_bot = play_bot (map, input_list, input_list_bot, input_list_player, difficulty)
                ui_print (map)

                # Check if game is over after the bot played
                game_finished, wins, ties, losses = check_gameover (input_list, input_list_bot, "o", wins, ties, losses, difficulty)

                # End game if game is finished (prevents that the while-loop lets the player do one more turn)
                if game_finished == True:
                    break


            ### Player Turn
            # get the next input from player
            key, input_list, input_list_player = ui_key (input_list, input_list_player)

            # ...and place x on the map
            map = play_player (map, key)
            ui_print (map)

            # Check if game is over after the player played
            game_finished, wins, ties, losses  = check_gameover (input_list, input_list_player, "x", wins, ties, losses, difficulty)

            # End game if game is finished (prevents that the while-loop lets the player do one more turn)
            if game_finished == True:
                break
            

            ### Bot Turn
            # if player does start, let computer place o after player and print the map afterwards
            if start == True:

                map, input_list, input_list_bot = play_bot (map, input_list, input_list_bot, input_list_player, difficulty)
                ui_print (map)

                # Check if game is over after the bot played
                game_finished, wins, ties, losses  = check_gameover (input_list, input_list_bot, "o", wins, ties, losses, difficulty)

                # End game if game is finished (prevents that the while-loop lets the player do one more turn)
                if game_finished == True:
                    break


            #####
        
        player = play_again()


###############################
play_tictactoe() # Play Function
###############################
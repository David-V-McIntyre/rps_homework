class Game():
    # the win_lookup function creates a dictionary of key-value pairs for each win condition. 
    def __init__(self):
        self.win_lookup = {
            "scissors" : "paper",
            "paper" : "rock",
            "rock" : "scissors"
        }

    def play(self, player_1, player_2):

# this method is going to take the players and determine who is the winner. It does this by taking 2 parameters(players) and using
# the prior win_lookup method to check the sequence of choices against the viable win conditions. Essentially the if statement determines
# if player_1 is the winner and the elif determines if player_2 is the winner. If neither is true then the logic in the game_controller 
# will determine that it must be a draw. the lower() function is built-in to python and will convert anyt string to all lower-case -
# this is useful in case the user inputs capital letters into the url. Without the "lower()" function this would return an error.

        winner = None

        if self.win_lookup[player_1.choice.lower()] == player_2.choice.lower():
            winner = player_1
        elif self.win_lookup[player_2.choice.lower()] == player_1.choice.lower():
            winner = player_2

        return winner



# below is my attempt at writing a game_controller. As you can see I attempted to write if/elif statements for each possible outcome -
# I was using a form to get player names and a select form to pick choices and this controller was going to determine the winner.

# def play_game(player1_choice, player2_choice):
#     if player1_choice == "rock" and player2_choice == "scissors":
#         print("Player 1 wins!")
#     elif player1_choice == "rock" and player2_choice == "paper":
#         print("Player 2 wins!")
#     elif player1_choice == player2_choice:
#         print("None")
#     elif player1_choice == "scissors" and player2_choice == "paper":
#         print ("Player 1 wins!")
#     elif player1_choice == "scissors" and player2_choice == "rock":
#         print ("Player 2 wins!")
#     elif player1_choice == "paper" and player2_choice == "rock":
#         print ("Player 1 wins!")
#     elif player1_choice == "paper" and player1_choice == "scissors":
#         print("Player 2 wins!") 
#     return


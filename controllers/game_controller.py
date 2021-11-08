from app import app
from models.game import *
from models.player import *
from flask import render_template

@app.route('/<player_1_choice>/<player_2_choice>')
# this app route allows the user to assign choices to each player by entering the choice as part of the URL.
def play(player_1_choice, player_2_choice):
# this method takes the two choices entered in the url and inputs them as paramters into the play function
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
# this assigns the arguments passed into play() as variables by calling the player classes from player.py
    game = Game() 
# this assigns the Game class to the game variable so that it can be called in the next line.

    winner = game.play(player_1, player_2)
# this applies the Game class (now assigned to the game variable) with the play method (all from game.py) 
# and the players we just assigned
#  in line 10 and 11 and resolves a winner. 
    
    return render_template("game.html", player_1=player_1, player_2=player_2, winner=winner)

# this returns the render template using the game.html file and passes the players and winner (from 
# earlier in this file) to the render template so that it can enter them into the game.html file.



# below is my original attempt at creating controllers. I eventually got frustrated and looked at the solution. 
# Looking at the solution I can tell that I was thinking about the problem in the wrong way and wasn't strictly 
# following the brief. Lesson learned: keep it simple

# from flask import render_template #, request, redirect
# from app import app
# from models.player import *
# from models.game import *
# # from models.players import player1, player2
# # from models.playgame import play_game

# @app.route("/")
# def index():
#     return render_template('index.html', title="Let's play a game!")

# @app.route("/", methods=["POST"])
# def play():
#     player1_name = "player1"
#     player2_name = "player2"
#     player1_choice = "player1choice"
#     player2_choice = "player2choice"
#     play_game(player1_choice, player2_choice)

    
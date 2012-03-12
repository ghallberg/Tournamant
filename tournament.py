from random import shuffle
from math   import log
class Tournament:
    """Basic single bracket tournament"""


    def __init__(this, arg_players):
        """Initialize the tournament with a list of players"""
        this.players = arg_players
        this.started = False;

    def add_player(this, player):
        """Add a player to the tournament if possible, return (status, message) tuple"""
        if this.started:
            return (False, "Tournament started")
        this.players.append(player)
        return (True, "Player added")
    
    def start_tourney(this):
        """Do initial preparation to start tourney. Set the started variable to true."""
        num_rounds = calc_rounds(len(this.players))
        this.cur_round = []

        this.started = True

    def seed_round(this):
        print(this.players)
        shuf_players = this.players
        shuffle(shuf_players)
        print(shuf_players)
        


def calc_rounds(num_players, next_pow = 1):
    if num_players == 0:
        return -1
    if num_players == 1:
        return 0
    if next_pow >= num_players:
        return log(next_pow, 2)
    
    return calc_rounds(num_players, next_pow*2)
    

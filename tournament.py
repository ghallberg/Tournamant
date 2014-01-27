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
            raise(Exception("Tournament started!"))
        this.players.append(player)

    def add_players(this, players):
        for player in players:
            this.add_player(player)
    
    def start_tourney(this):
        """Do initial preparation to start tourney. Set the started variable to true."""
        if this.started:
            raise(Exception("Already started."))

        try:
            this.num_rounds = calc_rounds(len(this.players))

            this.started = True

            this.seed_round()
        except Exception as e:
            raise e

    def report_match(this, match, player1_score, player2_score):
        """Finalize the reported match."""

    def seed_round(this):
        """Seed a new round"""
        if this.win_condition():
            raise Exception("Tournament finished!")
        if not this.started:
            raise Exception("Tournament not started yet!")


    def win_condition(this):
        return False

def calc_rounds(num_players, next_pow = 1):
    if num_players < 1:
        raise(Exception("Too few players!"))
    if num_players == 1:
        return 0
    if next_pow >= num_players:
        return log(next_pow, 2)
    
    return calc_rounds(num_players, next_pow*2)
    

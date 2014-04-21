from random import shuffle
from math   import log
import logging
class Tournament:
    """Basic single bracket tournament"""

    def __init__(self):
        """Initialize the tournament with a list of players"""
        logging.debug('Tournament created')
        self.players = []
        self.started = False;

    def add_player(self, player):
        """Add a player to the tournament if possible, return (status, message) tuple"""
        if self.started:
            raise(Exception("Tournament started"))
        if player in self.players:
            raise(Exception("Player already registered"))
        self.players.append(player)
        logging.info('Added player %s', player)

    def add_players(self, players):
        for player in players:
            self.add_player(player)
        logging.info('Added players: %s', players)
    
    def start_tourney(self):
        """Do initial preparation to start tourney. Set the started variable to true."""
        if self.started:
            raise(Exception("Already started."))

        try:
            self.num_rounds = calc_rounds(len(self.players))

            self.started = True

            self._seed_round()
            logging.info('Started tournament with %s rounds, first round matchups: %s', self.num_rounds, self.matches)
        except Exception as e:
            raise e

    def report_match(self, match, player1_score, player2_score):
        """Finalize the reported match."""

    def _seed_round(self):
        """Seed a new round"""
        if not self.started:
            raise Exception("Tournament not started yet!")
        if self.has_winner():
            raise Exception("Tournament finished!")
        shuffle(self.players)
        self.matches = [self.players[x:x+2] for x in range(0, len(self.players), 2)]
        if len(self.matches[-1]) == 1:
            self.matches[-1].append(None)


    def has_winner(self):
        return False

def calc_rounds(num_players, next_pow = 1):
    if num_players < 1:
        raise(Exception("Too few players!"))
    if num_players == 1:
        return 0
    if next_pow >= num_players:
        return log(next_pow, 2)
    
    return calc_rounds(num_players, next_pow*2)


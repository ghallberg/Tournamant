#!/usr/bin/python3
import unittest
from tournamant.tournament import Tournament
from tournamant.tournament import calc_rounds
import logging

class TestTourney(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(filename = 'tournamant_test.log', filemode = 'w',
                level=logging.DEBUG)
        self.tourn = Tournament()
        self.ONE_PLAYER = ["Gustaf"]
        self.TWO_PLAYERS = ["Gustaf", "bark"]
        self.THREE_PLAYERS = ["Gustaf", "bark", "Horv"]
        self.THREE_PLAYERS_DUPLICATE = ["Gustaf", "Gustaf", "Horv"]
        self.FOUR_PLAYERS = ["Gustaf", "bark", "Horv", "Chanuka"]

    def test_player(self):
        self.tourn.add_player("Gustaf")
        self.assertTrue(self.tourn.players == ["Gustaf"])

        self.tourn.add_player("bark")
        self.assertTrue(self.tourn.players == ["Gustaf", "bark"])

    def test_duplicate_player(self):
        self.tourn.add_player("Gustaf")
        self.assertTrue(self.tourn.players == ["Gustaf"])

        with self.assertRaises(Exception):
            self.tourn.add_player("Gustaf")

    def add_multiple_players(self):
        self.tourn.add_players(self.THREE_PLAYERS)
        for player in self.THREE_PLAYERS:
            self.assertTrue(player in self.tourn.players)

    def add_multiple_players_including_duplicate(self):
        with self.assertRaises(Exception):
            self.tourn.add_players(self.THREE_PLAYERS_DUPLICATE)

    def test_empty_start(self):
        self.assertRaises(Exception, self.tourn.start_tourney)

    def test_start(self):
        self.tourn.add_player("Gustaf")
        self.tourn.start_tourney()
        self.assertTrue(self.tourn.started)
        self.assertRaises(Exception, self.tourn.add_player, "Bark")

    def test_calc_rounds(self):
        self.assertRaises(Exception, calc_rounds, -1)
        self.assertRaises(Exception, calc_rounds, 0)
        self.assertTrue(calc_rounds(1) == 0)
        self.assertTrue(calc_rounds(2) == 1)
        self.assertTrue(calc_rounds(3) == 2)
        self.assertTrue(calc_rounds(4) == 2)
        self.assertTrue(calc_rounds(5) == 3)
        self.assertTrue(calc_rounds(9) == 4)
        self.assertTrue(calc_rounds(16) == 4)
        self.assertTrue(calc_rounds(33) == 6)

    def test_seeding(self):
        self.tourn.add_players(self.FOUR_PLAYERS)
        self.tourn.start_tourney()
        flat_matches = [player for match in self.tourn.matches for player in
                match]
        for player in self.FOUR_PLAYERS:
            self.assertTrue(player in flat_matches)

        for match in self.tourn.matches:
            self.assertTrue(len(match) == 2)

    def test_byes(self):
        self.tourn.add_players(self.THREE_PLAYERS)
        self.tourn.start_tourney()

        self.assertTrue(self.tourn.matches[-1][-1] is None)


if __name__ == '__main__':
    unittest.main()

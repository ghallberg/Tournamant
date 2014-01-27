import unittest
from tournament import Tournament
from tournament import calc_rounds

class TestTourney(unittest.TestCase):

    def setUp(self):
        self.tourn = Tournament([])
        self.ONE_PLAYER = ["Gustaf"]
        self.TWO_PLAYER = ["Gustaf", "bark"]
        self.THREE_PLAYER = ["Gustaf", "bark", "Horv"]
        self.FOUR_PLAYER = ["Gustaf", "bark", "Horv", "Chanuka"]
        
    def test_player(self):
        self.tourn.add_player("Gustaf")
        self.assertTrue(self.tourn.players == ["Gustaf"])

        self.tourn.add_player("bark")
        self.assertTrue(self.tourn.players == ["Gustaf", "bark"])

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
        self.tourn.add_players(self.FOUR_PLAYER)
        self.tourn.start_tourney()


if __name__ == '__main__':
        unittest.main()

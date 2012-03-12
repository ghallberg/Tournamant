import unittest
from tournament import Tournament
from tournament import calc_rounds

class TestTourney(unittest.TestCase):

    def setUp(self):
        self.tourn = Tournament([])
        
    def test_player(self):
        status, mess = self.tourn.add_player("Gustaf")
        self.assertTrue(len(self.tourn.players) == 1)
        status, mess = self.tourn.add_player("Bark")
        self.assertTrue(len(self.tourn.players) == 2)



    def test_start(self):
        self.tourn.start_tourney()
        status, mess = self.tourn.add_player("Bark")
        self.assertFalse(status)
        self.assertTrue(self.tourn.started)

    def test_calc_rounds(self):
        self.assertTrue(calc_rounds(0) == -1)
        self.assertTrue(calc_rounds(1) == 0)
        self.assertTrue(calc_rounds(2) == 1)
        self.assertTrue(calc_rounds(3) == 2)
        self.assertTrue(calc_rounds(4) == 2)
        self.assertTrue(calc_rounds(5) == 3)
        self.assertTrue(calc_rounds(9) == 4)
        self.assertTrue(calc_rounds(16) == 4)
        self.assertTrue(calc_rounds(33) == 6)


if __name__ == '__main__':
        unittest.main()

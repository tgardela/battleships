import unittest

from app.game.aiplayer import *


class TestAIPlayer(unittest.TestCase):
    def setUp(self):
        pass


    def test_get_shot_returns_in_margin(self):
        row, col = get_shot()
        self.assertTrue(row in range(1, 11))
        self.assertTrue(col in range(1, 11))


if __name__=='__main__':
    unittest.main(verbosity=2)
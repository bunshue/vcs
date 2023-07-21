from unittest import TestCase
from unittest.mock import MagicMock, patch

from main import AlienColumn
from test_utils import setup


class TestAlienColumn(TestCase):
    RIGHT = 1
    LEFT = -1

    @classmethod
    def setUpClass(cls) -> None:
        setup()

    def setUp(self) -> None:
        self.alien_column = AlienColumn(300, 300)

        mock_game_layer = MagicMock()
        mock_game_layer.width = 800
        for alien in self.alien_column.aliens:
            alien.parent = mock_game_layer

    def test_has_at_least_one_alien(self):
        self.assertEqual(len(self.alien_column.aliens) > 1, True)

    def test_should_not_turn_when_no_more_aliens(self):
        self.alien_column.aliens = []
        self.assertEqual(self.alien_column.should_turn(None), False)

    def test_turn_right(self):
        self.set_alien_x_position(800)
        self.assertEqual(self.alien_column.should_turn(TestAlienColumn.RIGHT), True)

    def test_turn_left(self):
        self.set_alien_x_position(0)
        self.assertEqual(self.alien_column.should_turn(TestAlienColumn.LEFT), True)

    def test_should_not_shoot_when_no_more_aliens(self):
        self.alien_column.aliens=[]
        self.assertEqual(self.alien_column.shoot(), None)

    @patch("random.random")
    def test_should_not_shoot_when_shoot_rate_is_over_threshold(self, mock_random):
        mock_random.return_value=1
        self.assertEqual(self.alien_column.shoot(), None)

    @patch("random.random")
    def test_shoot(self, mock_random):
        mock_random.return_value = 0
        self.assertIsNotNone(self.alien_column.shoot())

    def set_alien_x_position(self, x_position):
        for alien in self.alien_column.aliens:
            alien.x = x_position

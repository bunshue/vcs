from collections import defaultdict
from unittest import TestCase
from unittest.mock import MagicMock

import cocos.euclid as eu
from pyglet.window import key

from main import PlayerCannon, PlayerShoot, GameLayer
from test_utils import setup


class TestPlayerCannon(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        setup()

    def setUp(self) -> None:
        self.player_cannon = PlayerCannon(300, 300)
        self.player_cannon.parent = MagicMock()
        self.player_cannon.parent.width = 640

        PlayerCannon.KEYS_PRESSED = defaultdict(int)
        PlayerShoot.INSTANCE = None

    def test_shoot_cannon_when_press_space(self):
        self.assertTrue(PlayerShoot.INSTANCE is None)

        PlayerCannon.KEYS_PRESSED[key.SPACE] = 1
        self.player_cannon.update(0)
        self.assertTrue(PlayerShoot.INSTANCE is not None)

    def test_move_left(self):
        self.assertTrue(self.player_cannon.position == eu.Vector2(300, 300))

        PlayerCannon.KEYS_PRESSED[key.LEFT] = 1
        self.player_cannon.update(1)
        self.assertTrue(self.player_cannon.position == eu.Vector2(100, 300))

    def test_move_right(self):
        self.assertTrue(self.player_cannon.position == eu.Vector2(300, 300))

        PlayerCannon.KEYS_PRESSED[key.RIGHT] = 1
        self.player_cannon.update(1)
        self.assertTrue(self.player_cannon.position == eu.Vector2(500, 300))

    def test_cannot_move_to_out_of_bounds(self):
        self.player_cannon.position = eu.Vector2(10, 300)

        PlayerCannon.KEYS_PRESSED[key.LEFT]=1
        self.player_cannon.update(1)
        self.assertTrue(self.player_cannon.position == eu.Vector2(10, 300))

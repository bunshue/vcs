from unittest import TestCase
from unittest.mock import MagicMock

import cocos.collision_model as cm

from main import Alien, Bunker, PlayerCannon, Shoot, PlayerShoot
from main import GameLayer
from test_utils import setup


class TestGameLayer(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        setup()

    def setUp(self) -> None:
        self.game_layer = GameLayer(MagicMock())

    def test_did_instantiate_actors(self):
        self.assertEqual(1, len(self.get_game_children_with_type(PlayerCannon)))
        self.assertEqual(50, len(self.get_game_children_with_type(Alien)))
        self.assertEqual(0, len(self.get_game_children_with_type(Shoot)))

        self.assertTrue(0 < len(self.get_game_children_with_type(Bunker)))

    def test_collide_shoot_and_alien(self):
        player_shoot = PlayerShoot(100, 100)
        alien = Alien("img/alien1.png", 100, 100, 15)

        self.game_layer.add(player_shoot)
        self.game_layer.add(alien)

        self.assertTrue(player_shoot in self.get_game_children())
        self.assertTrue(alien in self.get_game_children())
        self.assertTrue(self.game_layer.score == 0)

        self.game_layer.update(0)

        self.assertTrue(player_shoot not in self.get_game_children())
        self.assertTrue(alien not in self.get_game_children())
        self.assertTrue(self.game_layer.score == 15)

    def test_collide_player_and_alien(self):
        player = self.game_layer.player
        player.position = (100, 100)
        player.cshape = cm.AARectShape(player.position, player.width / 2, player.height / 2)

        alien = Alien("img/alien1.png", 100, 100, 15)

        self.game_layer.add(alien)

        self.assertTrue(player in self.get_game_children())
        self.assertTrue(alien in self.get_game_children())
        self.assertTrue(self.game_layer.lives == 3)
        self.assertTrue(self.game_layer.score == 0)

        self.game_layer.update(0)

        self.assertTrue(player not in self.get_game_children())
        self.assertTrue(alien not in self.get_game_children())
        self.assertTrue(self.game_layer.lives == 2)
        self.assertTrue(self.game_layer.score == 0)

    def test_game_won(self):
        self.assertTrue(len(self.get_game_children_with_type(Alien)) > 0)
        self.remove_game_children_with_type(Alien)
        self.assertTrue(len(self.get_game_children_with_type(Alien)) == 0)
        self.game_layer.hud.show_game_won.assert_not_called()

        self.game_layer.update(0)

        self.game_layer.hud.show_game_won.assert_called_once()

    def get_game_children(self):
        return [child for _, child in self.game_layer.children]

    def get_game_children_with_type(self, child_class):
        return [child for child in self.get_game_children() if isinstance(child, child_class)]

    def remove_game_children_with_type(self, child_class):
        for _, child in self.game_layer.children:
            if isinstance(child, child_class):
                child.kill()

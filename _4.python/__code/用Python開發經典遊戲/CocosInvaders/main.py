import random
from collections import defaultdict
from typing import List

import cocos
import cocos.collision_model as cm
import cocos.euclid as eu
import cocos.layer
from pyglet.image import load, ImageGrid, Animation
from pyglet.window import key


class Actor(cocos.sprite.Sprite):
    def __init__(self, image, x, y):
        super(Actor, self).__init__(image)
        pos = eu.Vector2(x, y)

        # self.position is defined in cocos.sprite.Sprite with type (int, int)
        # assigning self.position type eu.Vector2(int,int) seems to assign the type (int,int)
        self.position = pos
        self.cshape = cm.AARectShape(self.position, self.width / 2, self.height / 2)

    def move(self, offset):
        self.position += offset
        self.cshape = cm.AARectShape(self.position, self.width / 2, self.height / 2)

    def update(self, elapsed):
        """Template design pattern for the child classes to implement"""
        pass


class PlayerCannon(Actor):
    KEYS_PRESSED = defaultdict(int)

    def __init__(self, x, y):
        super(PlayerCannon, self).__init__("img/cannon.png", x, y)
        self.speed = eu.Vector2(200, 0)

    def update(self, elapsed):
        pressed = PlayerCannon.KEYS_PRESSED
        space_pressed = pressed[key.SPACE] == 1

        if PlayerShoot.INSTANCE is None and space_pressed:
            self.parent.add(PlayerShoot(self.x, self.y + 50))

        movement = pressed[key.RIGHT] - pressed[key.LEFT]
        w = self.width / 2

        # w <= self.x <= self.parent.width is the same as
        # w <= self.x and self.x <= self.parent.width:
        if movement != 0 and w <= self.x <= self.parent.width:
            self.move(self.speed * movement * elapsed)


class GameLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self, hud):
        super(GameLayer, self).__init__()
        width, height = cocos.director.director.get_window_size()
        self.hud = hud
        self.width = width
        self.height = height
        self.lives = 3
        self.score = 0
        self.update_score()
        self.create_player()
        self.create_alien_group(100, 300)
        self.create_bunker_groups()

        # recommended cell size is the maximum object width *1.25
        cell = self.player.width * 1.25
        self.collman = cm.CollisionManagerGrid(0, width, 0, height,
                                               cell, cell)

        # Defined in cocos.cocosnode.CocosNode
        self.schedule(self.update)

    def on_key_press(self, k, _):
        PlayerCannon.KEYS_PRESSED[k] = 1

    def on_key_release(self, k, _):
        PlayerCannon.KEYS_PRESSED[k] = 0

    def create_player(self):
        self.player = PlayerCannon(self.width / 2, 50)
        self.add(self.player)
        self.hud.update_lives(self.lives)

    def update_score(self, score=0):
        self.score += score
        self.hud.update_score(self.score)

    def create_alien_group(self, x, y):
        """(0,0) = bottom left"""
        self.alien_group = AlienGroup(x, y)
        for alien_column in self.alien_group:
            self.add(alien_column)

    def create_bunker_groups(self):
        for i in range(75, 775, 150):
            self.create_bunker_group(i)

    def create_bunker_group(self, initial_x):
        for x in range(initial_x, initial_x + 50, 8):
            for y in range(120, 160, 8):
                self.add(Bunker(x, y))

    def update(self, dt):
        self.collman.clear()

        node: Actor
        for _, node in self.children:
            self.collman.add(node)
            if not self.collman.knows(node):
                self.remove(node)

        for k, v in self.collide_with_group(PlayerShoot.INSTANCE, self.get_children_by_types(Alien)).items():
            for alien in v:
                self.update_score(alien.score)
                alien.kill()
            if len(v) > 0:
                k.kill()

        for k, v in self.collide_with_group(self.player, self.get_children_by_types((Shoot, Alien))).items():
            sprite: cocos.sprite.Sprite
            for sprite in v:
                sprite.kill()

            if len(v) > 0:
                k.kill()
                self.respawn_player()

        for k, v in self.group_collide(
                self.get_children_by_types(Shoot),
                self.get_children_by_types(Bunker)
        ).items():
            for bunker in v:
                bunker.kill()
            if len(v) > 0:
                k.kill()

        no_more_aliens = len(self.get_children_by_types(Alien)) == 0
        if no_more_aliens:
            self.unschedule(self.update)
            self.hud.show_game_won()

        for column in self.alien_group.columns:
            shoot = column.shoot()
            if shoot is not None:
                self.add(shoot)

        for _, node in self.children:
            node.update(dt)

        self.alien_group.update(dt)
        if random.random() < 0.001:
            self.add(MysteryShip(50, self.height - 50))

    def get_children_by_types(self, classes):
        # child[1] :Actor
        return [child[1] for child in self.children if isinstance(child[1], classes)]

    def collide_with_group(self, sprite, group_a: List[cocos.sprite.Sprite]):
        collision_array = []
        if sprite is not None:
            collision_array = [a for a in group_a if self.collman.they_collide(sprite, a)]
        return {sprite: collision_array}

    def group_collide(self, group_a: List[cocos.sprite.Sprite], group_b: List[cocos.sprite.Sprite]):
        collision_dict = {}
        for a in list(filter(None, group_a)):
            collision_dict[a] = []
            for b in list(filter(None, group_b)):
                if self.collman.they_collide(a, b):
                    collision_dict[a].append(b)
        return collision_dict

    def respawn_player(self):
        """Unschedule update() when there are no more lives left to stop the main loop"""
        self.lives -= 1
        if self.lives < 0:
            self.unschedule(self.update)
            self.hud.show_game_over()
        else:
            self.create_player()


class Bunker(Actor):
    def __init__(self, x, y):
        super(Bunker, self).__init__("img/bunkerPart.png", x, y)


class Alien(Actor):
    def load_animation(image):
        seq = ImageGrid(load(image), 2, 1)
        return Animation.from_image_sequence(seq, 0.5)

    TYPES = {
        "1": (load_animation("img/alien1.png"), 40),
        "2": (load_animation("img/alien2.png"), 20),
        "3": (load_animation("img/alien3.png"), 10)
    }

    def from_type(x, y, alien_type, column):
        animation, score = Alien.TYPES[alien_type]
        return Alien(animation, x, y, score, column)

    # We pass a reference to alien_column so the column of aliens know which alien is at the bottom
    def __init__(self, img, x, y, score, alien_column=None):
        super(Alien, self).__init__(img, x, y)
        self.score = score
        self.alien_column = alien_column

    def on_exit(self):
        super(Alien, self).on_exit()
        if self.alien_column:
            self.alien_column.remove(self)


class MysteryShip(Alien):
    SCORES = [10, 50, 100, 200]

    def __init__(self, x, y):
        score = random.choice(MysteryShip.SCORES)
        super(MysteryShip, self).__init__("img/alien4.png", x, y, score)
        self.speed = eu.Vector2(150, 0)

    def update(self, elapsed):
        self.move(self.speed * elapsed)


class AlienColumn(object):
    def __init__(self, x, y):
        alien_types = enumerate(["3", "3", "2", "2", "1"])
        self.aliens = [Alien.from_type(x, y + i * 60, alien, self)
                       for i, alien in alien_types]

    def should_turn(self, direction):
        if len(self.aliens) == 0:
            return False
        alien = self.aliens[0]
        x, parent_width = alien.x, alien.parent.width

        right = 1
        left = -1
        return (x >= parent_width - 50 and direction == right) or (x <= 50 and direction == left)

    def remove(self, alien):
        self.aliens.remove(alien)

    def shoot(self):
        # We set a low probability of shooting since random() is called multiple times per second
        if random.random() < 0.002 and len(self.aliens) > 0:
            bottom_most_alien_position = self.aliens[0].position
            return Shoot(bottom_most_alien_position[0], bottom_most_alien_position[1] - 50)
        return None


class AlienGroup(object):
    def __init__(self, x, y):
        self.columns = [AlienColumn(x + i * 60, y)
                        for i in range(10)]
        self.speed = eu.Vector2(10, 0)

        # 1 = right
        # -1 = left
        self.direction = 1
        self.elapsed = 0.0
        self.period = 1.0

    def __iter__(self):
        for column in self.columns:
            for alien in column.aliens:
                yield alien

    def update(self, elapsed):
        self.elapsed += elapsed
        while self.elapsed >= self.period:
            self.elapsed -= self.period
            offset = self.direction * self.speed
            if self.side_reached():
                self.direction *= -1
                offset = eu.Vector2(0, -10)
            for alien in self:
                alien.move(offset)

    def side_reached(self):
        return any(map(lambda column: column.should_turn(self.direction), self.columns))


class Shoot(Actor):
    def __init__(self, x, y, image="img/shoot.png"):
        super(Shoot, self).__init__(image, x, y)
        self.speed = eu.Vector2(0, -400)

    def update(self, elapsed):
        self.move(self.speed * elapsed)


class PlayerShoot(Shoot):
    INSTANCE = None
    """The player can't shoot until the shoot hits an enemy or goes off-screen"""

    def __init__(self, x, y):
        super(PlayerShoot, self).__init__(x, y, image="img/laser.png")
        self.speed *= -1
        PlayerShoot.INSTANCE = self

    def on_exit(self):
        super(PlayerShoot, self).on_exit()
        PlayerShoot.INSTANCE = None


class HUD(cocos.layer.Layer):
    """
    score-----------lives\n
    |                |\n
    |    game over   |\n
    |                |\n
    """

    def __init__(self):
        super(HUD, self).__init__()
        width, height = cocos.director.director.get_window_size()
        self.score_text = cocos.text.Label("", font_size=18)
        self.score_text.position = (20, height - 40)
        self.lives_text = cocos.text.Label("", font_size=18)
        self.lives_text.position = (width - 100, height - 40)
        self.add(self.score_text)
        self.add(self.lives_text)

    def update_score(self, score):
        self.score_text.element.text = "Score %s" % score

    def update_lives(self, lives):
        self.lives_text.element.text = "Lives %s" % lives

    def show_game_over(self):
        self._show_center_text("Press F to pay respects")

    def show_game_won(self):
        self._show_center_text("You won!")

    def _show_center_text(self, text):
        width, height = cocos.director.director.get_window_size()
        label = cocos.text.Label(text,
                                 font_size=50,
                                 anchor_x="center",
                                 anchor_y="center")
        label.position = (width / 2, height / 2)
        self.add(label)


if __name__ == '__main__':
    cocos.director.director.init(caption="Cocos Invaders", width=800, height=650)
    main_scene = cocos.scene.Scene()
    hud_layer = HUD()
    game_layer = GameLayer(hud_layer)

    main_scene.add(hud_layer, z=1)
    main_scene.add(game_layer, z=0)

    cocos.director.director.run(main_scene)

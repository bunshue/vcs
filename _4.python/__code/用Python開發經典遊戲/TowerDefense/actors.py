import math

import cocos
import cocos.actions as ac
import cocos.collision_model as cm
import cocos.euclid as eu
import cocos.sprite
import pyglet.image
from pyglet.image import Animation

EXPLOSION_IMG = Animation.from_image_sequence(
    pyglet.image.ImageGrid(
        pyglet.image.load("assets\explosion.png"),
        1,
        8
    ),
    0.07,
    False
)


class Actor(cocos.sprite.Sprite):
    def __init__(self, img, x, y):
        super(Actor, self).__init__(img, position=(x, y))
        self._cshape = cm.CircleShape(self.position, self.width * 0.5)

    @property
    def cshape(self):
        """
        Actions like MoveBy only update the sprite position, not the cshape.center
        With this construct, when the cshape is read, we also update the cshape.center
        """
        self._cshape.center = eu.Vector2(self.x, self.y)
        return self._cshape


class Turret(Actor):
    def __init__(self, x, y):
        super(Turret, self).__init__("turret.png", x, y)
        self.add(cocos.sprite.Sprite("range.png", opacity=50, scale=5))

        self.cshape.r = 125.0
        self.target = None
        self.period = 2.0
        self.reload = 0.0
        self.schedule(self._shoot)

    def _shoot(self, dt):
        """Shoot every self.period seconds"""
        if self.reload < self.period:
            self.reload += dt
        elif self.target is not None:
            self.reload -= self.period
            offset = eu.Vector2(self.target.x - self.x,
                                self.target.y - self.y)
            shoot_position = self.cshape.center + offset.normalized() * 20
            self.parent.add(Shoot(shoot_position, offset, self.target))

    def collide(self, other):
        """Rotate the turret to simulate aiming at the target"""
        self.target = other
        if self.target is not None:
            x, y = other.x - self.x, other.y - self.y
            angle = -math.atan2(y, x)
            self.rotation = math.degrees(angle)


class Shoot(cocos.sprite.Sprite):
    """
    Shoot isn't an actor since it's not required to collide
    Since we don't collide, we just call target.hit after 0.1 seconds
    """

    def __init__(self, pos, offset, target):
        super(Shoot, self).__init__('shoot.png', position=pos)
        self.do(ac.MoveBy(offset, 0.1) +
                ac.CallFunc(self.kill) +
                ac.CallFunc(target.hit))


class Enemy(Actor):
    def __init__(self, x, y, actions):
        super(Enemy, self).__init__("tank.png", x, y)
        self.health = 100
        self.score = 20

        # Enemies can also be destroyed by hitting the bunker
        self.destroyed_by_turret = False
        self.do(actions)

    def hit(self):
        self.health -= 25
        self.do(Hit())
        if self.health <= 0 and self.is_running:
            self.destroyed_by_turret = True
            self.explode()

    def explode(self):
        self.parent.add(Explosion(self.position))
        self.kill()


class Hit(ac.IntervalAction):
    def init(self, duration=0.5):
        self.duration = duration

    def update(self, t):
        """Temporarily set the sprite's colour to red, then gradually return to the original colour"""
        self.target.color = (255, 255 * t, 255 * t)


class Explosion(cocos.sprite.Sprite):
    def __init__(self, pos):
        super(Explosion, self).__init__(EXPLOSION_IMG, pos)
        self.do(ac.Delay(1) + ac.CallFunc(self.kill))


class Bunker(Actor):
    def __init__(self, x, y):
        super(Bunker, self).__init__("bunker.png", x, y)
        self.hp = 100

    def collide(self, other):
        if isinstance(other, Enemy):
            self.hp -= 10
            other.explode()

            # Check self.is_running to avoid calling kill() when the bunker has already been removed
            if self.hp <= 0 and self.is_running:
                self.kill()


class TurretSlot(object):
    def __init__(self, pos, side_length):
        self.cshape = cm.AARectShape(eu.Vector2(*pos), side_length * 0.5, side_length * 0.5)

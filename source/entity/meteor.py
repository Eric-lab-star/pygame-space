from os.path import join
from typing import ClassVar, Unpack
import pygame
import random

from .entity_option import EntityOptions, MeteorOptions


class Meteor(pygame.sprite.Sprite):
    group: ClassVar[pygame.sprite.Group]
    surf: ClassVar[pygame.Surface]
    path: ClassVar[str] = join("images", "meteor.png")
    w: ClassVar[int]
    h: ClassVar[int]
    _configured: ClassVar[bool] = False
    speed: int = 400
    kill_time: int = 2000

    @classmethod
    def config(cls, **options: Unpack[EntityOptions]):
        cls.group = options["group"]
        cls.surf = pygame.image.load(Meteor.path).convert_alpha()
        cls._configured = True
        cls.w = options["width"]
        cls.h = options["height"]

    def __init__(self, pos):
        if not Meteor._configured:
            raise RuntimeError("must call Meteor.config() ")
        super().__init__(Meteor.group)

        self.image = Meteor.surf
        self.rect: pygame.FRect = self.image.get_frect(center=pos)
        self.spawn_time = pygame.time.get_ticks()
        self.speed = random.randint(300, 600)
        self.direction = pygame.Vector2(random.uniform(-0.5, 0.5), 1)

    @classmethod
    def spawn(cls, n: int):
        for _ in range(n):
            x = random.randint(0, Meteor.w)
            y = random.randint(-200, 0)
            Meteor((x, y))

    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_time >= self.kill_time:
            self.kill()

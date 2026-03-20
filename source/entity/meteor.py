from os.path import join
from typing import ClassVar, Unpack
import pygame

from .entity_option import EntityOptions


class Meteor(pygame.sprite.Sprite):
    group: ClassVar[pygame.sprite.Group]
    surf: ClassVar[pygame.Surface]
    w: ClassVar[int]
    h: ClassVar[int]
    path: ClassVar[str] = join("images", "meteor.png")
    _configured: ClassVar[bool] = False

    @classmethod
    def config(cls, **options: Unpack[EntityOptions]):
        cls.w = options["width"]
        cls.h = options["height"]
        cls.group = options["group"]
        cls.surf = pygame.image.load(Meteor.path).convert_alpha()
        cls._configured = True

    def __init__(self):
        if not Meteor._configured:
            raise RuntimeError("must call Meteor.config() ")
        super().__init__(Meteor.group)
        self.image = Meteor.surf
        self.rect = self.image.get_frect(center=(Meteor.w / 2, Meteor.h / 2))

    def update(self, dt):
        pass

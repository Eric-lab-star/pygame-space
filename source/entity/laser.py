from os.path import join
from typing import ClassVar, Unpack
import pygame

from .entity_option import EntityOptions


class Laser(pygame.sprite.Sprite):
    group: ClassVar[pygame.sprite.Group]
    surf: ClassVar[pygame.Surface]
    w: ClassVar[int]
    h: ClassVar[int]
    path: ClassVar[str] = join("images", "laser.png")
    _configured: ClassVar[bool] = False

    @classmethod
    def config(cls, **options: Unpack[EntityOptions]):
        cls.w = options["width"]
        cls.h = options["height"]
        cls.group = options["group"]
        cls._configured = True

    def __init__(self):
        if not Laser._configured:
            raise RuntimeError("must call Laser.config() ")
        super().__init__(Laser.group)
        self.image = pygame.image.load(Laser.path).convert_alpha()
        self.rect = self.image.get_frect(center=(20, Laser.h / 2))

    def update(self, dt):
        pass

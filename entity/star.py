from typing import ClassVar, Tuple, Unpack
import pygame
from os.path import join
from random import randint

from .entity_option import EntityOptions


class Star(pygame.sprite.Sprite):
    path: ClassVar[str] = join("images", "star.png")
    surf: ClassVar[pygame.Surface]
    h: ClassVar[int]
    w: ClassVar[int]
    group: ClassVar[Tuple[pygame.sprite.Group,...]]
    _configured: ClassVar[bool] = False

    @classmethod
    def config(cls, **options: Unpack[EntityOptions]):
        cls.w = options["width"]
        cls.h = options["height"]
        cls.group = options["group"]
        cls.surf = pygame.image.load(cls.path).convert_alpha()
        cls._configured = True

    def __init__(self):
        if not Star._configured:
            raise RuntimeError("must call Star.config()")
        super().__init__(Star.group)
        self.image = Star.surf
        self.rect = Star.surf.get_frect(center=(randint(0, Star.w), randint(0, Star.h)))

    @classmethod
    def create(cls, n: int):
        for _ in range(n):
            Star()

    def update(self, dt):
        pass

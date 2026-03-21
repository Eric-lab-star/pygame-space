from os import path
from typing import ClassVar, Unpack
import pygame

from .entity_option import EntityOptions


class Background(pygame.sprite.Sprite):
    surf: pygame.surface.Surface
    path = path.join("images", "starry_background.png")
    group: ClassVar[pygame.sprite.Group]
    w: int
    h: int

    @classmethod
    def config(cls, **opts: Unpack[EntityOptions]):
        cls.surf = pygame.transform.scale(
            pygame.image.load(cls.path).convert_alpha(), (opts["width"], opts["height"])
        )
        cls.group: pygame.sprite.Group = opts["group"]
        cls.w = opts["width"]
        cls.h = opts["height"]

    def __init__(self):
        super().__init__(Background.group)
        self.image: pygame.surface.Surface = Background.surf
        self.rect = self.image.get_frect(center=(Background.w / 2, Background.h / 2))

    def update(self, dt):
        self.image
        self.rect

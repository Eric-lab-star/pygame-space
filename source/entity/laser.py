from os.path import join
from typing import ClassVar, Unpack
import pygame

from .entity_option import LaserOptions


class Laser(pygame.sprite.Sprite):
    group: ClassVar[pygame.sprite.Group]
    surf: ClassVar[pygame.Surface]
    path: ClassVar[str] = join("images", "missile1.png")
    _configured: ClassVar[bool] = False

    @classmethod
    def config(cls, **options: Unpack[LaserOptions]):
        cls.group = options["group"]
        cls.surf = pygame.image.load(cls.path).convert_alpha()
        cls._configured = True

    def __init__(self, pos):
        if not Laser._configured:
            raise RuntimeError("must call Laser.config() ")
        super().__init__(Laser.group)
        self.image = Laser.surf
        self.rect: pygame.FRect = self.image.get_frect(midbottom=pos)

    def update(self, dt):
        self.rect.centery -= 400 * dt
        if self.rect.bottom < 0:
            self.kill()



from os.path import join
from typing import ClassVar, Tuple, Unpack
import pygame

from .entity_option import ScoreOptions


class GameOverText(pygame.sprite.Sprite):

    path = join("images", "Galmuri9.ttf")
    font: pygame.font.Font
    group: ClassVar[Tuple[pygame.sprite.Group,...]]
    _configured:ClassVar = False
    display_surface: pygame.surface.Surface
    width: int
    height: int

    @classmethod
    def config(cls, **opts: Unpack[ScoreOptions]):
        cls.group = opts["group"] 
        cls._configured = True
        cls.display_surface =opts["display"] 
        cls.width = opts["width"]
        cls.height = opts["height"]
        cls.font = pygame.font.Font(GameOverText.path, 40)

    def __init__(self, text: str = "", pos: pygame.Vector2 = pygame.Vector2(0,0)):
        if not GameOverText._configured:
            raise RuntimeError("must call HUD.config()")
        super().__init__(GameOverText.group)
        self.text = text
        self.image: pygame.surface.Surface = GameOverText.font.render(text, False, "white")
        self.pos = pos
        self.rect: pygame.FRect = self.image.get_frect(center=pos)

    def update(self, dt, event=None):
        pass

    def draw(self, text:str, pos:pygame.Vector2):
        self.image = GameOverText.font.render(text, False, "white")
        self.rect = self.image.get_frect(center=pos)
        GameOverText.display_surface.blit(self.image, self.rect)



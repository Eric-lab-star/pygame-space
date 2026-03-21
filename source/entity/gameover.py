

from os.path import join
from typing import ClassVar, Tuple, Unpack
import pygame

from .entity_option import ScoreOptions


class GameOver(pygame.sprite.Sprite):

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
        cls.font = pygame.font.Font(GameOver.path, 40)

    def __init__(self, text: str, pos: pygame.Vector2):
        if not GameOver._configured:
            raise RuntimeError("must call HUD.config()")
        super().__init__(GameOver.group)
        self.text = text
        self.image: pygame.surface.Surface = GameOver.font.render(text, False, "white")
        self.pos = pos
        self.rect: pygame.FRect = self.image.get_frect(center=pos)

    def update(self, dt):
        pass

    def draw(self, text:str, pos:pygame.Vector2):
        self.image = GameOver.font.render(text, False, "white")
        self.rect = self.image.get_frect(center=pos)
        GameOver.display_surface.blit(self.image, self.rect)



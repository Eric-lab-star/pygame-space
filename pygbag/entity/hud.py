
from os.path import join
from typing import ClassVar, Tuple, Unpack
import pygame

from .entity_option import ScoreOptions


class Score(pygame.sprite.Sprite):

    path = join("images", "Galmuri9.ttf")
    font: pygame.font.Font
    group: ClassVar[Tuple[pygame.sprite.Group,...]]
    _configured:ClassVar = False
    display_surface: pygame.surface.Surface
    width: int
    height: int
    start_tick:int

    @classmethod
    def config(cls, **opts: Unpack[ScoreOptions]):
        cls.group = opts["group"] 
        cls._configured = True
        cls.display_surface =opts["display"] 
        cls.width = opts["width"]
        cls.height = opts["height"]
        cls.font = pygame.font.Font(Score.path, 40)

    def __init__(self):
        if not Score._configured:
            raise RuntimeError("must call HUD.config()")
        super().__init__(Score.group)
        self.image = Score.font.render(str(0), False, "white")
        self.rect = self.image.get_frect(midbottom=(Score.width/2, Score.height - 25))
        self.t = 0
        self.lastes_score = 0
        self.start_tick = pygame.time.get_ticks()

    def update(self, dt, event=None):
        self.t =  (pygame.time.get_ticks() - self.start_tick) // 1000  
        self.image = Score.font.render(str(self.t), False, "white")
        self.rect = self.image.get_frect(
            midbottom=(Score.width / 2, Score.height - 25)
        )
    def reset(self):
        self.start_tick = pygame.time.get_ticks()
        self.t = 0
        self.image = Score.font.render(str(self.t), False, "white")
        self.rect = self.image.get_frect(
            midbottom=(Score.width / 2, Score.height - 25)
        )


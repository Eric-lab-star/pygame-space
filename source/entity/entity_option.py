from typing import Tuple, TypedDict
import pygame


class EntityOptions(TypedDict):
    width: int
    height: int
    group: Tuple[pygame.sprite.Group,...] 


class LaserOptions(TypedDict):
    group: Tuple[pygame.sprite.Group, ...]


class ScoreOptions(EntityOptions):
    display: pygame.surface.Surface






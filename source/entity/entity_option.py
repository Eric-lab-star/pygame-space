from typing import TypedDict
import pygame


class EntityOptions(TypedDict):
    width: int
    height: int
    group: pygame.sprite.Group

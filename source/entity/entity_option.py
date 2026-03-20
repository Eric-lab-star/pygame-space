from typing import TypedDict
import pygame


class EntityOptions(TypedDict):
    width: int
    height: int
    group: pygame.sprite.Group


class LaserOptions(TypedDict):
    group: pygame.sprite.Group


class MeteorOptions(TypedDict):
    group: pygame.sprite.Group

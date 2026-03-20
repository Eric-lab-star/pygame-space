from typing import ClassVar, Unpack
import pygame
from os.path import join

from .entity_option import EntityOptions


class Player(
    pygame.sprite.Sprite,
):
    w: ClassVar[int]
    h: ClassVar[int]
    group: ClassVar[pygame.sprite.Group]
    path: ClassVar[str] = join("images", "player.png")
    surf: ClassVar[pygame.Surface]
    _configured: ClassVar[bool] = False

    @classmethod
    def config(cls, **options: Unpack[EntityOptions]):
        cls.w = options["width"]
        cls.h = options["height"]
        cls.group = options["group"]
        cls.surf = pygame.image.load(cls.path).convert_alpha()
        cls._configured = True

    def __init__(self):
        if not Player._configured:
            raise RuntimeError("must call Player.config() ")
        super().__init__(Player.group)
        self.image = Player.surf
        self.rect: pygame.FRect = self.image.get_frect(
            center=(Player.w / 2, Player.h / 2)
        )
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 200
        self.can_shoot = True
        self.laser_time = 0
        self.laser_cooldown = 500

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.can_shoot = True

    def handle_laser(self):
        self.laser_timer()
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            print("fire laser")
            self.can_shoot = False
            self.laser_time = pygame.time.get_ticks()

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])

        if self.direction:
            self.direction = self.direction.normalize()
        self.rect.center += self.direction * self.speed * dt

        self.handle_laser()

import pygame
from os.path import join
from random import randint


class Player(
    pygame.sprite.Sprite,
):
    def __init__(self, group: pygame.sprite.Group):
        super().__init__(group)
        self.path = join("images", "player.png")
        self.image: pygame.Surface = pygame.image.load(self.path).convert_alpha()
        self.rect: pygame.FRect = self.image.get_frect(
            center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        )
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 200

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        if self.direction:
            self.direction = self.direction.normalize()
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE]:
            print("fire laser")


class Star(pygame.sprite.Sprite):
    path = join("images", "star.png")
    surf: pygame.Surface

    @classmethod
    def load_image(cls):
        cls.surf = pygame.image.load(cls.path).convert_alpha()

    def __init__(self, group: pygame.sprite.Group):
        super().__init__(group)
        self.rect = Star.surf.get_frect(
            center=(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))
        )

    def update(self, dt):
        pass


# clock
clock = pygame.time.Clock()


pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")

# sprite group


# player
player_path = join("images", "player.png")
player_surf = pygame.image.load(player_path).convert_alpha()
player_frect = player_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2(0, 0)
player_speed = 200

# star

# meteor
meteor_path = join("images", "meteor.png")
meteor_surf = pygame.image.load(meteor_path).convert_alpha()
meteor_frect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# laser
laser_path = join("images", "laser.png")
laser_surf = pygame.image.load(laser_path).convert_alpha()
laser_frect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))
laser_trigger = True


def main():
    running = True
    all_sprites = pygame.sprite.Group()

    Player(all_sprites)
    Star(all_sprites)

    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update(dt)

        # draw bg
        display_surface.fill("darkgray")

        # draw meteor
        display_surface.blit(meteor_surf, meteor_frect)

        # draw laser
        display_surface.blit(laser_surf, laser_frect)

        # draw player
        all_sprites.draw(display_surface)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

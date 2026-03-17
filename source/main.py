import pygame
from os.path import join
from random import randint

# clock

clock = pygame.time.Clock()

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
running = True


# player
player_path = join("images", "player.png")
player_surf = pygame.image.load(player_path).convert_alpha()
player_frect = player_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2(0, 0)
player_speed = 200

# star
star_path = join("images", "star.png")
star_surf = pygame.image.load(star_path).convert_alpha()
star_pos = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(14)]

# meteor
meteor_path = join("images", "meteor.png")
meteor_surf = pygame.image.load(meteor_path).convert_alpha()
meteor_frect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# laser
laser_path = join("images", "laser.png")
laser_surf = pygame.image.load(laser_path).convert_alpha()
laser_frect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))


def main():

    global running
    global player_direction
    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # player inputs
        player_direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        player_direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        player_direction = (
            player_direction.normalize() if player_direction else player_direction
        )
        player_frect.center += player_direction * player_speed * dt

        display_surface.fill("darkgray")

        # draw star
        for pos in star_pos:
            display_surface.blit(star_surf, pos)

        # draw meteor
        display_surface.blit(meteor_surf, meteor_frect)

        # draw laser
        display_surface.blit(laser_surf, laser_frect)

        # draw player
        display_surface.blit(player_surf, player_frect)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

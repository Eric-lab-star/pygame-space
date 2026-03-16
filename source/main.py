import pygame
from os.path import join
from random import randint


pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
running = True


# player surface
player_path = join("images", "player.png")
player_surf = pygame.image.load(player_path).convert_alpha()

# star surface
star_path = join("images", "star.png")
star_surf = pygame.image.load(star_path).convert_alpha()

star_positions = [
    (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(14)
]


def main():

    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.fill("darkgray")

        for cord in star_positions:
            display_surface.blit(star_surf, cord)

        display_surface.blit(player_surf, (100, 150))
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()

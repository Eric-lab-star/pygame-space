import pygame
from entity import Star, Player, Meteor
from entity.laser import Laser
from entity import Background

WINDOW_WIDTH, WINDOW_HEIGHT = 9 * 50, 16 * 50
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()


def config_entities():

    options = {
        "width": WINDOW_WIDTH,
        "height": WINDOW_HEIGHT,
        "group": all_sprites,
    }

    meteor_options = {
        **options,
        "group": (all_sprites, meteor_sprites),
    }

    laser_options = {
        **options,
        "group": (all_sprites, laser_sprites),
    }

    Background.config(**options)
    Star.config(**options)
    Player.config(**options)
    Meteor.config(**meteor_options)
    Laser.config(**laser_options)


def main():
    running = True
    clock = pygame.time.Clock()
    pygame.init()

    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.display.set_caption("Space Shooter")
    config_entities()

    Background()
    Star.create(10)
    Player(display_surface.get_rect())

    # custom meteor event
    meteor_event = pygame.event.custom_type()
    pygame.time.set_timer(meteor_event, 500)

    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == meteor_event:
                Meteor.spawn(2)

        # updates data
        all_sprites.update(dt)

        # draw bg

        # draw
        all_sprites.draw(display_surface)

        # collision test
        pygame.sprite.groupcollide(meteor_sprites, laser_sprites, True, True)

        # updates screen
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

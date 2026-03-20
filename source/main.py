import pygame
from entity import Star, Player, Meteor, Laser


def main():
    running = True
    clock = pygame.time.Clock()
    pygame.init()
    WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Space Shooter")
    all_sprites = pygame.sprite.Group()
    options = {
        "width": WINDOW_WIDTH,
        "height": WINDOW_HEIGHT,
        "group": all_sprites,
    }

    Star.config(**options)
    Player.config(**options)
    Meteor.config(**options)
    Laser.config(**options)

    Star.create(10)
    Meteor()
    Player()

    # custom meteor event
    # meteor_event = pygame.event.custom_type()
    # pygame.time.set_timer(meteor_event, 500)

    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # elif event.type == meteor_event:
            #     print("meteor")

        all_sprites.update(dt)

        # draw bg
        display_surface.fill("darkgray")

        # draw
        all_sprites.draw(display_surface)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

import pygame
from entity import Player, Meteor
from entity.laser import Laser
from entity import Background
from entity import LaserOptions
from entity import Score
from entity import EntityOptions, ScoreOptions
from entity import GameOverText

WINDOW_WIDTH, WINDOW_HEIGHT = 9 * 50, 16 * 50
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()


def config_entities(display: pygame.Surface):
    options: EntityOptions = {
        "width": WINDOW_WIDTH,
        "height": WINDOW_HEIGHT,
        "group": (all_sprites,)
    }

    meteor_options:EntityOptions = {
        **options,
        "group": (all_sprites, meteor_sprites),
    }

    laser_options:LaserOptions = {
        "group": (all_sprites, laser_sprites),
    }

    score_opts: ScoreOptions ={
            **options,
            "display": display,
            }

    Background.config(**options)
    Player.config(**options)
    Meteor.config(**meteor_options)
    Laser.config(**laser_options)
    Score.config(**score_opts)
    GameOverText.config(**score_opts)
    



def main():
    running = True
    game_over = False
    clock = pygame.time.Clock()
    pygame.init()

    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.display.set_caption("Space Shooter")

    config_entities(display_surface)

    bg = Background()
    score = Score()
    game_over_ui = GameOverText()
    game_over_ui.kill()
    player = Player(display_surface.get_rect())

    # custom meteor event
    meteor_event = pygame.event.custom_type()
    pygame.time.set_timer(meteor_event, 500)

    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == meteor_event:
                Meteor.spawn(5)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                if game_over:
                    score.reset()
                    meteor_sprites.empty()
                    laser_sprites.empty()
                    player.reset()
                    game_over_ui.kill()
                    
                    game_over = False
        

        pygame.sprite.groupcollide(meteor_sprites, laser_sprites, True, True)

        if not game_over:
            all_sprites.update(dt)
            if pygame.sprite.spritecollide(player, meteor_sprites, False):
                game_over = True
            all_sprites.draw(display_surface)
        else:
            display_surface.blit(bg.image, bg.rect)
            all_sprites.add(game_over_ui)
            game_over_ui.draw(f"생존시간 {score.t}초", pygame.Vector2(WINDOW_WIDTH /2, (WINDOW_HEIGHT /2) - 80))
            game_over_ui.draw("Game Over", pygame.Vector2(WINDOW_WIDTH /2, WINDOW_HEIGHT /2))
            game_over_ui.draw("R을 누르세요", pygame.Vector2(WINDOW_WIDTH /2, (WINDOW_HEIGHT /2) + 80))

        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

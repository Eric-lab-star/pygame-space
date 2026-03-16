import pygame


pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
running = True

#plain surface
surf = pygame.Surface((100, 150))
surf.fill("orange")

def main():
    
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.fill("darkgray")
        display_surface.blit(surf, (100, 150))
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()

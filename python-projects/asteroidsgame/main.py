import pygame, sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    version = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {version}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    clock = pygame.time.Clock()
    dt = 0

    #game over display on the screen
    def display_game_over(screen):
        screen.fill((0, 0, 0))

        # large main text
        font = pygame.font.Font(None, 64)
        small_font = pygame.font.Font(None, 32)
        text_surface = font.render("GAME OVER!", True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 40))
        screen.blit(text_surface, text_rect)

        # smaller subtitle
        subtitle = small_font.render("You hit an asteroid!", True, (255, 255, 255))
        subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 20))
        screen.blit(subtitle, subtitle_rect)

        pygame.display.flip()


    #game loop
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        updatable.update(dt)

        #check if player is hit
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                display_game_over(screen)
                pygame.time.delay(3000)
                print("\n💥 Collision detected! GAME OVER")
                sys.exit()

        #check if asteroid is destroyed
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.kill()
                    asteroid.split()
                    break


        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()

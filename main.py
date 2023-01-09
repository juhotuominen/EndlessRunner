
import pygame

pygame.init()

clock = pygame.time.Clock()

width = 800
height = 600

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("EndlessRunner")

player_img = pygame.image.load("guy.png")

red = (255, 0, 0)

font_style = pygame.font.SysFont("Arial", 25)


def message(msg, color, mx, my):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [mx, my])


def game_loop():
    running = True


    isJump = False
    y_gravity = 1
    jump_height = 20
    y_velocity = jump_height
    x = 350
    y = 400

    isJump = False

    while running:
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                        running = False
                if event.key == pygame.K_c:
                    game_loop()


        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            isJump = True
        
        if isJump:
            y -= y_velocity
            y_velocity -= y_gravity
            if y_velocity < -jump_height:
                isJump = False
                y_velocity = jump_height

        display.fill((0,0,0))
        message("Press Q to quit!", red, 10, 10)
        display.blit(player_img, (x, y))
        pygame.display.update()
        clock.tick(60)

game_loop()

        
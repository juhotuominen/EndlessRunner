
import pygame
import random

pygame.init()

clock = pygame.time.Clock()

width = 800
height = 600

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("EndlessRunner")

player_img = pygame.image.load("images/guy.png")

red = (255, 0, 0)
green = (0, 50, 0)
blue = (0, 0, 50)
yellow = (255, 255, 0)

font_style = pygame.font.SysFont("Arial", 25)

def message(msg, color, mx, my):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [mx, my])


def game_loop():
    running = True

    isJump = False
    y_gravity = 1
    jump_height = 15
    y_velocity = jump_height
    x = 350
    y = 405
    dx=5
    score = 0
    

    obstacles = [800, 1200, 1400, 1600, 1800]
    obstacle_speed = 2
    active = True
    isJump = False

    while running:
        score_display = font_style.render(str(score), True, yellow)
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                if event.key == pygame.K_c:
                    game_loop()
                    return 0
                    

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and active == True:
            isJump = True
        if keys[pygame.K_LEFT] and active == True:
                x -= dx
        if keys[pygame.K_RIGHT] and active == True:
                x += dx


        if isJump:
            y -= y_velocity
            y_velocity -= y_gravity
            if y_velocity < -jump_height:
                isJump = False
                y_velocity = jump_height

        display.fill((10, 10, 10))

        message("Score: ", yellow, 20, 10)
        display.blit(score_display, (100, 10))

        pygame.draw.rect(display, green, pygame.Rect(0, 447, 800, 10))
        obstacle0 = pygame.draw.rect(display, blue, pygame.Rect(obstacles[0], 406, 20, 40))
        obstacle1 = pygame.draw.rect(display, blue, pygame.Rect(obstacles[1], 406, 20, 40))
        obstacle2 = pygame.draw.rect(display, blue, pygame.Rect(obstacles[2], 406, 20, 40))
        obstacle3 = pygame.draw.rect(display, blue, pygame.Rect(obstacles[3], 406, 20, 40))
        obstacle4 = pygame.draw.rect(display, blue, pygame.Rect(obstacles[4], 406, 20, 40))
        player = pygame.Rect(x, y, 20, 40)

        for i in range(len(obstacles)):
            if active:
                obstacles[i] -= obstacle_speed
                if obstacles[i] < 0:
                    obstacles[i] = random.uniform(1000, 1600)
                    score += 1
                if (player.colliderect(obstacle0) or player.colliderect(obstacle1)
                    or player.colliderect(obstacle2) or player.colliderect(obstacle3) or player.colliderect(obstacle4)):
                    active = False
            else:
                message("Game Over, press Q to quit or C to play again", yellow, 70, 90)
        
        display.blit(player_img, (x, y))
        pygame.display.update()
        clock.tick(60)

game_loop()

        
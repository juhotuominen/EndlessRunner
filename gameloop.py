import pygame
import random
import images
import color
import math

pygame.init()

clock = pygame.time.Clock()
width = 1280
height = 720
display = pygame.display.set_mode((width, height))
font_style = pygame.font.SysFont("Arial", 25)


def message(msg, color, mx, my):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [mx, my])

def game_loop():
    running = True

    y_gravity = 1
    jump_height = 15
    y_velocity = jump_height
    x = 350
    y = 550
    dx=5
    score = 0
    
    obstacles = [800, 1200, 1400, 1600, 1800]
    obstacle_speed = 2
    active = True
    isJump = False

    #GAME LOOP
    while running:
        score_display = font_style.render(str(score), True, color.red)
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

        
        display.blit(images.background_img, (0,0))
        message("Score: ", color.black, 20, 10)
        display.blit(score_display, (100, 10))
        
        
        obstacle0 = pygame.Rect(obstacles[0], 530, 20, 60)
        obstacle1 = pygame.Rect(obstacles[1], 550, 20, 40)
        obstacle2 = pygame.Rect(obstacles[2], 570, 20, 20)
        obstacle3 = pygame.Rect(obstacles[3], 560, 20, 30)
        obstacle4 = pygame.Rect(obstacles[4], 540, 20, 50)
        player = pygame.Rect(x, y, 20, 40)

        i=random.randint(0, 4)
        for i in range(len(obstacles)):
            if active:
                obstacles[i] -= obstacle_speed
                if obstacles[i] < 0:
                    obstacles[i] = random.uniform(1300, 1900)
                    score += 1
                if (player.colliderect(obstacle0) or player.colliderect(obstacle1)
                    or player.colliderect(obstacle2) or player.colliderect(obstacle3) or player.colliderect(obstacle4)):
                    active = False
            else:
                message("Game Over", color.red, 400, 350)
                message("press Q to quit to menu or C to play again", color.black, 400, 400)
        display.blit(images.zombie_60_img, (obstacles[0], 530))
        display.blit(images.zombie_40_img, (obstacles[1], 550))
        display.blit(images.zombie_20_img, (obstacles[2], 570))
        display.blit(images.zombie_30_img, (obstacles[3], 560))
        display.blit(images.zombie_50_img, (obstacles[4], 540))
        display.blit(images.player_img, (x, y))
        pygame.display.update()
        clock.tick(60)
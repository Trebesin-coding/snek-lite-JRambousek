import pygame
import random
from spritesheet import *
from stats import *

pygame.init()
width = 1920
height = 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("HaHad")

spritesheet = Spritesheet("snek-lite-JRambousek/IMGJSON/had.png")
snake = spritesheet.get_sprite(0, 0, s_size, s_size).convert_alpha()
red_coin = spritesheet.get_sprite(38, 0, s_size, s_size).convert_alpha()
green_coin = spritesheet.get_sprite(76, 0, s_size, s_size).convert_alpha()
gold_coin = spritesheet.get_sprite(114, 0, s_size, s_size).convert_alpha()

time = 0
classic_font = pygame.font.Font("snek-lite-JRambousek/FONT/PixelifySans-Regular.ttf", 40)
win_font = pygame.font.Font("snek-lite-JRambousek/FONT/PixelifySans-Regular.ttf", 200)
score = classic_font.render(f"SCORE: {score_count}", True, (0, 0, 0))
timeos = classic_font.render(f"TIME: {time}", True, (0, 0, 0))
win = win_font.render("WIN", True, (0, 0, 0))
leave = classic_font.render("Press ESC to exit", True, (0, 0, 0))

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_w]:
        snake_y -= snake_speed
    if keys[pygame.K_s]:
        snake_y += snake_speed
    if keys[pygame.K_a]:        
        snake_x -= snake_speed
    if keys[pygame.K_d]:    
        snake_x += snake_speed
        
    snake_rect = snake.get_rect(center=(snake_x, snake_y))
    red_coin_rect = red_coin.get_rect(center=(red_coin_x, red_coin_y))
    green_coin_rect = green_coin.get_rect(center=(green_coin_x, green_coin_y))
    gold_coin_rect = gold_coin.get_rect(center=(gold_coin_x, gold_coin_y))

    if snake_rect.colliderect(red_coin_rect):
        red_coin_x = random.randint(0, 1820)
        red_coin_y = random.randint(0, 980)
        score_count += 1
        score = classic_font.render(f"SCORE: {score_count}", True, (0, 0, 0))
    
    green_current_timer = pygame.time.get_ticks()
    if green_current_timer - green_start_timer > 3000 and picked_green_coin == True:
        picked_green_coin = False
        green_coin_x = random.randint(0, 1820)
        green_coin_y = random.randint(0, 980)
        green_start_timer = green_current_timer
    elif green_current_timer - green_start_timer > 2000 and picked_green_coin == False:
        green_coin_x = out     
    if snake_rect.colliderect(green_coin_rect):
        green_coin_x = out
        score_count += 100
        picked_green_coin = True
        score = classic_font.render(f"SCORE: {score_count}", True, (0, 0, 0))
    
    gold_current_timer = pygame.time.get_ticks()
    if gold_current_timer - gold_start_timer > random_gold and gold_coin_respawn == True:   
        gold_coin_x = random.randint(0, 1820)
        gold_coin_y = random.randint(0, 980)
        gold_start_timer = gold_current_timer
        gold_coin_respawn = False
    elif gold_current_timer - gold_start_timer > 2000 and gold_coin_respawn == False:
        gold_coin_x = out
    if snake_rect.colliderect(gold_coin_rect):
        gold_coin_x = out
        score_count += 1000
        game_won = True
        gold_coin_respawn = False
        score = classic_font.render(f"SCORE: {score_count}", True, (0, 0, 0))
    
    if game_won == True:
        snake_speed = 0
        win_x = 758
        win_y = 300
        leave_x = 770
        leave_y = 500
        red_coin_x = out
        green_coin_x = out
        win = win_font.render("WIN", True, (0, 0, 0))
        leave = classic_font.render("Press ESC to exit", True, (0, 0, 0))
    elif game_won == False:
        time = pygame.time.get_ticks() // 1000
        timeos = classic_font.render(f"TIME: {time}", True, (0, 0, 0))
            
    screen.fill("lightgreen")
    screen.blit(red_coin, (red_coin_x, red_coin_y))
    screen.blit(green_coin, (green_coin_x, green_coin_y))
    screen.blit(gold_coin, (gold_coin_x, gold_coin_y))
    screen.blit(snake, (snake_x, snake_y))
    screen.blit(score, (1650, 20))
    screen.blit(timeos, (120, 20))
    screen.blit(win, (win_x, win_y))
    screen.blit(leave, (leave_x, leave_y))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
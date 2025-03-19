import random

out = 4000

score_count = 0
snake_speed = 7
snake_x = 900
snake_y = 500
game_won = False

red_coin_x = random.randint(0, 1820)
red_coin_y = random.randint(0, 980)

green_coin_x = out
green_coin_y = out
green_start_timer = 0
green_current_timer = 0
picked_green_coin = True

gold_coin_x = out
gold_coin_y = out
gold_start_timer = 0
gold_current_timer = 0
random_gold = random.randint(10000, 30000)
randomgone = random_gold + 2000
gold_coin_respawn = True

win_x = out
win_y = out

leave_x = out
leave_y = out
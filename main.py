import pygame as pg
import random as rd

pg.init()
disp = pg.display.set_mode((800, 480))
pg.display.set_caption("Змейка")
pg.display.update()

red = 255, 0, 0
black = 0, 0, 0
green = 0, 255, 0
direction = "right"

game_over = False
clock = pg.time.Clock()
font = pg.font.Font(None, 40)

x = 200
y = 320
apple_x = 400
apple_y = 320
score = 0
snake = [[x, y]]


while not game_over:
    clock.tick(5)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                direction = "left"
            if event.key == pg.K_d:
                direction = "right"
            if event.key == pg.K_w:
                direction = "up"
            if event.key == pg.K_s:
                direction = "down"

    if direction == "left":
        x -= 40
    if direction == "right":
        x += 40
    if direction == "up":
        y -=40
    if direction == "down":
        y += 40

    for i in range(len(snake) - 1):
        snake[i] = snake[i + 1]
    snake[-1] = [x, y]

    if x == apple_x and y == apple_y:
        snake = [snake[0]] + snake
        score += 1
        while [apple_x, apple_y] in snake:
            apple_x = rd.randint(1, 11) * 40
            apple_y = rd.randint(1, 11) * 40


    disp.fill(black)
    for i in range(len(snake)):
        pg.draw.rect(disp, green, [snake[i][0], snake[i][1], 40,40])
    pg.draw.rect(disp, (red), [apple_x, apple_y, 40, 40])
    pg.display.update()

    message = font.render("cчет: " + str(score), True, (255, 255, 255))
    disp.blit(message, [0, 0])
    pg.display.update()
pg.quit()
quit()
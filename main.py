import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)

background_img = pygame.image.load("img/background.jpg")

target_img = pygame.image.load("img/target.png")
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

target_speed_x = random.randint(-2, 2)
target_speed_y = random.randint(-2, 2)

color = (random.randint(a:=0, b:=255), random.randint(a:=0, b:=255), random.randint(a:=0, b:=255))

score = 0
lives = 3

running = True
game_over = False

while running:
    screen.blit(background_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            else:
                lives -= 1
                if lives == 0:
                    game_over = True


    target_x += target_speed_x
    target_y += target_speed_y

    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    screen.blit(target_img, (target_x, target_y))

    font = pygame.font.SysFont(None, 36)
    lives_text = font.render(f'Жизни: {lives}', True, ("white"))
    score_text = font.render(f'Очки: {score}', True, ('white'))
    screen.blit(lives_text, (SCREEN_WIDTH - 150, 10))
    screen.blit(score_text, (10, 10))

    if game_over:
        game_over_text = font.render('Game Over', True, (255, 0, 0))
        final_score_text = font.render(f'Ваши очки: {score}', True, (255, 0, 0))
        screen.blit(game_over_text, (
        SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
        screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

    pygame.display.update()

pygame.quit()
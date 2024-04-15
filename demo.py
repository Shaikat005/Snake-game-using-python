import pygame
import random

pygame.init()

# setting the game window:
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

clock = pygame.time.Clock()

def show_game_over():
    font_style = pygame.font.SysFont(None, 50)
    game_over_text = font_style.render("Game Over", True, white)
    window.blit(game_over_text, (window_width // 2 - 100, window_height // 2 - 50))
    pygame.display.update()
    pygame.time.wait(500)  # Pause for 2 seconds before showing restart option
    restart_text = font_style.render("Press R to restart", True, white)
    window.blit(restart_text, (window_width // 2 - 140, window_height // 2 + 50))
    pygame.display.update()

    quit_text = font_style.render("Press Q to quit the game", True, white)
    window.blit(quit_text, (window_width // 2 - 190, window_height // 2 + 100))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # Signal to restart the game
                elif event.key == pygame.K_q:
                    pygame.quit()  # Quit the game

def restart_game():
    global game_over, score, x1, y1, x1_change, y1_change, snake_body, length_of_snake, foodx, foody
    game_over = False
    score = 0
    x1 = window_width // 2
    y1 = window_height // 2
    x1_change = 0
    y1_change = 0
    snake_body = []
    length_of_snake = 1
    foodx = round(random.randrange(0, window_width - 10) / 10) * 10.0
    foody = round(random.randrange(0, window_height - 10) / 10) * 10.0

game_over = False
score = 0
x1 = window_width // 2
y1 = window_height // 2
x1_change = 0
y1_change = 0
snake_body = []
length_of_snake = 1
foodx = round(random.randrange(0, window_width - 10) / 10) * 10.0
foody = round(random.randrange(0, window_height - 10) / 10) * 10.0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # check for arrow keys pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
            elif event.key == pygame.K_q:
                pygame.quit()  # Quit the game

    x1 += x1_change
    y1 += y1_change

    if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
        game_over = show_game_over()  # Call the function to show "Game Over" and prompt restart or quit
        if game_over:  # Check if the game should be restarted
            restart_game()

    window.fill(black)

    snake_head = [x1, y1]
    snake_body.append(snake_head)

    if len(snake_body) > length_of_snake:
        del snake_body[0]

    for segment in snake_body[:-1]:
        if segment == snake_head:
            game_over = show_game_over()  # Call the function to show "Game Over" and prompt restart or quit
            if game_over:  # Check if the game should be restarted
                restart_game()

    font_style = pygame.font.SysFont(None, 50)
    score_text = font_style.render("Score: " + str(score), True, white)
    window.blit(score_text, (10, 10))

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, window_width - 10) / 10) * 10.0
        foody = round(random.randrange(0, window_height - 10) / 10) * 10.0
        length_of_snake += 1
        score += 1

    pygame.draw.rect(window, red, [foodx, foody, 10, 10])

    # Draw the snake's head in red color
    pygame.draw.rect(window, red, [x1, y1, 10, 10])

    for segment in snake_body:
        pygame.draw.rect(window, white, [segment[0], segment[1], 10, 10])

    pygame.display.update()
    clock.tick(15)

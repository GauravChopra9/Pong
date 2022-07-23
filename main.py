import sys
import pygame
import pygame.draw

print('Welcome to my first game called Pong! We are going to use Pygame')

# Initializing the game
pygame.init()
clock = pygame.time.Clock()

# Setting up the game
WIDTH = 1300
HEIGHT = 780
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Setting up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setting up velocities
velocity_x = 6
velocity_y = 6

player1_velocity = 0
opponent_velocity = 0


ball = pygame.Rect(WIDTH / 2 - 10, HEIGHT / 2 - 10, 20, 20)
player1 = pygame.Rect(WIDTH - 15, HEIGHT / 2 - 75, 30, 150)
opponent = pygame.Rect(0 - 15, HEIGHT / 2 - 75, 30, 150)
dividing_line = pygame.Rect(WIDTH/2 - 1, 0, 2, HEIGHT)

def draw():
    game_display.fill(BLACK)
    pygame.draw.ellipse(game_display, WHITE, ball)
    pygame.draw.rect(game_display, WHITE, player1)
    pygame.draw.rect(game_display, WHITE, opponent)
    pygame.draw.rect(game_display, WHITE, dividing_line)

def ball_movement():
    global ball
    global velocity_x
    global velocity_y
    ball.x = ball.x + velocity_x
    ball.y = ball.y + velocity_y

    if ball.left <= 0 or ball.right >= WIDTH:
        velocity_x = velocity_x * -1

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        velocity_y = velocity_y * -1

    # Accounting for collisions
    if ball.colliderect(player1) or ball.colliderect(opponent):
        velocity_x = velocity_x * -1
        velocity_y = velocity_y * -1

    if ball.left <= 0 or ball.right >= WIDTH:
        ball = pygame.Rect(WIDTH / 2 - 10, HEIGHT / 2 - 10, 20, 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            sys.exit()

        # Accounting for player1 movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_velocity = 5

            if event.key == pygame.K_UP:
                player1_velocity = -5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_velocity = 0

            if event.key == pygame.K_UP:
                player1_velocity = 0

        # Accounting for opponent movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                opponent_velocity = 5

            if event.key == pygame.K_e:
                opponent_velocity = -5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                opponent_velocity = 0

            if event.key == pygame.K_e:
                opponent_velocity = 0

    player1.y = player1.y + player1_velocity
    if player1.bottom >= HEIGHT:
        player1.bottom = HEIGHT

    if player1.top <= 0:
        player1.top = 0

    opponent.y = opponent.y + opponent_velocity
    if opponent.bottom >= HEIGHT:
        opponent.bottom = HEIGHT

    if opponent.top <= 0:
        opponent.top = 0

    # Accounting for ball movements start here
    ball_movement()
    draw()

    # Updating the window
    clock.tick(60)
    pygame.display.flip()









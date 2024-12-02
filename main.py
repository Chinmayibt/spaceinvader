import pygame
import random#for placement of enemy

# initialize  pygame to use all the tools
pygame.init()

# create a screen
screen = pygame.display.set_mode((800, 600))

# title and icon(icon is 32*32px)
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# palyer
player_img = pygame.image.load('shoot.png')
player_x = 360  # exactly the middle of the screen
player_y = 480  # slightly above the bottom
player_x_change = 0

# enemy
enemy_img = pygame.image.load('ufo.png')
enemy_x = random.randint(0,500)  # exactly the middle of the screen
enemy_y = random.randint(0,50) # slightly above the bottom
enemy_x_change = 0


def player(x, y):
    screen.blit(player_img, (player_x, player_y))  # to drawing the img on the screen


def enemy(x, y):
    screen.blit(enemy_img, (enemy_x, enemy_y))  # to drawing the img on the screen


# for closing the window(if u don't use a  while loop the window get hung and u cannot come out of the game)
running = True
while running:

    # rbg
    screen.fill((0, 0, 0))
    # player_x -= 0.1
    # player_y -= 0.1 movement along y-axis ie up and down
    for event in pygame.event.get():  # get is a method
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed right of left
        if event.type == pygame.KEYDOWN:
            print("A key is pressed")
            if event.key == pygame.K_LEFT:
                player_x_change = -0.2
                print("LEFT")+
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.2
                print("RIGHT")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
                print("keystroke is released")


    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736


    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pygame.display.update()  # to update the color of the screen

###### NEW: lets this file run from the ICS4U folder or the demo folder.
import os
os.chdir(os.path.dirname(__file__))
###### END NEW.


import pygame
import char_item_copy as ci
framex = 1200
framey = 800
pygame.init()
screen = pygame.display.set_mode((framex, framey))
clock = pygame.time.Clock()
BLACK = (10, 10, 10)
WHITE = (230, 230, 230)
GRAY = (90, 90, 90)
GREEN = (80, 180, 80)
YELLOW = (200, 200, 0)
RED = (180, 50, 50)
BLUE = (60, 120, 210)
left_key = pygame.K_a
right_key = pygame.K_d
jump_key = pygame.K_w
move_unit = 7
gravity = 1
jump_power = -18
max_fall_speed = 18

start_location = (90, 650)
user1 = ci.player("User 1", "knight", 1, 100, 0, start_location, 0, ci.knight_img)
user1.rect.midbottom = start_location
user1.on_ground = False

#future tmx
platforms = [
    pygame.Rect(0, 720, 1200, 80),
    pygame.Rect(150, 620, 180, 30),
    pygame.Rect(420, 540, 180, 30),
    pygame.Rect(700, 455, 180, 30),
    pygame.Rect(950, 365, 180, 30),
]
hazards = [
    ("reset", pygame.Rect(330, 690, 220, 30), BLUE),
    ("fail", pygame.Rect(720, 690, 220, 30), RED),
]
finish_rect = pygame.Rect(1060, 190, 80, 80)


def draw_level():
    screen.fill(BLACK)
    for platform in platforms:
        pygame.draw.rect(screen, GRAY, platform)
    for hazard in hazards:
        pygame.draw.rect(screen, hazard[2], hazard[1])
    pygame.draw.rect(screen, GREEN, finish_rect)



def move_user(user, keys):
    user.velocity.x = 0
    if keys[left_key]:
        user.velocity.x = -move_unit
        user.image = user.image_set["Walk"][0]
    elif keys[right_key]:
        user.velocity.x = move_unit
        user.image = user.image_set["Walk"][0]
    else:
        user.image = user.image_set["Jump"][0]
    if keys[jump_key] and user.on_ground:
        user.velocity.y = jump_power
        user.on_ground = False
    user.velocity.y += gravity
    if user.velocity.y > max_fall_speed:
        user.velocity.y = max_fall_speed




def collision_check(user, platform_list):
    user.rect.x += user.velocity.x
    for platform in platform_list:
        if user.rect.colliderect(platform):
            if user.velocity.x > 0:
                user.rect.right = platform.left
            elif user.velocity.x < 0:
                user.rect.left = platform.right
    user.on_ground = False
    user.rect.y += user.velocity.y
    for platform in platform_list:
        if user.rect.colliderect(platform):
            if user.velocity.y > 0:
                user.rect.bottom = platform.top
                user.velocity.y = 0
                user.on_ground = True
            elif user.velocity.y < 0:
                user.rect.top = platform.bottom
                user.velocity.y = 0



def reset_user(user):
    user.rect.midbottom = start_location
    user.velocity = pygame.math.Vector2(0, 0)
    user.on_ground = False



def fail_check(user):
    if user.rect.top > framey:
        print("Side stage failed: fell")
        return True

    for hazard in hazards:
        if user.rect.colliderect(hazard[1]):
            if hazard[0] == "reset":
                print("Side stage reset")
                reset_user(user)
                return False
            if hazard[0] == "fail":
                print("Side stage failed")
                return True

    return False


def win_check(user):
    if user.rect.colliderect(finish_rect):
        return True
    return False


game_active = True
side_stage_clear = False

while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False

    keys = pygame.key.get_pressed()
    move_user(user1, keys)
    collision_check(user1, platforms)
    ###### NEW: side stage can fail before it can clear.
    if fail_check(user1):
        game_active = False
    ###### END NEW.

    if win_check(user1):
        side_stage_clear = True
        game_active = False

    draw_level()
    screen.blit(user1.image, user1.rect)

    pygame.display.update()
    clock.tick(60)

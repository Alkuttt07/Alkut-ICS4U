import os
os.chdir(os.path.dirname(__file__))
import pygame
import pytmx
import char_item_copy as ci



framex = 1200
framey = 800
pygame.init()
screen = pygame.display.set_mode((framex, framey))
clock = pygame.time.Clock()
BLACK = (10, 10, 10)
OUTLINE = (25, 25, 25)



bunker_full_background_img = pygame.image.load("side_assets\\bunker_full_background_ai.png").convert_alpha()
bunker_full_background_img = pygame.transform.scale(bunker_full_background_img, (framex, framey))
bunker_platform_img = pygame.image.load("side_assets\\bunker_platform.png").convert_alpha()

puzzle_bridge_img = pygame.image.load("side_assets\\puzzle_bridge.png").convert_alpha()
button_img = pygame.image.load("side_assets\\button.png").convert_alpha()
button_pressed_img = pygame.image.load("side_assets\\button_pressed.png").convert_alpha()

blue_trap_img = pygame.image.load("side_assets\\blue_reset_trap.png").convert_alpha()
red_trap_img = pygame.image.load("side_assets\\red_fail_trap.png").convert_alpha()
exit_gate_img = pygame.image.load("side_assets\\exit_gate.png").convert_alpha()

exit_gate_open_img = pygame.image.load("side_assets\\exit_gate_open.png").convert_alpha()
gold_key_img = pygame.image.load("side_assets\\gold_key.png").convert_alpha()


left_key = pygame.K_a
right_key = pygame.K_d
jump_key = pygame.K_w


move_unit = 4.7
gravity = 1
jump_power = -14
max_fall_speed = 8


tiled_map = pytmx.load_pygame("side_stage.tmx", pixelalpha=True)
background = pygame.Surface((framex, framey)).convert_alpha()
background.fill((0, 0, 0, 0))


def draw_image_layers(map):
    global background

    for layer in map.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile_image = map.get_tile_image_by_gid(gid)
                if tile_image:
                    pixel_x = x * map.tilewidth
                    pixel_y = y * map.tileheight
                    background.blit(tile_image, (pixel_x, pixel_y))


def object_rects(layer_name):
    rects = []
    for obj in tiled_map.get_layer_by_name(layer_name):
        rects.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
    return rects


def draw_tiled_image(surface, image, rect):
    for x in range(rect.left, rect.right, image.get_width()):
        for y in range(rect.top, rect.bottom, image.get_height()):
            piece_width = min(image.get_width(), rect.right - x)
            piece_height = min(image.get_height(), rect.bottom - y)
            surface.blit(image, (x, y), (0, 0, piece_width, piece_height))


def draw_scaled_image(surface, image, rect):
    scaled_image = pygame.transform.scale(image, (rect.width, rect.height))
    surface.blit(scaled_image, rect)


def scale_image_set(image_set, scale):
    smaller_image_set = {}
    for action in image_set:
        smaller_image_set[action] = []
        for image in image_set[action]:
            width = int(image.get_width() * scale)
            height = int(image.get_height() * scale)
            smaller_image_set[action].append(pygame.transform.scale(image, (width, height)))
    return smaller_image_set


platforms = object_rects("Platforms")
blue_traps = object_rects("Blue Traps")
red_traps = object_rects("Red Traps")
button_rects = object_rects("Buttons")
bridge_platforms = object_rects("Bridge Platforms")
button_pressed = False
button_rects_2 = object_rects("Buttons 2")
bridge_platforms_2 = object_rects("Bridge Platforms 2")
button_pressed_2 = False

spawn = tiled_map.get_object_by_name("Start")
start_location = (spawn.x, spawn.y)

entrance = tiled_map.get_object_by_name("Entrance")
entrance_rect = pygame.Rect(entrance.x, entrance.y, entrance.width, entrance.height)

finish = tiled_map.get_object_by_name("Finish")
finish_rect = pygame.Rect(finish.x, finish.y, finish.width, finish.height)

key = tiled_map.get_object_by_name("Key")
key_rect = pygame.Rect(key.x, key.y, key.width, key.height)
key_collected = False

draw_image_layers(tiled_map)


sideview_knight_img = scale_image_set(ci.knight_img, 0.42)
user1 = ci.player("User 1", "knight", 1, 100, 0, start_location, 0, sideview_knight_img)
user1.rect.midbottom = start_location
user1.on_ground = False


def draw_level():
    global key_collected, button_pressed, button_pressed_2

    screen.fill(BLACK)
    screen.blit(bunker_full_background_img, (0, 0))
    screen.blit(background, (0, 0))

    for platform in platforms:
        draw_tiled_image(screen, bunker_platform_img, platform)
        pygame.draw.rect(screen, OUTLINE, platform, 2)

    if button_pressed:
        for platform in bridge_platforms:
            draw_tiled_image(screen, puzzle_bridge_img, platform)
            pygame.draw.rect(screen, OUTLINE, platform, 2)
    if button_pressed_2:
        for platform in bridge_platforms_2:
            draw_tiled_image(screen, puzzle_bridge_img, platform)
            pygame.draw.rect(screen, OUTLINE, platform, 2)

    for button in button_rects:
        if button_pressed:
            screen.blit(button_pressed_img, button)
        else:
            screen.blit(button_img, button)
    for button in button_rects_2:
        if button_pressed_2:
            screen.blit(button_pressed_img, button)
        else:
            screen.blit(button_img, button)

    for trap in blue_traps:
        draw_tiled_image(screen, blue_trap_img, trap)

    for trap in red_traps:
        draw_tiled_image(screen, red_trap_img, trap)

    draw_scaled_image(screen, exit_gate_img, entrance_rect)

    if not key_collected:
        screen.blit(gold_key_img, key_rect)

    if key_collected:
        draw_scaled_image(screen, exit_gate_open_img, finish_rect)
    else:
        draw_scaled_image(screen, exit_gate_img, finish_rect)


def active_platforms():
    current_platforms = platforms[:]
    if button_pressed:
        current_platforms += bridge_platforms
    if button_pressed_2:
        current_platforms += bridge_platforms_2
    return current_platforms


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
    global key_collected, button_pressed, button_pressed_2

    user.rect.midbottom = start_location
    user.velocity = pygame.math.Vector2(0, 0)
    user.on_ground = False
    key_collected = False
    button_pressed = False
    button_pressed_2 = False


def fail_check(user):
    if user.rect.top > framey:
        print("Side stage failed: fell")
        return True

    for trap in blue_traps:
        if user.rect.colliderect(trap):
            print("Side stage reset")
            reset_user(user)
            return False

    for trap in red_traps:
        if user.rect.colliderect(trap):
            print("Side stage failed")
            return True

    return False


def button_check(user):
    global button_pressed, button_pressed_2

    for button in button_rects:
        if user.rect.colliderect(button):
            button_pressed = True

    for button in button_rects_2:
        if user.rect.colliderect(button):
            button_pressed_2 = True


def key_check(user):
    global key_collected

    if not key_collected and user.rect.colliderect(key_rect):
        key_collected = True
        print("Side stage key collected")


def win_check(user):
    if key_collected and user.rect.colliderect(finish_rect):
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
    collision_check(user1, active_platforms())

    if fail_check(user1):
        game_active = False

    button_check(user1)

    key_check(user1)

    if win_check(user1):
        side_stage_clear = True
        game_active = False

    draw_level()
    screen.blit(user1.image, user1.rect)

    pygame.display.update()
    clock.tick(60)

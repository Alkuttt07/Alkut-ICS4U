###### NEW: lets this file run from the ICS4U folder or the demo folder.
import os
os.chdir(os.path.dirname(__file__))
###### END NEW.


###### COPIED FROM stage1.py / stage2.py: pygame, pytmx, and demo character imports.
import pygame
import pytmx
import char_item_copy as ci
###### END COPIED.


###### COPIED FROM stage1.py / stage2.py: same window size names and pygame setup.
framex = 1200
framey = 800
pygame.init()
screen = pygame.display.set_mode((framex, framey))
###### END COPIED.


###### NEW: side-stage colors and clock.
clock = pygame.time.Clock()
BLACK = (10, 10, 10)
OUTLINE = (25, 25, 25)
###### END NEW.


###### MODIFIED: use the stronger pixel-art grey bunker background with warm lower light.
bunker_full_background_img = pygame.image.load("side_assets\\bunker_full_background_ai.png").convert_alpha()
bunker_full_background_img = pygame.transform.scale(bunker_full_background_img, (framex, framey))
bunker_platform_img = pygame.image.load("side_assets\\bunker_platform.png").convert_alpha()
###### NEW: puzzle bridge and pressure button images for the side-stage puzzle.
puzzle_bridge_img = pygame.image.load("side_assets\\puzzle_bridge.png").convert_alpha()
button_img = pygame.image.load("side_assets\\button.png").convert_alpha()
button_pressed_img = pygame.image.load("side_assets\\button_pressed.png").convert_alpha()
###### END NEW.
blue_trap_img = pygame.image.load("side_assets\\blue_reset_trap.png").convert_alpha()
red_trap_img = pygame.image.load("side_assets\\red_fail_trap.png").convert_alpha()
exit_gate_img = pygame.image.load("side_assets\\exit_gate.png").convert_alpha()
###### NEW: open gate image appears after the key is collected.
exit_gate_open_img = pygame.image.load("side_assets\\exit_gate_open.png").convert_alpha()
###### END NEW.
###### NEW: one key is required before the player can clear the side stage.
gold_key_img = pygame.image.load("side_assets\\gold_key.png").convert_alpha()
###### END NEW.
###### END MODIFIED.


###### MODIFIED FROM stage1.py / stage2.py: same key style, but sideview only uses left, right, and jump.
left_key = pygame.K_a
right_key = pygame.K_d
jump_key = pygame.K_w
###### END MODIFIED.


###### NEW: sideview gravity settings.
move_unit = 6
gravity = 1
jump_power = -17
max_fall_speed = 10
###### END NEW.


###### COPIED FROM stage1.py / stage2.py: load a Tiled map and prepare the background surface.
tiled_map = pytmx.load_pygame("side_stage.tmx", pixelalpha=True)
background = pygame.Surface((framex, framey)).convert_alpha()
###### MODIFIED: keep the TMX tile layer transparent so it does not cover the full background PNG.
background.fill((0, 0, 0, 0))
###### END MODIFIED.
###### END COPIED.


###### COPIED FROM stage2.py: draw visible tile layers from a Tiled map.
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
###### END COPIED.


###### NEW: convert a Tiled object layer into pygame Rects.
def object_rects(layer_name):
    rects = []
    for obj in tiled_map.get_layer_by_name(layer_name):
        rects.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
    return rects
###### END NEW.


###### MODIFIED: draw one small PNG repeatedly inside a rectangle without spilling past the right or bottom edge.
def draw_tiled_image(surface, image, rect):
    for x in range(rect.left, rect.right, image.get_width()):
        for y in range(rect.top, rect.bottom, image.get_height()):
            piece_width = min(image.get_width(), rect.right - x)
            piece_height = min(image.get_height(), rect.bottom - y)
            surface.blit(image, (x, y), (0, 0, piece_width, piece_height))
###### END MODIFIED.


###### NEW: make a smaller player image set only for the side-scroller stage.
def scale_image_set(image_set, scale):
    smaller_image_set = {}
    for action in image_set:
        smaller_image_set[action] = []
        for image in image_set[action]:
            width = int(image.get_width() * scale)
            height = int(image.get_height() * scale)
            smaller_image_set[action].append(pygame.transform.scale(image, (width, height)))
    return smaller_image_set
###### END NEW.


###### NEW: read side-stage layout from side_stage.tmx.
platforms = object_rects("Platforms")
blue_traps = object_rects("Blue Traps")
red_traps = object_rects("Red Traps")
###### NEW: bridge platforms start hidden until the player touches the button.
button_rects = object_rects("Buttons")
bridge_platforms = object_rects("Bridge Platforms")
button_pressed = False
###### END NEW.
###### NEW: second pressure button opens the upper bridge for the longer puzzle route.
button_rects_2 = object_rects("Buttons 2")
bridge_platforms_2 = object_rects("Bridge Platforms 2")
button_pressed_2 = False
###### END NEW.

spawn = tiled_map.get_object_by_name("Start")
start_location = (spawn.x, spawn.y)

###### NEW: entrance door is a visual marker for the player spawn point.
entrance = tiled_map.get_object_by_name("Entrance")
entrance_rect = pygame.Rect(entrance.x, entrance.y, entrance.width, entrance.height)
###### END NEW.

finish = tiled_map.get_object_by_name("Finish")
finish_rect = pygame.Rect(finish.x, finish.y, finish.width, finish.height)

###### NEW: side stage key object comes from the TMX map.
key = tiled_map.get_object_by_name("Key")
key_rect = pygame.Rect(key.x, key.y, key.width, key.height)
key_collected = False
###### END NEW.

draw_image_layers(tiled_map)
###### END NEW.


###### MODIFIED FROM stage2.py: same player creation style, but the sideview player is smaller for safe platform clearance.
sideview_knight_img = scale_image_set(ci.knight_img, 0.42)
user1 = ci.player("User 1", "knight", 1, 100, 0, start_location, 0, sideview_knight_img)
user1.rect.midbottom = start_location
user1.on_ground = False
###### END MODIFIED.


###### MODIFIED FROM current side_stage.py: draw level objects loaded from TMX.
def draw_level():
    global key_collected, button_pressed, button_pressed_2

    screen.fill(BLACK)
    ###### MODIFIED: draw the full grey wall with warm torch light.
    screen.blit(bunker_full_background_img, (0, 0))
    screen.blit(background, (0, 0))
    ###### END MODIFIED.

    for platform in platforms:
        ###### MODIFIED: platforms use background-matching bunker stone tiles.
        draw_tiled_image(screen, bunker_platform_img, platform)
        pygame.draw.rect(screen, OUTLINE, platform, 2)
        ###### END MODIFIED.

    ###### NEW: draw the bridge only after the pressure button has been touched.
    if button_pressed:
        for platform in bridge_platforms:
            draw_tiled_image(screen, puzzle_bridge_img, platform)
            pygame.draw.rect(screen, OUTLINE, platform, 2)
    ###### END NEW.
    ###### NEW: draw the upper bridge only after the second pressure button has been touched.
    if button_pressed_2:
        for platform in bridge_platforms_2:
            draw_tiled_image(screen, puzzle_bridge_img, platform)
            pygame.draw.rect(screen, OUTLINE, platform, 2)
    ###### END NEW.

    ###### NEW: draw puzzle button in pressed or unpressed state.
    for button in button_rects:
        if button_pressed:
            screen.blit(button_pressed_img, button)
        else:
            screen.blit(button_img, button)
    ###### END NEW.
    ###### NEW: draw the second puzzle button in pressed or unpressed state.
    for button in button_rects_2:
        if button_pressed_2:
            screen.blit(button_pressed_img, button)
        else:
            screen.blit(button_img, button)
    ###### END NEW.

    for trap in blue_traps:
        ###### MODIFIED: blue reset traps use a pixel-art water tile without an extra outline.
        draw_tiled_image(screen, blue_trap_img, trap)
        ###### END MODIFIED.

    for trap in red_traps:
        ###### MODIFIED: red fail traps use a pixel-art lava tile without an extra outline.
        draw_tiled_image(screen, red_trap_img, trap)
        ###### END MODIFIED.

    ###### MODIFIED: draw the closed entrance door at the spawn point.
    screen.blit(exit_gate_img, entrance_rect)
    ###### END MODIFIED.

    ###### NEW: draw the required key until the player collects it.
    if not key_collected:
        screen.blit(gold_key_img, key_rect)
    ###### END NEW.

    ###### MODIFIED: exit gate changes image after the key is collected.
    if key_collected:
        screen.blit(exit_gate_open_img, finish_rect)
    else:
        screen.blit(exit_gate_img, finish_rect)
    ###### END MODIFIED.
###### END MODIFIED.


###### NEW: hidden bridge becomes solid after the button is pressed.
def active_platforms():
    current_platforms = platforms[:]
    if button_pressed:
        current_platforms += bridge_platforms
    if button_pressed_2:
        current_platforms += bridge_platforms_2
    return current_platforms
###### END NEW.


###### MODIFIED FROM stage2.py move_user(): horizontal movement plus gravity jump.
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
###### END MODIFIED.


###### NEW: sideview collision checks x and y separately.
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
###### END NEW.


###### MODIFIED: blue trap reset helper also resets the key, buttons, and locks the exit again.
def reset_user(user):
    global key_collected, button_pressed, button_pressed_2

    user.rect.midbottom = start_location
    user.velocity = pygame.math.Vector2(0, 0)
    user.on_ground = False
    key_collected = False
    button_pressed = False
    button_pressed_2 = False
###### END MODIFIED.


###### MODIFIED FROM current side_stage.py: blue traps reset, red traps fail, all from TMX.
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
###### END MODIFIED.


###### NEW: pressure button permanently opens the bridge for this simple puzzle.
def button_check(user):
    global button_pressed, button_pressed_2

    for button in button_rects:
        if user.rect.colliderect(button):
            button_pressed = True

    for button in button_rects_2:
        if user.rect.colliderect(button):
            button_pressed_2 = True
###### END NEW.


###### NEW: collect the key before checking the locked exit.
def key_check(user):
    global key_collected

    if not key_collected and user.rect.colliderect(key_rect):
        key_collected = True
        print("Side stage key collected")
###### END NEW.


###### MODIFIED: win condition requires the key and the TMX exit object.
def win_check(user):
    if key_collected and user.rect.colliderect(finish_rect):
        return True
    return False
###### END MODIFIED.


###### COPIED FROM stage1.py / stage2.py: same game loop shape and pygame event handling.
game_active = True
side_stage_clear = False

while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False

    keys = pygame.key.get_pressed()
    move_user(user1, keys)
    ###### MODIFIED: collision includes bridge platforms only after the button opens them.
    collision_check(user1, active_platforms())
    ###### END MODIFIED.

    if fail_check(user1):
        game_active = False

    ###### NEW: button opens the puzzle bridge before the key route.
    button_check(user1)
    ###### END NEW.

    ###### NEW: player must collect the key before the finish can clear the stage.
    key_check(user1)
    ###### END NEW.

    if win_check(user1):
        side_stage_clear = True
        game_active = False

    draw_level()
    screen.blit(user1.image, user1.rect)

    pygame.display.update()
    clock.tick(60)
###### END COPIED.

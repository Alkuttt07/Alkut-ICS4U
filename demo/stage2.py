import pygame
import pytmx
import random
import char_item_copy as ci

framex = 1200
framey = 800

pygame.init()
screen = pygame.display.set_mode((framex, framey))

background = pygame.Surface((framex, framey)).convert_alpha()

tiled_map = pytmx.load_pygame("stage2.1.tmx", pixelalpha=True)
tiled_map2 = pytmx.load_pygame("stage2.2.tmx", pixelalpha=True)

mapwalls = {
    tiled_map: [[], [], [], []],
    tiled_map2: [[], [], [], []]
}   #Order: Up, Left, Bottom, Right

def wall_append(walldic):
    for m in walldic:
        for w in m.get_layer_by_name("Up Walls"):
            walldic[m][0].append(pygame.Rect(w.x, w.y, w.width, w.height))
        for w in m.get_layer_by_name("Left Walls"):
            walldic[m][1].append(pygame.Rect(w.x, w.y, w.width, w.height))
        for w in m.get_layer_by_name("Bottom Walls"):
            walldic[m][2].append(pygame.Rect(w.x, w.y, w.width, w.height))
        for w in m.get_layer_by_name("Right Walls"):
            walldic[m][3].append(pygame.Rect(w.x, w.y, w.width, w.height))

wall_append(mapwalls)

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

up_key = pygame.K_w
left_key = pygame.K_a
down_key = pygame.K_s
right_key = pygame.K_d

user1 = ci.player("User 1", "knight", 1, 100, 0, ci.default_location, 0, ci.knight_img)
move_unit = 10

def map_transition(user, bg, mob_group):
    if user.rect.left > framex and bg == tiled_map:
        draw_image_layers(tiled_map2)
        user.rect.left -= framex
        for x in mob_group:
            x.rect.left -= framex
        return tiled_map2
    
    elif user.rect.left < 0 and bg == tiled_map2:
        bg == tiled_map
        draw_image_layers(tiled_map)
        user.rect.left += framex
        for x in mob_group:
            x.rect.left += framex
        return tiled_map
    
    else:
        return bg

def move_user(user):

    img = user.image_set["Jump"]

    if event.type == pygame.KEYDOWN:
        
        if event.key == left_key:                
            user.velocity += pygame.math.Vector2(-move_unit, 0)
            img = user.image_set["Walk"]
        if event.key == right_key:
            user.velocity += pygame.math.Vector2(move_unit, 0)
            img =  user.image_set["Walk"]
        if event.key == up_key:
            user.velocity += pygame.math.Vector2(0, -move_unit)
            img = user.image_set["Jump"]
        if event.key == down_key:                
            user.velocity += pygame.math.Vector2(0, move_unit)
            img = user.image_set["Jump"]

    if event.type == pygame.KEYUP:
        if event.key == left_key:
            user.velocity = pygame.math.Vector2(0, user.velocity.y)
        if event.key == right_key:
            user.velocity = pygame.math.Vector2(0, user.velocity.y)
        if event.key == up_key:
            user.velocity = pygame.math.Vector2(user.velocity.x, 0)
        if event.key == down_key:
            user.velocity = pygame.math.Vector2(user.velocity.x, 0)
        
        img = user.image_set["Jump"]

    return img

def collision_check(user, wlist):
    if user.rect.move(user.velocity).collidelist(wlist[0]) > -1:
        user.velocity = pygame.math.Vector2(user.velocity.x, 0)
    if user.rect.move(user.velocity).collidelist(wlist[1]) > -1:
        user.velocity = pygame.math.Vector2(0, user.velocity.y)
    if user.rect.move(user.velocity).collidelist(wlist[2]) > -1:
        user.velocity = pygame.math.Vector2(user.velocity.x, 0)
    if user.rect.move(user.velocity).collidelist(wlist[3]) > -1:
        user.velocity = pygame.math.Vector2(0, user.velocity.y)

game_active = True

mob_list = pygame.sprite.Group()
for x in range(5):
    mob_list.add(ci.monster("Skeleton", 1, 10, (random.randint(100, framex-100), random.randint(100, framey-100)), ci.skelly_img))

current_map = tiled_map
draw_image_layers(current_map)

frame_n = 0
while game_active:
    current_map = map_transition(user1, current_map, mob_list)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False
        
        else:
            user1.image = move_user(user1)[frame_n]

    collision_check(user1, mapwalls[current_map])

    user1.update()

    screen.blit(background, (0,0))
    screen.blit(user1.image, user1.rect)

    mob_list.update(user1)
    mob_list.draw(screen)

    if frame_n < 11 and user1.velocity != pygame.math.Vector2(0, 0):
        frame_n += 1
    else:
        frame_n = 0

    pygame.display.update()
    pygame.time.Clock().tick(20)
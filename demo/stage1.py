import pygame
import pytmx
import random
import char_item as ci
import map

framex = 1200
framey = 800

pygame.init()
screen = pygame.display.set_mode((framex, framey))

tiled_map = pytmx.load_pygame("stage1.tmx", pixelalpha=True)

background = pygame.Surface((1200, 800)).convert_alpha()

rwall = []
lwall = []
uwall = []
bwall = []

rwall_layer = tiled_map.get_layer_by_name("Right Walls")
lwall_layer = tiled_map.get_layer_by_name("Left Walls")
uwall_layer = tiled_map.get_layer_by_name("Up Walls")
bwall_layer = tiled_map.get_layer_by_name("Bottom Walls")

for w in rwall_layer:
    rwall.append(pygame.Rect(w.x, w.y, w.width, w.height))
for w in lwall_layer:
    lwall.append(pygame.Rect(w.x, w.y, w.width, w.height))
for w in uwall_layer:
    uwall.append(pygame.Rect(w.x, w.y, w.width, w.height))
for w in bwall_layer:
    bwall.append(pygame.Rect(w.x, w.y, w.width, w.height))

door = tiled_map.get_object_by_name("Exit")
door_rect = pygame.Rect(door.x, door.y, door.width, door.height)

def draw_image_layers():
    global background
    
    for layer in tiled_map.visible_layers:        
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile_image = tiled_map.get_tile_image_by_gid(gid)
                if tile_image:
                    pixel_x = x * tiled_map.tilewidth
                    pixel_y = y * tiled_map.tileheight
                    background.blit(tile_image, (pixel_x, pixel_y))

draw_image_layers()

up_key = pygame.K_w
left_key = pygame.K_a
down_key = pygame.K_s
right_key = pygame.K_d

user1 = ci.player("User 1", "knight", 1, 100, 0, ci.default_location, 0, ci.inventory, ci.knight_img)
move_unit = 10

def move_user(user):

    img_flip = 0

    if event.type == pygame.KEYDOWN:
        if event.key == up_key:
            user.velocity += pygame.math.Vector2(0, -move_unit)
            user.image = user.image_set["Jump"][img_flip]
        if event.key == left_key:                
            user.velocity += pygame.math.Vector2(-move_unit, 0)
            img_flip = 1
            user.image = user.image_set["Walk"][img_flip]
        if event.key == down_key:                
            user.velocity += pygame.math.Vector2(0, move_unit)
            user.image = user.image_set["Jump"][img_flip]
        if event.key == right_key:
            user.velocity += pygame.math.Vector2(move_unit, 0)
            img_flip = 0
            user.image = user.image_set["Walk"][img_flip]                

    if event.type == pygame.KEYUP:
        if event.key == up_key:
            user.velocity = pygame.math.Vector2(user.velocity.x, 0)
        if event.key == left_key:
            user.velocity = pygame.math.Vector2(0, user.velocity.y)
            img_flip = 1
        if event.key == down_key:
            user.velocity = pygame.math.Vector2(user.velocity.x, 0)
        if event.key == right_key:
            user.velocity = pygame.math.Vector2(0, user.velocity.y)
            img_flip = 0

        user.image = user.image_set["Stand"][img_flip]

def collision_check(user, ulist, llist, blist, rlist, dr):
    if user.rect.move(user.velocity).collidelist(ulist) > -1:
        user.velocity = pygame.math.Vector2(user.velocity.x, 0)
    if user.rect.move(user.velocity).collidelist(llist) > -1:
        user.velocity = pygame.math.Vector2(0, user.velocity.y)
    if user.rect.move(user.velocity).collidelist(blist) > -1:
        user.velocity = pygame.math.Vector2(user.velocity.x, 0)
    if user.rect.move(user.velocity).collidelist(rlist) > -1:
        user.velocity = pygame.math.Vector2(0, user.velocity.y)
    if user.rect.colliderect(dr):
        print("Stage 2")

game_active = True

mob_list = pygame.sprite.Group()
for x in range(5):
    mob_list.add(ci.monster("Skeleton", 1, 10, (random.randint(100, framex-100), random.randint(100, framey-100)), ci.skelly_img))

interac_list = pygame.sprite.Group()
for x in range(3):
    interac_list.add(map.interactive("bush", (random.randint(100, framex-100), random.randint(100, framey-100)), map.bush_img))
for x in range(2):
    interac_list.add(map.interactive("hole", (random.randint(100, framex-100), random.randint(100, framey-100)), map.hole_img))

while game_active and user1.death():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False
        
        else:
            move_user(user1)
    
    collision_check(user1, uwall, lwall, bwall, rwall, door_rect)

    user1.update()

    screen.blit(background, (0,0))
    screen.blit(user1.image, user1.rect)

    mob_list.update(user1)
    mob_list.draw(screen)

    interac_list.update()
    interac_list.draw(screen)
    user1.interaction(interac_list)

    pygame.display.update()
    pygame.time.Clock().tick(12)

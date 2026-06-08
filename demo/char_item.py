import pygame
pygame.init()
import random
import time

screen = pygame.display.set_mode((1200, 800))

lvlup_hp = 1.1
lvlup_gold = 100

move_unit = 10
mob_move_unit = 2

default_location = (200, 400)
character_size = (100, 100)

knight_walk_sprites = pygame.image.load('char_images\\knight\\walk_spritesheet.png').convert_alpha()
knight_jump_sprites = pygame.image.load('char_images\\knight\\jump_spritesheet.png').convert_alpha()

class Spritesheet:
    def __init__(self, image):
        self.sheet = image
    
    def get_image(self, frame, width, height, scale):

        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
           
        image = pygame.transform.scale(image, (width * scale, height * scale))
           
        return image

knight_img_origin = {
    "Stand": [pygame.image.load('char_images\\knight\\stand.png').convert_alpha()],
    "Walk": [pygame.image.load('char_images\\knight\\walk.png').convert_alpha()],
    "Jump": [pygame.image.load('char_images\\knight\\jump.png').convert_alpha()],
    "Attack": [pygame.image.load('char_images\\knight\\attack.png').convert_alpha()]
}

knight_sprites_img_origin = {
    "Walk": [Spritesheet(knight_walk_sprites).get_image(i, 2016, 288, 25/72) for i in range(12)],
    "Jump": [Spritesheet(knight_jump_sprites).get_image(i, 2016, 288, 25/72) for i in range(12)]
}

sprite_img = pygame.image.load('sample_sprites.png').convert_alpha()

'''Sprite sheet plan: 80*100 for each frame, 12 images per animation: 960*100 size image will be required
    Needed sprite sheets: Horizontal movement, Vertical movement, Attack, Defence
    Skins? Just change colours

    Edits for image dictionary: the "values" of the image dictionary should be list of images for animation, maybe 12 objects inside.
    Will need walk, jump, attack, defense. Stand image will be standard image for all.
    No defense method will be needed for monsters' image dictionary

'''
def img_adjust(img_dict):
    for i in img_dict:
        img_dict[i][0] = pygame.transform.scale(img_dict[i][0], character_size)
        img_dict[i].append(pygame.transform.flip(img_dict[i][0], flip_x=True, flip_y=False))
    return img_dict

knight_img = img_adjust(knight_img_origin)

skelly_img = pygame.image.load('char_images\\larry.png').convert_alpha()
skelly_img = pygame.transform.scale(skelly_img, character_size)

class character(pygame.sprite.Sprite):
    def __init__(self, name, level, hp, location, img):
        super().__init__()
        self.name = name
        self.level = level
        self.hp = hp
        self.image = img
        self.rect = self.image.get_rect(center = location)
        self.velocity = pygame.math.Vector2(0, 0)
        pass

    def update(self):
        self.rect.move_ip(self.velocity)
        pass

    def attack(self):
        pass

class player(character):
    def __init__(self, name, profession, level, hp, xp, location, gold, img_set):
        super().__init__(name, level, hp, location, img_set["Stand"][0])
        self.profession = profession
        self.xp = xp
        self.gold = gold
        self.visibility = True
        self.image_set = img_set

    def promotion(self):
        self.level += 1
        self.hp *= lvlup_hp
        self.gold += lvlup_gold

    def interaction(self, interac):
        interac_list = [x for x in interac.sprites()]
        if self.rect.collidelist([x.rect for x in interac_list]) > -1 and interac_list[self.rect.collidelist(interac_list)].type == "bush":
            self.visibility = False
        else:
            self.visibility = True
        
        if self.rect.collidelist([x.rect for x in interac_list]) > -1 and interac_list[self.rect.collidelist(interac_list)].type == "hole":
            self.velocity = pygame.math.Vector2(0, 0)
    
    def death(self):
        if self.hp <= 0:
            return False
        else:
            return True

class monster(character):

    def attack(self, user):
        if self.rect.colliderect(user.rect):
            user.hp -= 1
        
    def update(self, user):
        if user.visibility:
            distance = (user.rect.center[0] - self.rect.center[0], user.rect.center[1] - self.rect.center[1])
            ratio = max(abs(distance[0]), abs(distance[1])) / mob_move_unit
            if ratio != 0 and user.velocity != pygame.math.Vector2(0, 0):
                self.rect.move_ip(distance[0]/ratio, distance[1]/ratio)
        else:
            self.rect.move_ip(random.randint(-mob_move_unit, mob_move_unit), random.randint(-mob_move_unit, mob_move_unit))
        '''if self.rect.colliderect(user.rect):
            user.hp -= 5'''


class Weapon:
    def __init__(self, name, level, dur, dmg, cd, hc, cost, img):
        self.name = name
        self.level = level
        self.durability = dur
        self.damage = dmg
        self.cooldown = cd
        self.hitchance = hc
        self.cost = cost
        self.image = img

    def attack(self, target):
        target -= self.damage

class Shield:
    def __init__(self, name, level, hp, dr, cost, img):
        self.name = name
        self.level = level
        self.hp = hp
        self.dr = dr
        self.cost = cost
        self.img = img
    
    def block(self, attack):
        attack *= (1 - self.dr)
        self.hp -= attack
        attack = 0

class Potion:
    def __init__(self, name, level, cost, img):
        self.name = name
        self.level = level
        self.cost = cost
        self.img = img
        pass

    def use(self):
        pass

inventory = {
    "Weapon": [],
    "Shield": [],
    "Potion": []
}

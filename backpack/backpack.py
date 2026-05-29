import pygame
pygame.init()
WIDTH, HEIGHT = 1200, 800
GRID_SIZE = 60
GRID_COLS = 8
GRID_ROWS = 4
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bag_img = pygame.image.load('backpack/bagimg.png').convert_alpha()
bag_img = pygame.transform.scale(bag_img,(750,745))
dungeon_menu = pygame.image.load('menu/menu images/dungeon_menu.png').convert()
clock = pygame.time.Clock()
cursor_img = pygame.image.load("menu/menu images/sword_cursor.png").convert_alpha()
cursor_img = pygame.transform.scale(cursor_img, (30, 30))
pygame.mouse.set_cursor((0, 0), cursor_img)
BG = (30, 30, 30)
GRID_COLOR = (210, 210, 210)
ITEM_COLOR = (0, 200, 0)
DRAG_COLOR = (200, 200, 0)
INVALID_COLOR = (200, 50, 50)
INV_X = 100
INV_Y = 100
class Button:
    def __init__(self, pos, size, image, type):
        self.pos = pos
        self.size = size
        self.image = image
        self.type = type
class Interactive_Button(Button):
    def __init__(self, pos, size, image, lit_image, dark_image, type, action=None):
        super().__init__(pos, size, image, type)
        self.lit_image = lit_image
        self.dark_image = dark_image
        self.action = action
        self.pressed = False
    def detect_hover(self, screen, mouse_pos):
        button_rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        mouse_down = pygame.mouse.get_pressed()[0]
        if button_rect.collidepoint(mouse_pos):
            if mouse_down:
                self.pressed = True
                screen.blit(self.dark_image, self.pos)
            else:
                if self.pressed:
                    if self.action:
                        self.action()
                    self.pressed = False
                screen.blit(self.lit_image, self.pos)
        else:
            self.pressed = False
            screen.blit(self.image, self.pos)
    def detect_click(self, mouse_pos):
        button_rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        if self.action and button_rect.collidepoint(mouse_pos):
            self.action()
        return button_rect.collidepoint(mouse_pos)
class InventoryItem:
    def __init__(self, item):
        self.item = item
        self.width = item.dimensions[0]
        self.height = item.dimensions[1]
        self.grid_x = 0
        self.grid_y = 0
        self.rotated = False
    def rotate(self):
        self.width, self.height = self.height, self.width
        self.rotated = not self.rotated
    def get_rect(self):
        return pygame.Rect(
            INV_X + self.grid_x * GRID_SIZE,
            INV_Y + self.grid_y * GRID_SIZE,
            self.width * GRID_SIZE,
            self.height * GRID_SIZE
        )
class Inventory:
    def __init__(self):
        self.cols = GRID_COLS
        self.rows = GRID_ROWS
        self.upgrade_level = 0
        self.items = []
        self.itemposition = {}
    def can_place(self, item, x, y):
        if x < 0 or y < 0:
            return False
        if x + item.width > self.cols or y + item.height > self.rows:
            return False
        for other in self.items:
            if other == item:
                continue
            if not (x + item.width <= other.grid_x or
                    x >= other.grid_x + other.width or
                    y + item.height <= other.grid_y or
                    y >= other.grid_y + other.height):
                return False
        return True
    def upgrade(self):
        if self.upgrade_level == 0:
            self.cols = 12
            self.rows = 4
        elif self.upgrade_level == 1:
            self.cols = 12
            self.rows = 6
        elif self.upgrade_level == 2:
            self.cols = 12
            self.rows = 8
        self.upgrade_level += 1    
    def auto_sort(self):
        items = self.items[:]
        items.sort(key=lambda item: item.width * item.height, reverse=True)
        self.items = []
        for item in items:
            placed = False
            for rotate in [False, True]:
                if rotate:
                    item.rotate()
                for y in range(self.rows):
                    for x in range(self.cols):
                        if self.can_place(item, x, y):
                            item.grid_x = x
                            item.grid_y = y
                            self.items.append(item)
                            placed = True
                            break
                    if placed:
                        break
                if placed:
                    break
                else:
                    if rotate:
                        item.rotate()
            if not placed:
                self.items.append(item)
            assign_txt()
    def draw(self):
        for i in range(self.cols):
            for j in range(self.rows):
                rect = pygame.Rect(
                    INV_X + i * GRID_SIZE,
                    INV_Y + j * GRID_SIZE,
                    GRID_SIZE,
                    GRID_SIZE
                )
                temp_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
                pygame.draw.rect(
                    temp_surface,
                    (*GRID_COLOR, 80),
                    (0, 0, rect.width, rect.height))
                screen.blit(temp_surface, rect.topleft)
        for item in self.items:
            pygame.draw.rect(screen, ITEM_COLOR, item.get_rect())

class Item:
    def __init__(self, name, description, value, image, ID, dimensions = (1,1)):  
        self.name = name
        self.description = description
        
        self.value = value
        self.image = image
        self.dimensions = dimensions
        self.ID = ID

class Potion(Item):
    def __init__(self, name, description, value, image, ID, dimensions = (1,1)):
        super().__init__(name, description, value, image, ID, dimensions)

class Weapon(Item):
    def __init__(self, name, description, value, image, ID, damage, hitchance, dimensions = (1,1)):
        super().__init__(name, description, value, image, ID, dimensions)
        self.damage = damage
        self.hitchance = hitchance
        self.rarity = value/10 

class Melee(Weapon):
    def __init__(self,name, description, value, image, ID, damage, hitchance, dimensions = (1,1), range = 1):
        super().__init__(name, description, value, image, ID, damage, hitchance, dimensions)

        self.range = range
        self.rarity = value/10

class Spear(Melee):
    def __init__(self,name, description, value, image, ID, damage, hitchance, dimensions = (1,1), range = 2):
        super().__init__(name, description, value, image, ID, damage, hitchance, dimensions, range)


inventory = Inventory()

#examples
w1 = Weapon("blablabla","good weapon",50,None,35,20,10,(2,1))
w2 = Weapon("sss","better waepon",100,None,50,30,10,(1,3))
w3 = Weapon("bbb0","best weapon",150,None,60,40,13,(2,2))
inventory.items.append(InventoryItem(w1))
inventory.items.append(InventoryItem(w2))
inventory.items.append(InventoryItem(w3))

def read_txt():
    with open("backpack/inventory.txt") as txt:
        item_index = 0
        read_list = txt.readlines()
        for x in read_list:
            x = x.split("&&")
            if x[0] == "Weapon":
                inventory.items.append(InventoryItem(Weapon(x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])))
                inventory.itemposition.update({item_index : x[9]})
                item_index += 1
            elif x[0] == "Potion":
                inventory.items.append(InventoryItem(Potion(x[1],x[2],x[3],x[4],x[5],x[6])))
                inventory.itemposition.update({item_index : x[7]})
                item_index += 1
            elif x[0] == "Melee":
                inventory.items.append(InventoryItem(Melee(x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])))
                inventory.itemposition.update({item_index : x[9]})
                item_index += 1
            elif x[0] == "Spear":
                inventory.items.append(InventoryItem(Spear(x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])))
                inventory.itemposition.update({item_index : x[9]})
                item_index += 1
            elif x[0] == "Item":
                inventory.items.append(InventoryItem(Item(x[1],x[2],x[3],x[4],x[5],x[6])))
                inventory.itemposition.update({item_index : x[7]})
                item_index += 1
            elif x == "0":
                inventory.upgrade_level = 0
            elif x == "1":
                inventory.upgrade_level = 1
            elif x == "2":
                inventory.upgrade_level = 2


def assign_txt():
    item_index = 0
    with open("backpack/inventory.txt","w") as clear_txt:
        clear_txt.write("")
    with open("backpack/inventory.txt","a") as txt:
        for x in inventory.items:
            if x is Weapon:
                txt.write(f"Weapon&&{x.name}&&{x.description}&&{x.value}&&{x.image}&&{x.ID}&&{x.damage}&&{x.hitchance}&&{x.dimensions}&&{inventory.itemposition[item_index]}\n")
                item_index += 1
            elif x is Potion:
                txt.write(f"Potion&&{x.name}&&{x.description}&&{x.value}&&{x.image}&&{x.ID}&&{x.dimensions}&&{inventory.itemposition[item_index]}\n")
                item_index += 1
            elif x is Melee:
                txt.write(f"Melee&&{x.name}&&{x.description}&&{x.value}&&{x.image}&&{x.ID}&&{x.damage}&&{x.hitchance}&&{x.dimensions}&&{inventory.itemposition[item_index]}\n")
                item_index += 1
            elif x is Spear:
                txt.write(f"Spear&&{x.name}&&{x.description}&&{x.value}&&{x.image}&&{x.ID}&&{x.damage}&&{x.hitchance}&&{x.dimensions}&&{inventory.itemposition[item_index]}\n")
                item_index += 1
            elif x is Item:
                txt.write(f"Item&&{x.name}&&{x.description}&&{x.value}&&{x.image}&&{x.ID}&&{x.dimensions}&&{inventory.itemposition[item_index]}\n")
                item_index += 1
        txt.write(inventory.upgrade_level)




selected_item = None
def interact_action():
    if selected_item:
        print(selected_item.item.name)
def discard_action():
    global selected_item, dragging_item, deleted_item
    target = dragging_item if dragging_item else selected_item  
    if target in inventory.items:
        inventory.items.remove(target) 
    selected_item = None
    dragging_item = None
    deleted_item = True
    assign_txt()
def sort_action():
    if not dragging_item:
        inventory.auto_sort()
def upgrade_action():
    if not dragging_item:
        inventory.upgrade()
def make_button_surface(color, text=None):
    surf = pygame.Surface((180, 60))
    surf.fill(color)
    font = pygame.font.SysFont(None, 36)
    text_surface = font.render(text, True, (255, 255, 255))
    surf.blit(text_surface, (35, 15))
    return surf

button = Interactive_Button(
    pos=(900, 120),
    size=(180, 60),
    image=make_button_surface((80, 80, 80),"SORT"),
    lit_image=make_button_surface((120, 120, 200),"SORT"),
    dark_image=make_button_surface((50, 50, 150),"SORT"),
    type="sort",
    action=sort_action
)
upgrade_button = Interactive_Button(
    pos=(900, 220),
    size=(180, 60),
    image=make_button_surface((80, 80, 80), "UPGRADE"),
    lit_image=make_button_surface((120, 120, 200), "UPGRADE"),
    dark_image=make_button_surface((50, 50, 150), "UPGRADE"),
    type="upgrade",
    action=upgrade_action
)

interact_button = Interactive_Button(
    pos=(900, 420),
    size=(180, 60),
    image=make_button_surface((80, 80, 80),"INTERACT"),
    lit_image=make_button_surface((120, 120, 200),"INTERACT"),
    dark_image=make_button_surface((50, 50, 150),"INTERACT"),
    type="interact",
    action=interact_action
)

discard_button = Interactive_Button(
    pos=(900, 520),
    size=(180, 60),
    image=make_button_surface((120, 50, 50),"DISCARD"),
    lit_image=make_button_surface((180, 70, 70),"DISCARD"),
    dark_image=make_button_surface((90, 30, 30),"DISCARD"),
    type="discard",
    action=discard_action
)
dragging_item = None
deleted_item = False
offset_x = 25
offset_y = 25
running = True
while running:
    screen.fill(BG)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(dungeon_menu, (0, 0))
    screen.blit(bag_img ,(88.5,0))
    inventory.draw()
    if selected_item and selected_item in inventory.items:
        pygame.draw.rect(
            screen,
            (255,255,0),
            selected_item.get_rect(),
            4)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_on_ui = (
                pygame.Rect(button.pos[0], button.pos[1], button.size[0], button.size[1]).collidepoint(mouse_x, mouse_y) or
                pygame.Rect(upgrade_button.pos[0], upgrade_button.pos[1], upgrade_button.size[0], upgrade_button.size[1]).collidepoint(mouse_x, mouse_y) or
                pygame.Rect(discard_button.pos[0], discard_button.pos[1], discard_button.size[0], discard_button.size[1]).collidepoint(mouse_x, mouse_y) or
                pygame.Rect(interact_button.pos[0], interact_button.pos[1], interact_button.size[0], interact_button.size[1]).collidepoint(mouse_x, mouse_y))
            if mouse_on_ui:
                pass
            else:
                clicked_item = False
                for item in inventory.items:
                    if item.get_rect().collidepoint(mouse_x, mouse_y):
                        selected_item = item
                        dragging_item = item
                        clicked_item = True
                        break
                if not clicked_item:
                    selected_item = None
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if dragging_item:
                    if not deleted_item:
                        grid_x = (mouse_x - INV_X) // GRID_SIZE
                        grid_y = (mouse_y - INV_Y) // GRID_SIZE
                        if inventory.can_place(dragging_item, grid_x, grid_y):
                            dragging_item.grid_x = grid_x
                            dragging_item.grid_y = grid_y
                    dragging_item = None
                    deleted_item = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and dragging_item:
                dragging_item.rotate()
    button.detect_hover(screen, (mouse_x, mouse_y))
    upgrade_button.detect_hover(screen, (mouse_x, mouse_y))
    if selected_item is not None:
        interact_button.detect_hover(screen, (mouse_x, mouse_y))
        discard_button.detect_hover(screen, (mouse_x, mouse_y))
        if selected_item is not None:
            font = pygame.font.SysFont(None, 28)
            item_name = font.render(
                selected_item.item.name,
                True,
                (255,255,255))
            item_description = font.render(
                selected_item.item.description,
                True,
                (255,255,255))
            screen.blit(item_name, (900, 350))
            screen.blit(item_description, (900, 375))
    if dragging_item and not deleted_item:
        temp_x = mouse_x - offset_x
        temp_y = mouse_y - offset_y
        grid_x = (mouse_x - INV_X) // GRID_SIZE
        grid_y = (mouse_y - INV_Y) // GRID_SIZE
        valid = inventory.can_place(dragging_item, grid_x, grid_y)
        color = DRAG_COLOR if valid else INVALID_COLOR
        rect = pygame.Rect(
            temp_x,
            temp_y,
            dragging_item.width * GRID_SIZE,
            dragging_item.height * GRID_SIZE
        )
        pygame.draw.rect(screen, color, rect)
    pygame.display.flip()
    clock.tick(60)
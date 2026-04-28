import pygame

pygame.init()

WIDTH, HEIGHT = 1200, 800
GRID_SIZE = 60
GRID_COLS = 12
GRID_ROWS = 8

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Inventory")

clock = pygame.time.Clock()

BG = (30, 30, 30)
GRID_COLOR = (80, 80, 80)
ITEM_COLOR = (0, 200, 0)
DRAG_COLOR = (200, 200, 0)
INVALID_COLOR = (200, 50, 50)

INV_X = 100
INV_Y = 80


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
    def __init__(self, item, width, height):
        self.item = item
        self.width = width
        self.height = height
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
        self.items = []

    def can_place(self, item, x, y):
        if x < 0 or y < 0:
            return False
        if x + item.width > GRID_COLS or y + item.height > GRID_ROWS:
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

    def auto_sort(self):
        items = self.items[:]
        items.sort(key=lambda item: item.width * item.height, reverse=True)
        self.items = []

        for item in items:
            placed = False

            for rotate in [False, True]:
                if rotate:
                    item.rotate()

                for y in range(GRID_ROWS):
                    for x in range(GRID_COLS):
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

    def draw(self):
        for i in range(GRID_COLS):
            for j in range(GRID_ROWS):
                rect = pygame.Rect(
                    INV_X + i * GRID_SIZE,
                    INV_Y + j * GRID_SIZE,
                    GRID_SIZE,
                    GRID_SIZE
                )
                pygame.draw.rect(screen, GRID_COLOR, rect, 1)

        for item in self.items:
            pygame.draw.rect(screen, ITEM_COLOR, item.get_rect())


class Weapon:
    def __init__(self, level, dur, dmg, cd, hc, cost, img):
        self.level = level
        self.durability = dur
        self.damage = dmg
        self.cooldown = cd
        self.hitchance = hc
        self.cost = cost
        self.image = img


inventory = Inventory()

# examples
w1 = Weapon(1, 100, 20, 1.0, 0.8, 100, None)
w2 = Weapon(2, 120, 35, 0.8, 0.85, 200, None)
w3 = Weapon(1, 80, 15, 1.2, 0.75, 80, None)

inventory.items.append(InventoryItem(w1, 2, 1))
inventory.items.append(InventoryItem(w2, 1, 3))
inventory.items.append(InventoryItem(w3, 2, 2))


def sort_action():
    if not dragging_item:
        inventory.auto_sort()


def make_button_surface(color):
    surf = pygame.Surface((180, 60))
    surf.fill(color)
    font = pygame.font.SysFont(None, 36)
    text = font.render("SORT", True, (255, 255, 255))
    surf.blit(text, (50, 15))
    return surf


button = Interactive_Button(
    pos=(900, 120),
    size=(180, 60),
    image=make_button_surface((80, 80, 80)),
    lit_image=make_button_surface((120, 120, 200)),
    dark_image=make_button_surface((50, 50, 150)),
    type="sort",
    action=sort_action
)


dragging_item = None
offset_x = 0
offset_y = 0


while True:
    screen.fill(BG)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.detect_click((mouse_x, mouse_y)):
                continue

            for item in reversed(inventory.items):
                if item.get_rect().collidepoint(mouse_x, mouse_y):
                    dragging_item = item
                    offset_x = mouse_x - item.get_rect().x
                    offset_y = mouse_y - item.get_rect().y
                    inventory.items.remove(item)
                    break

        if event.type == pygame.MOUSEBUTTONUP:
            if dragging_item:
                grid_x = (mouse_x - INV_X) // GRID_SIZE
                grid_y = (mouse_y - INV_Y) // GRID_SIZE

                if inventory.can_place(dragging_item, grid_x, grid_y):
                    dragging_item.grid_x = grid_x
                    dragging_item.grid_y = grid_y

                inventory.items.append(dragging_item)
                dragging_item = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and dragging_item:
                dragging_item.rotate()

    inventory.draw()
    button.detect_hover(screen, (mouse_x, mouse_y))

    if dragging_item:
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
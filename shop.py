import pygame
pygame.init()
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (10, 10, 10)
DARK = (30, 30, 30)
GRAY = (90, 90, 90)
WHITE = (230, 230, 230)
YELLOW = (200, 200, 0)
RED = (180, 60, 60)
GREEN = (80, 180, 80)



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





class Player:
    def __init__(self):
        self.money = 6000
        self.bought_items = []


class Shop:
    def __init__(self, player):
        self.player = player

        self.items = [
            Item("blabalbal","aaaa",1500,"gameplot/plot02.jpg",120,(2,1)),
            Item("hahaha","bbbb",700,"gameplot/plot03.jpg",122,(1,1)),
            Item("qqqqqqq","ccc",2500,"gameplot/plot02.jpg",110,(2,3)),
        ]

        self.selected_index = 0
        self.message = "Choose an item to buy."

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.selected_index -= 1
                if self.selected_index < 0:
                    self.selected_index = len(self.items) - 1
            elif event.key == pygame.K_s:
                self.selected_index += 1
                if self.selected_index >= len(self.items):
                    self.selected_index = 0
            elif event.key == pygame.K_SPACE:
                self.buy_selected_item()
    def buy_selected_item(self):
        item = self.items[self.selected_index]
        if self.player.money < item.value:
            self.message = "Not enough money."
            return
        self.player.money -= item.value
        self.player.bought_items.append(item)
        self.message = f"You bought {item.name}."

    def draw(self, surface):
        surface.fill(BLACK)
        self.draw_title(surface)
        self.draw_money(surface)
        self.draw_item_list(surface)
        self.draw_preview(surface)
        self.draw_message(surface)
        self.draw_controls(surface)

    def draw_title(self, surface):
        title = pygame.font.SysFont("arial", 28).render("SHOP - BUY", True, YELLOW)
        surface.blit(title, (50, 50))

    def draw_money(self, surface):
        money_text = pygame.font.SysFont("arial", 28).render(f"Money: {self.player.money}", True, YELLOW)
        surface.blit(money_text, (1000, 50))

    def draw_item_list(self, surface):
        x = 60
        y = 130
        width = 500
        height = 60
        for i, item in enumerate(self.items):
            rect = pygame.Rect(x, y + i * height, width, height - 8)
            if i == self.selected_index:
                pygame.draw.rect(surface, YELLOW, rect, 3)
            else:
                pygame.draw.rect(surface, GRAY, rect, 1)

            name_text = pygame.font.SysFont("arial", 28).render(item.name, True, WHITE)
            price_text = pygame.font.SysFont("arial", 28).render(str(item.value), True, YELLOW)
            surface.blit(name_text, (rect.x + 15, rect.y + 12))
            surface.blit(price_text, (rect.x + 350, rect.y + 12))

    def draw_preview(self, surface):
        item = self.items[self.selected_index]

        panel = pygame.Rect(620, 130, 520, 540)
        pygame.draw.rect(surface, DARK, panel)
        pygame.draw.rect(surface, GRAY, panel, 2)

        name_text = pygame.font.SysFont("arial", 28).render(item.name, True, YELLOW)
        surface.blit(name_text, (panel.x + 20, panel.y + 20))

        price_text = pygame.font.SysFont("arial", 28).render(f"Price: {item.value}", True, WHITE)
        surface.blit(price_text, (panel.x + 20, panel.y + 70))

        description_text = pygame.font.SysFont("arial", 28).render(item.description, True, WHITE)
        surface.blit(description_text, (panel.x + 20, panel.y + 445))

        pygame.draw.rect(surface, GRAY, (panel.x + 296, panel.y + 46, 178, 178), 4)
        image = pygame.image.load(item.image)
        image = pygame.transform.scale(image, (170, 170))
        surface.blit(image, (panel.x + 300, panel.y + 50))

        dimension_text = pygame.font.SysFont("arial", 28).render(
            f"Dimension: {item.dimensions[0]} x {item.dimensions[1]}",
            True,
            WHITE
        )
        surface.blit(dimension_text, (panel.x + 20, panel.y + 105))
        grid_size = 40
        preview_x = panel.x + 20
        preview_y = panel.y + 160

        for row in range(item.dimensions[1]):
            for col in range(item.dimensions[0]):
                rect = pygame.Rect(
                    preview_x + col * grid_size,
                    preview_y + row * grid_size,
                    grid_size,
                    grid_size
                )
                pygame.draw.rect(surface, GREEN, rect)
                pygame.draw.rect(surface, BLACK, rect, 2)

    def draw_message(self, surface):
        msg = pygame.font.SysFont("arial", 28).render(self.message, True, WHITE)
        surface.blit(msg, (60, 700))

    def draw_controls(self, surface):
        text = pygame.font.SysFont("arial", 28).render("w or s to change selection    space to buy", True, GRAY)
        surface.blit(text, (60, 735))


player = Player()
shop = Shop(player)

running = True

while running:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        shop.handle_event(event)
    shop.draw(screen)
    pygame.display.flip()
pygame.quit()
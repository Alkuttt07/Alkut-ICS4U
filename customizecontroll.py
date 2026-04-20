import pygame
import os
controls={}
def initializekeyboard():
    global controls
    controls = {
        "up": ["w", "up"],
        "down": ["s", "down"],
        "left": ["a", "left"],
        "right": ["d", "right"]
    }
def loadkeyboard():
    global controls
    if not os.path.exists("control.txt"):
        initializekeyboard()
        applykeyboard()
        return 
    with open("control.txt", "r") as tx1:
        a=tx1.readline().split("%")
        if len(a) != 8:
            initializekeyboard()
            applykeyboard()
            return
        controls={
            "up": [a[0], a[1]],
            "down": [a[2], a[3]],
            "left": [a[4], a[5]],
            "right": [a[6], a[7]]
            }
def applykeyboard():
    y=[]
    for x in ["up","down","left","right"]:
        y.extend(controls[x])
    with open("control.txt", "w") as f:
        f.write("%".join(y))
def keyused(z):
    for k in controls:
        if z in controls[k]:
            return True
    return False
def changekeyboard():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            return pygame.key.name(event.key)
def keypressed(a, b):
    return (b[pygame.key.key_code(controls[a][0])] or
            b[pygame.key.key_code(controls[a][1])])

#testing
pygame.init()
screen1 = pygame.display.set_mode((1200, 800))
font = pygame.font.SysFont(None, 40)
dungeon_menu = pygame.image.load('menu/menu images/dungeon_menu.png').convert()
settings_img = pygame.image.load('menu/menu images/settings.png').convert_alpha()
settings_img = pygame.transform.scale(settings_img, (612, 408))

button = pygame.Surface((612, 100))
button.fill((60,60,60))
button_selected = pygame.Surface((612, 100))
button_selected.fill((120,120,60))
loadkeyboard()
mode = "menu"
state = {
    "selected": None,
    "rebinding": False
}
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if mode == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                rect = settings_img.get_rect()
                if rect.collidepoint(mx, my):
                    mode = "settings"
        elif mode == "settings":
            actions = ["up","down","left","right"]
            start_y = 200
            gap = 120
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for i, action in enumerate(actions):
                    rect = pygame.Rect(294, start_y + i*gap, 612, 100)
                    if rect.collidepoint(mx, my):
                        state["selected"] = action
                        state["rebinding"] = True
            if state["rebinding"] and event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if not keyused(key):
                    controls[state["selected"]][0] = key
                    state["rebinding"] = False
                    state["selected"] = None
                    applykeyboard()
    if mode == "menu":
        screen1.blit(dungeon_menu, (0, 0))
        screen1.blit(settings_img, (294, 200))
    elif mode == "settings":
        screen1.blit(dungeon_menu, (0, 0))
        actions = ["up","down","left","right"]
        start_y = 200
        gap = 120
        for i, action in enumerate(actions):
            y = start_y + i*gap
            if action == state["selected"]:
                screen1.blit(button_selected, (294, y))
            else:
                screen1.blit(button, (294, y))
            text = f"{action.upper()}: {controls[action][0]} / {controls[action][1]}"
            img = font.render(text, True, (255,255,255))
            screen1.blit(img, (320, y + 30))
        if state["rebinding"]:
            hint = f"Press key for {state['selected']}"
        else:
            hint = "Click to change key"
        hint_img = font.render(hint, True, (255,255,255))
        screen1.blit(hint_img, (350, 120))
    pygame.display.update()
    pygame.time.Clock().tick(60)
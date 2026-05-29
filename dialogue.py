import pygame
pygame.init()
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 32)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOX_COLOR = (30, 30, 30)
dialogues = [
    {
        "speaker": "Alkut",
        "text": "hello!",
        "image": "gameplot/plot01.jpg"
    },

    {
        "speaker": "Harry",
        "text": "HI!!",
        "image": "gameplot/plot02.jpg"
    },

    {
        "speaker": "Toby",
        "text": "Good morning.",
        "image": "gameplot/plot03.jpg"
    },

    {
        "speaker": "everyone",
        "text": "hahahahahahhahah",
        "image": "gameplot/plot02.jpg"
    }
]
dialogue_index = 0
cutscene_finished = False
def draw_dialogue(dialogue):
    screen.fill(BLACK)
    pygame.draw.rect(screen, BOX_COLOR, (80, 500, 1070, 200))
    pygame.draw.rect(screen, WHITE, (80, 500, 1070, 200), 4)
    speaker_text = font.render(dialogue["speaker"], True, WHITE)
    screen.blit(speaker_text, (230, 525))
    content_text = font.render(dialogue["text"], True, WHITE)
    screen.blit(content_text, (230, 585))
    hint = font.render("Press any key to continue  TAB to skip", True, WHITE)
    screen.blit(hint, (230, 640))
    pygame.draw.rect(screen, BOX_COLOR, (40, 480, 160, 190))
    pygame.draw.rect(screen, WHITE, (40, 480, 160, 190), 4)
    img = pygame.image.load(dialogue["image"]).convert_alpha()
    img = pygame.transform.scale(img, (152, 182))
    screen.blit(img, (44, 484))
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if not cutscene_finished:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    cutscene_finished = True
                else:
                    dialogue_index += 1
                    if dialogue_index >= len(dialogues):
                        cutscene_finished = True

    if not cutscene_finished:
        draw_dialogue(dialogues[dialogue_index])
    else:
        screen.fill(BLACK)
        end_text = font.render("end", True, WHITE)
        screen.blit(end_text, (520, 340))
    pygame.display.update()
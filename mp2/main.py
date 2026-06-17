import pygame
pygame.init()
screen=pygame.display.set_mode((1200,800))
color=(225,255,255)
screen.fill(color)
active=True
while active:   
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            raise SystemExit
    pygame.display.update()
    pygame.time.Clock().tick(60)

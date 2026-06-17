import pygame
initialkeyboard=["w","up","a","left","s","down","d","right"]
currentkeyboard=[]
def loadkeyboard():
    with open("control.txt","r") as customizetx1:
        x=customizetx1.readline().split("%")
        for y in range(len(x)):
            currentkeyboard[y]=x[y]
def changekeyboard():
    while True:
        for event in pygame.event.get():  
            if event.type==pygame.KEYDOWN:
                keynumber=event.key
                return pygame.key.name(keynumber)


def applykeyboard():
    with open("control.txt","w") as customizetx2:
        customizetx2.write("%".join(currentkeyboard))

def initializekeyboard():
    global currentkeyboard
    currentkeyboard=initialkeyboard

def assigning():
    pass

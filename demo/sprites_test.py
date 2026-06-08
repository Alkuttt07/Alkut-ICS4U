import pygame
pygame.init()


screen1 = pygame.display.set_mode((800, 400))
sprite_sheet_image = pygame.image.load('sample_sprites_copy.png').convert_alpha()
 
class SpriteSheet():
      def __init__(self, image):
            self.sheet = image

      def get_image(self, frame, width, height, scale):
           
            #create a simple blank surface for a specific frame on the sprite sheet
            image = pygame.Surface((width, height)).convert_alpha()
            #inserting the image of that frame onto the created surface
            image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
           
            image = pygame.transform.scale(image, (width * scale, height * scale))
           
            return image

Animation_object = SpriteSheet(sprite_sheet_image)
Frames = [Animation_object.get_image(i, 12, 15, 5) for i in range(21)]

i = 0
game_active = True
while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False

    screen1.blit(Frames[i], (200,200))

    if i < 20:
          i+=1
    else:
          i = 0

    pygame.display.update()
    pygame.time.Clock().tick(10)
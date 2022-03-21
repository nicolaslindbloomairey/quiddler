from images import IMAGE_DICT
import pygame

class Card(pygame.sprite.Sprite):
    top_z = 0
    def __init__(self, letter, x=30, y=30):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.letter = letter
        self.bring_to_top() # newly created card has max z-index 

        # set image pointer to an image
        self.face = IMAGE_DICT.get(self.letter, IMAGE_DICT["template"])
        self.back = IMAGE_DICT["back"]
        self.image = self.back

        self.face_up = False

        # pygame expects sprites to have a self.rect [Rectangle]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0

        #self.selected = False

    def flip_over(self):
        self.face_up = not self.face_up
        self.image = self.face if self.face_up else self.back

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def __str__(self):
        return self.letter

    def __repr__(self):
        return self.letter

    def bring_to_top(self):
        self.z = Card.top_z
        Card.top_z += 1

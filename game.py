import pygame
from card import Card
from deck import Deck
 
class Game:
    DISCARD = (140, 30)
    DECK = (30, 30)
    def __init__(self):
        pygame.init()
        # load and set the logo
        #logo = pygame.image.load("logo32x32.png")
        #pygame.display.set_icon(logo)
        pygame.display.set_caption("Quiddler")

        self.clock = pygame.time.Clock()
        self.fps_font = pygame.font.SysFont("Arial", 18)
         
        # create a surface on screen that has the size of 240 x 180
        SIZE = HEIGHT, WIDTH = 1280, 720
        self.screen = pygame.display.set_mode(SIZE)
         
        # define a variable to control the main loop
        self.running = True

    def setup(self):
        self.deck = Deck() # deck constructor creates the quiddler deck
        self.hand = self.deck.draw(5) # first hand is 3 cards
        self.discard = self.deck.draw(1)
        for card in self.discard:
            card.bring_to_top()
            card.rect.x = Game.DISCARD[0]
        for i in range(len(self.hand)):
            card = self.hand[i]
            card.rect.y = 530
            card.rect.x = 300 +(i*110)
            
        self.sprites = self.deck.card_list + self.hand + self.discard
        self.mode = "draw"

        self.discard_select = None

        # initially we have 3 one letter words.
        self.word_stacks = [[self.hand[0]], [self.hand[1]], [self.hand[2]]]

    def update_fps(self):
        fps = str(int(self.clock.get_fps()))
        fps_text = self.fps_font.render(fps, 1, pygame.Color("coral"))
        return fps_text

    def handle_mouse_down(self, event):
        # find all cards that collide with the mouse location
        collided_sprites = []
        for sprite in self.sprites:
            if sprite in self.hand and sprite.rect.collidepoint(event.pos):
                collided_sprites.append(sprite)
        # if no cards are selected then skip this event loop
        if len(collided_sprites) == 0: return

        # find top z indexed card and drag that one around
        sprite = max(collided_sprites,key= lambda card: card.z) 
        if self.mode == "discard":
            self.discard_select = sprite
        else: # all other modes are "drag"
            sprite.dragging = True
            sprite.bring_to_top()
            mouse_x, mouse_y = event.pos
            sprite.offset_x = sprite.rect.x - mouse_x
            sprite.offset_y = sprite.rect.y - mouse_y
            
            #remove this card from its stack
            for word in self.word_stacks:
                if sprite in word:
                    word.remove(sprite)
                if len(word) == 0:
                    self.word_stacks.remove(word)
            self.word_stacks.append([sprite])

    def handle_mouse_up(self, event):
        print(pygame.mouse.get_pos())
        for sprite in self.sprites:
            if not sprite.dragging:
                continue
            sprite.dragging = False
            # now sprite is the one we just finished dragging
            collided_sprites = []
            for other_sprite in self.sprites:
                if not other_sprite == sprite and other_sprite in self.hand and other_sprite.rect.collidepoint(event.pos):
                    # here, other
                    collided_sprites.append(other_sprite)
            #collided sprites represent cards we placed another card on top of
            # look for a "word" that contains a card from collided sprites and add sprite to it
            if len(collided_sprites) == 0: return

            for word in self.word_stacks:
                if sprite in word:
                    word.remove(sprite)
                    if len(word) == 0:
                        self.word_stacks.remove(word)
                if collided_sprites[0] in word:
                    last_card_in_word = word[-1]
                    word.append(sprite)
                    card_to_move = sprite
                    card_to_move.rect.x = last_card_in_word.rect.x + 40
                    card_to_move.rect.y = last_card_in_word.rect.y

        # DRAW FROM DECK OR DISCARD
        if self.mode == "draw":
            if len(self.deck.card_list) > 0 and self.deck.card_list[0].rect.collidepoint(event.pos):
                card_to_draw = self.deck.draw()[0]
                card_to_draw.rect.y += 150
                self.hand.append(card_to_draw)
                self.mode = "drag"
                self.word_stacks.append([card_to_draw])

            elif len(self.discard) > 0 and self.discard[0].rect.collidepoint(event.pos):
                card_to_draw = self.discard.pop()
                card_to_draw.rect.y += 150
                self.hand.append(card_to_draw)
                self.mode = "drag"
                self.word_stacks.append([card_to_draw])

    def handle_mouse_moved(self, event):
        for sprite in self.sprites:
            if sprite.dragging:
                mouse_x, mouse_y = event.pos
                sprite.rect.x = mouse_x + sprite.offset_x
                sprite.rect.y = mouse_y + sprite.offset_y

    def handle_key_up(self, event):
        if event.key == pygame.K_r:
            self.setup()
        elif event.key == pygame.K_x:
            if self.mode == "discard" and self.discard_select is not None:
                card = self.discard_select
                self.hand.remove(self.discard_select)
                self.discard.append(self.discard_select)
                self.discard_select.rect.x = Game.DISCARD[0]
                self.discard_select.rect.y = Game.DISCARD[1]
                self.mode = "draw"
                self.discard_select = None
                for word in self.word_stacks:
                    if card in word:
                        word.remove(card)
                    if len(word) == 0:
                        self.word_stacks.remove(word)
            else:
                self.mode = "discard"
        elif event.key == pygame.K_RETURN:
            if self.mode == "draw":
                print("trying to go out with ", self.word_stacks)

    # main game function
    def run(self):

        #card1 = Card("A", 200, 200)
        self.setup()


        # keep a list of stacks of indices of cards in hand

        while self.running: # main loop

#---------------------------------------------------------------
# EVENT HANDLING
#---------------------------------------------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                # LEFT MOUSE BUTTON DOWN
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.handle_mouse_down(event)
                # LEFT MOUSE BUTTON UP
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.handle_mouse_up(event)
                elif event.type == pygame.MOUSEMOTION:
                    self.handle_mouse_moved(event)
                elif event.type == pygame.KEYUP:
                    self.handle_key_up(event)
#---------------------------------------------------------------------
# RENDERING
#-------------------------------------------------------------

            self.screen.fill((70,70,70))
            self.clock.tick(60)

            # render cards in z-index order
            for sprite in sorted(self.sprites, key= lambda card: card.z):
                #render discard red box
                if self.discard_select == sprite:
                    r = sprite.rect
                    x = sprite.rect.x -10
                    y = sprite.rect.y -10
                    w = sprite.rect.w +20
                    h = sprite.rect.h +20
                    pygame.draw.rect(self.screen, (200, 0, 0), (x,y,w,h))

                sprite.draw(self.screen)

            self.screen.blit(self.update_fps(), (10,0))
            self.screen.blit(self.fps_font.render("Mode: "+self.mode, 1, pygame.Color("coral")), (500,0))
            pygame.display.flip()

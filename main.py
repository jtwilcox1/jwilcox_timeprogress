# File created by: JT Wilcox


# This file was created by: JT Wilcox
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: my friend Charlie
'''
My goal is:
to add a countdown timer 
'''

# import libs
import pygame as pg
import os
# import timer, setting, and sprites
from settings import *
from sprites import *
from timer import*
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# game class to pass props in sprites

class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        # sets up the screen the game will be displayed in
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # name
        pg.display.set_caption("my game")
        # used to track a certain amount of time
        self.clock = pg.time.Clock()
        # start of game loop
        self.running = True
        print(self.screen)
    def new(self):
        # starting a new game
        self.score = 0
        # imports sprites
        self.all_sprites = pg.sprite.Group()
        # imports platforms
        self.platforms = pg.sprite.Group()
        # import enemies
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        # the characteristics of each platform
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (WHITE), "normal")
        self.plat2 = Platform(200, 35, 200, 400, (WHITE), "normal")
        self.plat3 = Platform(100, 35, 500, 300, (WHITE), "normal")
        self.plat4 = Platform(150, 35, 150, 200, (WHITE), "normal")
        self.all_sprites.add(self.plat1)
        self.all_sprites.add(self.plat2)
        self.all_sprites.add(self.plat3)
        self.all_sprites.add(self.plat4)
        self.platforms.add(self.plat1)
        self.platforms.add(self.plat2)
        self.platforms.add(self.plat3)
        self.platforms.add(self.plat4)
        self.all_sprites.add(self.player)
        # screen = pg.display((500, 500))
        # the range in from 0-10
        for i in range(0,10):
            m = Mob(20,20,(0,255,0))
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.run()
    def run(self):
        self.playing = True
        # animations happen while game is running
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                # keybinds for how to control sprite
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def update(self):
        self.all_sprites.update()
        # explains what will happen when sprites collide
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)

        
# characteristics of what will happen when they hit
            if hits:
                if hits[0].variant == "dissapearing":
                    hits[0].kill()
                elif hits[0].variant == "icey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    PLAYER_FRICTION = 0
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0

    def draw(self):
        # color of background
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
        # attempting to make it so timer will display in actual game but have not fixed yet
    def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        screen.blit(text_surface, text_rect)
    draw_text("TIMER", 22, WHITE, WIDTH/2, HEIGHT/24)        
    
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)
    

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()
    

pg.quit()

    



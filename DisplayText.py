import sys
from random import choice, randrange
from string import ascii_letters
import pygame as pg

class DisplayText:

    def __init__(self):
        print('Contructor')
    def display(self,txt):
        pg.init()
        info = pg.display.Info()
        screen = pg.display.set_mode((info.current_w, info.current_h), pg.FULLSCREEN)
        screen_rect = screen.get_rect()
        font = pg.font.Font(None, 100)
        clock = pg.time.Clock()
        color = (randrange(256), randrange(256), randrange(256))
        txt = font.render(txt, True, color)
        timer = 10
        '''done = False
        while not done:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        done = True
                    '''
        timer -= 1
        # Update the text surface and color every 10 frames.
        if timer <= 0:
            timer = 10
            color = (randrange(256), randrange(256), randrange(256))
            txt = font.render(txt, True, color)

        screen.fill((30, 30, 30))
        screen.blit(txt, txt.get_rect(center=screen_rect.center))

        pg.display.flip()
        clock.tick(30)
        pg.quit()

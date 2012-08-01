""" lux obscura """

import sys
import os

from cocos.director import director
from cocos.layer import *
from cocos.scene import Scene
from cocos.scenes.transitions import *
from cocos.actions import *
from cocos.sprite import *
from cocos.menu import *
from cocos.text import *

import pyglet
from pyglet import gl, font
from pyglet.window import key
from states import playing
class Options(Menu):
    def _init_(self):
        super(Options, self).__init__('Lux Obscura - Options')
class MainMenu(Menu):
    def __init__(self):
        super( MainMenu, self).__init__('Lux Obscura') 


        # you can override the font that will be used for the title and the items
        # you can also override the font size and the colors. see menu.py for
        # more info
        self.font_title['font_name'] = 'Edit Undo Line BRK'
        self.font_title['font_size'] = 72
        self.font_title['color'] = (204,164,164,255)

        self.font_item['font_name'] = 'Edit Undo Line BRK',
        self.font_item['color'] = (32,16,32,255)
        self.font_item['font_size'] = 32
        self.font_item_selected['font_name'] = 'Edit Undo Line BRK'
        self.font_item_selected['color'] = (32,16,32,255)
        self.font_item_selected['font_size'] = 46


        # example: menus can be vertical aligned and horizontal aligned
        self.menu_anchor_y = CENTER
        self.menu_anchor_x = CENTER

        items = []

        items.append( MenuItem('New Game', self.on_new_game) )
        items.append( MenuItem('Options', self.on_options) )
        items.append( MenuItem('Scores', self.on_scores) )
        items.append( MenuItem('Quit', self.on_quit) )

        self.create_menu( items, shake(), shake_back() )
    def on_new_game(self):
        pass
    def on_options(self):
        pass
    def on_scores(self):
        pass
    def on_quit(self):
        pyglet.app.exit()

if __name__ == "__main__":
    director.init(resizable=True, caption='Lux Obscura', width=640, height=640)
    main=Scene()
    main.add( MultiplexLayer(
        MainMenu()
        ),
               z=1 )
    director.run(main)
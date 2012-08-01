""" lux obscura playing scene """

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

class Playing(Scene):
    def __init__(self):
        super( Playing, self).__init__('Lux Obscura - Playing') 
    def on_draw(self):
        pass

if __name__ == "__main__":
    director.init(resizable=True, caption='Lux Obscura', width=640, height=640)
    director.run()

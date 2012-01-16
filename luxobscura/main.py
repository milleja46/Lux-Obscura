""" lux obscura """

import spyral
import pygame as pg
SIZE = (640, 640)
BG_COLOR = (2, 255, 20)
colors = {}
images = {}
geom = {}
fonts = {}
strings = {}
menu_active = 0

class Game(spyral.scene.Scene):
    """
    A Scene represents a distinct state of your game. They could be menus,
    different subgames, or any other things which are mostly distinct.
    
    A Scene should define two methods, update and render.
    """
    def __init__(self):
        """
        The __init__ message for a scene should set up the camera(s) for the
        scene, and setup groups and other structures which are needed for the
        scene.
        """
        spyral.scene.Scene.__init__(self)
        self.camera = spyral.director.get_camera()
        # For simple games with no layers, using the root camera is fine
        # Anything more advanced will want to make new cameras on top of this
        self.group = spyral.sprite.Group(self.camera)
        bg = spyral.util.new_surface(SIZE)
        bg.fill(BG_COLOR)
        self.camera.set_background(bg)
        # More setup here
                
    def render(self):
        """
        The render function should call .draw() on the scene's group(s) and
        camera(s). Unless your game logic should be bound by framerate,
        logic should go elsewhere.
        """
        self.group.draw()
        self.camera.draw()
        
    def update(self, tick):
        """
        The update function should contain or call out to all the logic.
        Here is where group.update() should be called for the groups, where
        event handling should be taken care of, etc.
        """
        self.group.update()
class Menu(spyral.scene.Scene):
    def __init__(self):
        spyral.scene.Scene.__init__(self)
        self.camera = spyral.director.get_camera().make_child(virtual_size=geom['size'])
        self.group = spyral.sprite.Group(self.camera)
        self.inited = False
        
    def on_enter(self):
        if self.inited:
            return
        self.inited = True
        bg = spyral.util.new_surface(geom['size'])
        bg.fill(colors['bg'])
        self.camera.set_background(bg)
        self.menufont = pg.font.SysFont("None", 42)
        
        title = spyral.sprite.Sprite()
        title.image = images['menu_title']
        title.rect.top = 10
        title.rect.centerx = self.camera.get_rect().centerx
        
        self.newGame = spyral.sprite.Sprite()
        self.newGame.text = "  New Game"
        self.newGame.image = self.menufont.render(self.newGame.text, True, colors['menu'])
        self.newGame.rect.top = title.rect.bottom + 40
        self.newGame.rect.left = 190

        self.gameContinue = spyral.sprite.Sprite()
        self.gameContinue.text = "  Continue"
        self.gameContinue.image = self.menufont.render(self.gameContinue.text, True, colors['menu'])
        self.gameContinue.rect.top = self.newGame.rect.bottom + 5
        self.gameContinue.rect.left = 190

        self.options = spyral.sprite.Sprite()
        self.options.image = images['menu_Options']
        self.options.rect.top = self.gameContinue.rect.bottom +5
        self.options.rect.left = 190

        self.gameQuit =  spyral.sprite.Sprite()
        self.gameQuit.image = images['menu_Quit']
        self.gameQuit.rect.top = self.options.rect.bottom +5
        self.gameQuit.rect.left = 190

        
        self.group.add(title, self.newGame, self.gameContinue, self.options, self.gameQuit)
        self.active = 0
        
    def render(self):
        self.group.draw()
        spyral.director.get_camera().draw()
        if self.active == 0:
            self.newGame.text = "> New Game"
            self.newGame.image = self.menufont.render(self.newGame.text, True, colors['menu'])
        if self.active != 0:
            self.newGame.text = "  New Game"
            self.newGame.image = self.menufont.render(self.newGame.text, True, colors['menu'])
        if self.active == 1:
            self.gameContinue.text = "> Continue"
            self.gameContinue.image = self.menufont.render(self.gameContinue.text, True, colors['menu'])
        if self.active != 1:
            self.gameContinue.text = "  Continue"
            self.gameContinue.image = self.menufont.render(self.gameContinue.text, True, colors['menu'])
            
        strings['menu_Options'] = "Options"
        strings['menu_Quit'] = "Quit"
        self.group.update()

    def update(self, tick):
        global menu_active
        self.active = menu_active
        for ev in pg.event.get():
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_UP:
                    if menu_active < 0:
                        menu_active = 4
                    else:
                        menu_active =  menu_active - 1
                if ev.key == pg.K_UP:
                    if menu_active > 4:
                        menu_active = 0
                    else:
                        menu_active += 1
                if ev.key == pg.K_RETURN:
                    if menu_active == 0:
                        exit(0)
                        spyral.director.push(intro)
                    if menu_active == 1:
                        pass
                    if menu_active == 2:
                        pass
                    if menu_active == 3:
                        pass
                    if menu_active == 4:
                        exit(0)
            if ev.type == pg.QUIT:
                exit(0)
        
class intro(spyral.scene.Scene):
    def init(self):
        spyral.Scene.__init__(self)
    def on_exit(self):
        pass
    def on_enter(self):
        pass
    def render(self):
        pass
    def update(self):
        pass
class Playing(spyral.scene.Scene):
    def init(self):
        spyral.Scene.__init__(self)
    def on_exit(self):
        pass
    def on_enter(self):
        pass
    def render(self):
        pass
    def update(self):
        pass
class Paused(spyral.scene.Scene):
    def init(self):
        spyral.Scene.__init__(self)
    def on_exit(self):
        pass
    def on_enter(self):
        pass
    def render(self):
        pass
    def update(self):
        pass
class GameOver(spyral.scene.Scene):
    def init(self):
        spyral.Scene.__init__(self)
    def on_exit(self):
        pass
    def on_enter(self):
        pass
    def render(self):
        pass
    def update(self):
        pass
if __name__ == "__main__":
    spyral.init() # Always call spyral.init() first
    colors['bg'] = BG_COLOR
    colors['menu'] = (255, 255, 255)

    geom['size'] = SIZE
    geom['width'] =  640
    geom['height'] = 640
    geom['menu_title_font_size'] = int(.20*geom['height'])
    geom['menu_font_size'] = int(.12*geom['height'])

    strings['menu_title']= "Lux Obscura"
    strings['menu_newGame'] = "  New Game"
    strings['menu_gameContinue'] = "  Continue"
    strings['menu_Options'] = "  Options"
    strings['menu_Quit'] = "  Quit"

    fonts['menu'] = pg.font.SysFont(None, geom['menu_font_size'])
    fonts['menu_title'] = pg.font.SysFont(None, geom['menu_title_font_size'])


    images['menu_title'] = fonts['menu_title'].render(
                            strings['menu_title'],
                            True,
                            colors['menu'])
    images['menu_Options'] = fonts['menu'].render(
                              strings['menu_Options'],
                              True,
                              colors['menu'])
    images['menu_Quit'] = fonts['menu'].render(
                            strings['menu_Quit'],
                            True,
                            colors['menu'])
    
    spyral.director.init(SIZE) # the director is the manager for your scenes
    spyral.director.push(Menu()) # push means that this Game() instance is
                                 # on the stack to run
    spyral.director.run() # This will run your game. It will not return.

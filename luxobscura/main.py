""" lux obscura """

import spyral
import pygame as pg
SIZE = (640, 640)
BG_COLOR = (0, 0, 0)
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
        self.active = 0
        bg = pg.image.load("media/images/menu.png").convert()
        self.camera.set_background(bg)
        self.menufont = pg.font.SysFont("None", int(.12*640))
        self.menutitlefont = pg.font.SysFont("None", int(.20*640))
        self.menucolor = (0, 200, 25)
        
        self.title = spyral.sprite.Sprite()
        self.title.text = "Lux Obscura"
        self.title.image = self.menutitlefont.render(self.title.text, True, self.menucolor)
        self.title.rect.top = 10
        self.title.rect.centerx = self.camera.get_rect().centerx
        
        self.newGame = spyral.sprite.Sprite()
        self.newGame.text = "   New Game"
        self.newGame.image = self.menufont.render(self.newGame.text, True, self.menucolor)
        self.newGame.rect.top = self.title.rect.bottom + 70
        self.newGame.rect.left = 180

        self.gameContinue = spyral.sprite.Sprite()
        self.gameContinue.text = "   Continue"
        self.gameContinue.image = self.menufont.render(self.gameContinue.text, True, self.menucolor)
        self.gameContinue.rect.top = self.newGame.rect.bottom + 5
        self.gameContinue.rect.left = 180

        self.options = spyral.sprite.Sprite()
        self.options.text = "   Options"
        self.options.image = self.menufont.render(self.options.text, True, self.menucolor)
        self.options.rect.top = self.gameContinue.rect.bottom +5
        self.options.rect.left = 180

        self.gameQuit =  spyral.sprite.Sprite()
        self.gameQuit.text = "   Quit"
        self.gameQuit.image = self.menufont.render(self.gameQuit.text, True, self.menucolor)
        self.gameQuit.rect.top = self.options.rect.bottom +5
        self.gameQuit.rect.left = 180

        
        self.group.add(self.title, self.newGame, self.gameContinue, self.options, self.gameQuit)
        
    def render(self):
        self.group.draw()
        spyral.director.get_camera().draw()
        if self.active == 0:
            self.newGame.text = "> New Game"
            self.newGame.image = self.menufont.render(self.newGame.text, True, self.menucolor)
        if self.active != 0:
            self.newGame.text = "   New Game"
            self.newGame.image = self.menufont.render(self.newGame.text, True, self.menucolor)
        if self.active == 1:
            self.gameContinue.text = "> Continue"
            self.gameContinue.image = self.menufont.render(self.gameContinue.text, True, self.menucolor)
        if self.active != 1:
            self.gameContinue.text = "   Continue"
            self.gameContinue.image = self.menufont.render(self.gameContinue.text, True, self.menucolor)
        if self.active == 2:
            self.options.text = "> Options"
            self.options.image = self.menufont.render(self.options.text, True, self.menucolor)
        if self.active != 2:
            self.options.text = "   Options"
            self.options.image = self.menufont.render(self.options.text, True, self.menucolor)
        if self.active == 3:
            self.gameQuit.text = "> Quit"
            self.gameQuit.image = self.menufont.render(self.gameQuit.text, True, self.menucolor)
        if self.active != 3:
            self.gameQuit.text = "   Quit"
            self.gameQuit.image = self.menufont.render(self.gameQuit.text, True, self.menucolor)

    def update(self, tick):
        for ev in pg.event.get():
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_UP:
                    if self.active < 0:
                        self.active = 3
                    else:
                        self.active -= 1
                if ev.key == pg.K_DOWN:
                    if self.active > 3:
                        self.active = 0
                    else:
                        self.active += 1
                if ev.key == pg.K_RETURN:
                    if menu_active == 0:
                        spyral.director.push(intro())
                    if menu_active == 1:
                        pass
                    if menu_active == 2:
                        pass
                    if menu_active == 3:
                        pass
            if ev.type == pg.QUIT:
                exit(0)
        self.group.update()
    def on_exit(self):
        self.group.empty()
class intro(spyral.scene.Scene):
    def __init__(self):
        spyral.scene.Scene.__init__(self)
        self.camera = spyral.director.get_camera().make_child(virtual_size=geom['size'])
        self.group = spyral.sprite.Group(self.camera)
        self.inited = False
        
    def on_enter(self):
        if self.inited:
            return
        bg = spyral.util.new_surface(640, 640)
        bg.fill(BG_COLOR)
        self.camera.set_background(bg)
        self.inited = True
        self.player = spyral.sprite.Sprite()
        self.player.image = pg.image.load("media/images/player.png")
        self.player.rect.centerx = 320
        self.player.rect.centery = 320

        self.group.add(self.player)
    def render(self):
        self.group.draw()
        spyral.director.get_camera().draw()
    def update(self, tick):
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            self.player.rect.centerx -= 5
        if key[pg.K_RIGHT]:
            self.player.rect.centerx += 5
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                exit(0)
        self.group.update()
class level(object):
    def __init__(self):
        pass
    def runLevel(self):
        pass
    def getCurrent(self):
        pass
    def getNext(self):
        pass
    def enemyObjects(self):
        pass
    def friendObjects(self):
        pass
if __name__ == "__main__":
    spyral.init() # Always call spyral.init() first
    colors['bg'] = BG_COLOR
    colors['menu'] = (255, 255, 255)

    geom['size'] = SIZE
    geom['width'] =  640
    geom['height'] = 640

    spyral.director.init(SIZE) # the director is the manager for your scenes
    spyral.director.push(Menu()) # push means that this Game() instance is on the stack to run
    spyral.director.run() # This will run your game. It will not return.

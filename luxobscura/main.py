""" lux obscura """

import pygame
import spyral

SIZE = (640, 640)
BG_COLOR = (0, 0, 0)
colors = {}
images = {}
geom = {}
fonts = {}
strings = {}

class MenuItem(spyral.gui.MouseSprite):
    """gui.MenuItem
    MenuItem(text, item_id) : return menu_item

    text -> str; the display text.
    item_id -> int; the numeric ID; also the item_id attribute returned in the
        pygame event.
    
    This class is not intended to be used directly. Use PopupMenu instead,
    unless designing your own interface to this class.
    """
    
    def __init__(self, text, item_id, action):
        self.text = text
        self.item_id = item_id
        self.image = font.render(text, True, text_color)
        self.rect = self.image.get_rect()
        self.active = False
        self.render()
        self.action = action
    def render(self):
        if self.active:
            self.image = fonts['menu_item'].render(self.text,
                                                          True,
                                                          colors['menuitem_active'])
        else:
            self.image = fonts['menu_item'].render(self.text,
                                                   True,
                                                   colors['menuitem_inactive'])
    def on_click(self, ev):
        pass


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
        
        title = spyral.sprite.Sprite()
        title.image = images['menu_title']
        title.rect.top = 10
        title.rect.centerx = self.camera.get_rect().centerx
        
        newGame = spyral.gui.MouseSprite()
        newGame.image = images['menu_newGame']
        newGame.rect.top = title.rect.bottom + 40
        newGame.rect.centerx = self.camera.get_rect().centerx
        
        self.group.add(title, newGame)

        
    def render(self):
        self.group.draw()
        spyral.director.get_camera().draw()
        
    def update(self, tick):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    exit(0)
                spyral.director.push(Pong())
            if event.type == pygame.QUIT:
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

    geom['size'] = (640, 640)
    geom['width'] =  640
    geom['height'] = 640
    geom['menu_title_font_size'] = int(.20*geom['height'])
    geom['menu_font_size'] = int(.06*geom['height'])

    strings['menu_title']= "Lux Obscura"
    strings['menu_newGame'] = "New Game"

    fonts['menu'] = pygame.font.SysFont(None, geom['menu_font_size'])
    fonts['menu_title'] = pygame.font.SysFont(None, geom['menu_title_font_size'])


    images['menu_title'] = fonts['menu_title'].render(
                            strings['menu_title'],
                            True,
                            colors['menu'])
    images['menu_newGame'] = fonts['menu'].render(
                            strings['menu_newGame'],
                            True,
                            colors['menu'])
    
    spyral.director.init(SIZE) # the director is the manager for your scenes
    spyral.director.push(Menu()) # push means that this Game() instance is
                                 # on the stack to run
    spyral.director.run() # This will run your game. It will not return.

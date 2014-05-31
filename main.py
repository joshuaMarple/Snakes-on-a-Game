from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.image import Image, Texture
from kivy.graphics.instructions import Canvas
from kivy.graphics import Rectangle

from Player import Player
from Magic import Magic

import math
#see this space here? see how there's no global state? keep it that way.
#global functions are ok, so long as they don't add state


class Baddie(Widget):
    name = "baddie"

class Obstacle(Widget):
    name = "obstacle"

class Background(Widget):
    #needs no methods or other functions, so we just pass it
    #has to have a class, or else kivy throws a fit
    pass



class Game(Widget):

    player = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)
        self.add_widget(Obstacle(size = (10, 10))) #trial obstacle, I will formalize this code more later

    def on_touch_down(self, touch):
        target_x = touch.x + 25/2 #so that the middle of the magic hits the cursor
        target_y = touch.y + 25/2 #same as above
        #dammmmn son lookit that trig
        #and you thought high school math was worthless
        hyp = math.sqrt((target_y - self.player.center_y)**2 + (target_x - self.player.center_x)**2)
        r = math.asin((target_x - self.player.center_x)/hyp)
        x = math.sin(r)
        y = math.cos(r)
        if target_y - self.player.y < 0: #makes sure it goes in the right direction, screws up for some reason if i do the x axis too
            y *= -1
        self.add_widget(Magic(pos = self.player.pos, size = (25, 25), x_comp = x, y_comp = y))

    def fireMagic(self):
        pass

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None
    def _on_keyboard_down(self, _keyboard, keycode, text, modifiers):
        if keycode[1] == 'w':
            self.player.vel_y = 2
        elif keycode[1] == 's':
            self.player.vel_y = -2
        elif keycode[1] == 'a':
            self.player.vel_x = -2
        elif keycode[1] == 'd':
            self.player.vel_x = 2
        return True

    def _on_keyboard_up(self, _keyboard, keycode):
        if keycode[1] == 'w':
            self.player.vel_y = 0
        elif keycode[1] == 's':
            self.player.vel_y = 0
        elif keycode[1] == 'a':
            self.player.vel_x = 0
        elif keycode[1] == 'd':
            self.player.vel_x = 0
        return True

    def update(self, dt):
        #check to see if it collides with any obstacles
        self.player.update(self.children, self.width, self.height)
        for i in self.children:
            try:
                if i.remove == True:
                    self.remove_widget(i)
                #test if its colliding
                if i.name == "magic":
                    i.update(self.children, self.width, self.height)
            except AttributeError:
                pass

class testApp(App):
    def build(self):
        game = Game()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    testApp().run()
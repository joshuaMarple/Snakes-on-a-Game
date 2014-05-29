from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window

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

class Player(Widget):
    baddieTimer = 0
    health = NumericProperty(0)

    def update(self, widgets, parent_width, parent_height):

         #no escaping!
        if self.x < 0:
            self.x = 0
            self.vel_x = 0
        if self.right > parent_width:
            self.right = parent_width
            self.vel_x = 0
        if self.top > parent_height:
            self.top = parent_height
            self.vel_y = 0
        if self.y < 0:
            self.y = 0
            self.vel_y = 0
        #update the baddie timer
        if self.baddieTimer > 0:
            self.baddieTimer -= 1

        #so he can actually move
        #velocity makes for a much smoother movement than just incrementing position
        prev_x = self.center_x
        prev_y = self.center_y
        self.center_x += self.vel_x
        self.center_y += self.vel_y

        for i in widgets:
            try:
                #test if its colliding
                if self.collide_widget(i) and i.name == "obstacle":
                    new_x = self.center_x #try resetting the x value
                    self.center_x = prev_x
                    if self.collide_widget(i) and i.name== "obstacle":
                        self.center_y = prev_y #well, since it wasn't the x value, lets try y
                        self.center_x = new_x
                        if self.collide_widget(i) and i.name== "obstacle":
                            self.center_x = prev_x #holy shit, still colliding? must be both then
            except AttributeError:
                pass

        #check to see if player collides with baddies
        for i in widgets:
            try:
                #test if its colliding
                if self.collide_widget(i) and i.name == "baddie":
                    if self.baddieTimer == 0: #prevents him from getting damaged so quick
                        # print(self.source)
                        self.source = 'media/p1_hurt.png'
                        self.hurt(1)
                        self.baddieTimer = 120
                    new_x = self.center_x #try resetting the x value
                    self.center_x = prev_x
                    if self.collide_widget(i) and i.name== "baddie":
                        self.center_y = prev_y #well, since it wasn't the x value, lets try y
                        self.center_x = new_x
                        if self.collide_widget(i) and i.name== "baddie":
                            self.center_x = prev_x #holy shit, still colliding? must be both then
            except AttributeError:
                pass

    #for when he takes damage
    #pain should be a number
    def hurt(self, pain):
        self.health -= pain

class Game(Widget):

    player = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)
        self.add_widget(Obstacle(size = (10, 10))) #trial obstacle, I will formalize this code more later

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

class testApp(App):
    def build(self):
        game = Game()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    testApp().run()
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window

class Background(Widget):
    pass

class Player(Widget):
    health = NumericProperty(0)

class PongGame(Widget):
    secCounter = 0
    player = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(PongGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)
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
            # if(self.player.vel_y > 0):
            #     self.player.vel_y -= 1
            self.player.vel_y = 0
        elif keycode[1] == 's':
            # if(self.player.vel_y > 0):
            #     self.player.vel_y += 1
            self.player.vel_y = 0
        elif keycode[1] == 'a':
            # if(self.player.vel_x > 0):
            #     self.player.vel_x += 1
            self.player.vel_x = 0
        elif keycode[1] == 'd':
            # if(self.player.vel_x > 0):
                # self.player.vel_x -= 1
            self.player.vel_x = 0
        return True

    def update(self, dt):
        # secCounter = 0
        self.player.center_x += self.player.vel_x
        self.player.center_y += self.player.vel_y

        self.secCounter += 1
        # if self.secCounter == 60:
        #     if self.player.vel_x > 0:
        #         self.player.vel_x -= .5
        #     if self.player.vel_x < 0:
        #         self.player.vel_x += .5
        #     if self.player.vel_y > 0:
        #         self.player.vel_y -= .5
        #     if self.player.vel_y < 0:
        #         self.player.vel_y += .5   
        #     self.secCounter = 0 

        # self.ball.move()
        # self.player.x += 1
        #bounce of paddles
        # self.player1.bounce_ball(self.ball)
        # self.player2.bounce_ball(self.ball)

        #bounce ball off bottom or top
        # if (self.ball.y < self.y) or (self.ball.top > self.top):
        #     self.ball.velocity_y *= -1

        # #went of to a side to score point?
        # if self.ball.x < self.x:
        #     self.player2.score += 1
        #     self.serve_ball(vel=(4, 0))
        # if self.ball.x > self.width:
        #     self.player1.score += 1
        #     self.serve_ball(vel=(-4, 0))



class testApp(App):
    def build(self):
        game = PongGame()
        # game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    testApp().run()
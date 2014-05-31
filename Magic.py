from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty

class Magic(Widget):
    name = "magic"
    remove = False
    vel_x = 2
    vel_y = 2
    x_comp = NumericProperty(0)
    y_comp = NumericProperty(0)

    def update(self, widgets, parent_width, parent_height):
        self.x += self.x_comp * self.vel_x
        self.y += self.y_comp * self.vel_y

        if self.x < 0:
            self.remove = True
        if self.right > parent_width:
            self.remove = True
        if self.top > parent_height:
            self.remove = True
        if self.y < 0:
            self.remove = True
        for i in widgets:
            try:
                #test if its colliding
                if self.collide_widget(i) and i.name == "obstacle":
                    self.remove = True 
            except AttributeError:
                pass

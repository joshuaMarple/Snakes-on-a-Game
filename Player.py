from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty


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

                        #I cannot change his fucking image for anything. No clue why, and internet is no help

                        # print(self.source)
                        # new_texture = Image('media/p1_hurt.png').texture
                        # with self.canvas:
                        #     self.Rectangle = Rectangle(texture=new_texture, pos=self.pos, size=self.size)
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
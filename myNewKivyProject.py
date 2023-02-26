from kivy.app import App
from kivy.graphics.vertex_instructions import Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class FirstScreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/60)

    def on_size(self, *args):
        # print("on size : " + str(self.width) + ", " + str(self.height))
        self.ball.pos = (self.center_x-self.ball_size/2, self.height - self.height)

    def update(self, dt):
        # print("update")
        x, y = self.ball.pos

        #x += self.vx
        y += self.vy

        #  self.ball_size / self.width
        # self.vx = - self.vx
        if y > self.center_y:
            self.vy = 0
#        if y + self.ball_size > self.height:
#            y = self.height-self.ball_size
#            self.vy = -self.vy
#        if x + self.ball_size > self.width:
#            x = self.width-self.ball_size
#            self.vx = -self.vx
#        if y < 0:
#            y = 0
#            self.vy = -self.vy
#        if x < 0:
#            x = 0
#            self.vx = -self.vx

        self.ball.pos = (x, y)


class MyNewProjectApp(App):
    pass


MyNewProjectApp().run()

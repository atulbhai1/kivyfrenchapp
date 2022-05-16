import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.uix.image import Image
class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)
        self.points = ()
        with self.canvas:
            self.image = Image(source="clipart145323.png", pos=(0, 0), size=(50, 50))
    def on_touch_down(self, touch):
        print("mouse down", touch)
        self.image.pos = touch.pos
        self.points = self.points+touch.pos
        with self.canvas:
            Color(1, 0, 0, .5, mode='rgba')
            Line(points=self.points)
    def on_touch_move(self, touch):
        print("mouse move", touch)
        self.image.pos = touch.pos
        self.points = self.points + touch.pos
        with self.canvas:
            Color(1, 0, 0, .5, mode='rgba')
            Line(points=self.points)
    def on_touch_up(self, touch):
        print("mouse up", touch)
        self.points = ()


class CanvasApp(App):
    def build(self):
        return Touch()
if __name__ == "__main__":
    CanvasApp().run()
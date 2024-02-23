from kivy.uix.label import Label
from kivy.app import App
import kivy
from kivy.core.window import Window

kivy.require('1.0.6')  # replace with your current kivy version !
Window.size = (400, 200)


class MyApp(App):

    def build(self):
        return Label(text='Hello world', font_size='100px')


if __name__ == '__main__':
    MyApp().run()

from kivy.uix.label import Label
from kivy.app import App
import kivy
from kivy.core.window import Window
from kivy.uix.button import Button
# https://kivy.org/doc/stable/api-kivy.uix.button.html
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.0.6')  # replace with your current kivy version !
Window.size = (400, 200)


class MyApp(App):

    def build(self):
        self.box = BoxLayout(orientation='vertical', spacing=20)
        self.label = Label(text='Hello world', font_size='30px')
        self.button = Button(
            text='click',
            size=(200, 100),
            size_hint=(None, None),
            background_color=(1, 0, 0, 1),
            border = (5,5,5,5)
        )
        self.box.add_widget(self.label)
        self.box.add_widget(self.button)
        return self.box


if __name__ == '__main__':
    MyApp().run()

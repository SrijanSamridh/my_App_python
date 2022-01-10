import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout


class MyLayout(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label())
        self.Image = self.add_widget(AsyncImage(source="IMG_20190808_021142_180.jpg",
                                                pos=(0.5, 0.5),
                                                ))
        self.add_widget(Label())
        self.greeting = Label(
            text="What's your name?",
            font_size=28,
            color='#00FFCE',
        )
        self.add_widget(self.greeting)

        # self.add_widget(Button(text="Click Here 1"))
        self.Text = TextInput(multiline=False, hint_text="Name", padding=8, size_hint=(.2, .3))
        self.add_widget(self.Text)

        self.bottom_layout = GridLayout()
        self.bottom_layout = GridLayout()
        self.bottom_layout.cols = 2
        self.yes = Button(text="Yes!",
                          # color="#00FFCE",
                          size_hint=(.2, .2),
                          background_color="#00FFCE",
                          )

        self.yes.bind(on_press=self.callBack)
        self.bottom_layout.add_widget(self.yes)

        self.bottom_layout.add_widget(Button(text="No!",
                                             size_hint=(.2, .2),
                                             background_color="#FF0000"))

        self.add_widget(self.bottom_layout)
        self.add_widget(Label())

    def callBack(self, instance):
        self.greeting.text = "Hello " + self.Text.text + "!!"
        print("Callback was called!!")

    def refresh(self, instance):
        return MyLayout()


class MyApplication(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        # return Label(text="This is my first kivy App!!!")
        return MyLayout()

    def on_start(self):
        print("This method is fired on start!!")

    def on_stop(self):
        print("This method is fired on end!!")


if __name__ == '__main__':
    MyApplication().run()

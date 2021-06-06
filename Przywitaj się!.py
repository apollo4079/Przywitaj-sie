from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        #zwracam okno aplikacji z widgetami
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # obrazek
        self.window.add_widget(Image(source="logo.png"))

        # etykieta
        self.greeting = Label(
                        text= "Jak masz na imię?",
                        font_size= 18,
                        color= '#00FFCE'
                        )
        self.window.add_widget(self.greeting)

        # wprowadzanie tekstu
        self.user = TextInput(
                    multiline= False,
                    padding_y= (20,20),
                    size_hint= (1, 0.5)
                    )

        self.window.add_widget(self.user)

        # przycisk
        self.button = Button(
                      text= "PRZYWITAJ",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#00FFCE',
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        self.greeting.text = "Witaj " + self.user.text + "!"

if __name__ == "__main__":
    SayHello().run()

from kivy.app import App
from kivy.uix.button import Button

class RechnerApp(App):
    pass

    def league(self,button,gui,app):
        for x in [self,button,gui,app]:
            print(x)
        if button.text == 'LoL':
            button.text='Das wars!'
            print("Das wars!")
        else:
            button.text = 'LoL'


    def discorde(self,button,gui,app):
        for x in [self,button,gui,app]:
            print(x)
        if button.text == 'Discord':
            button.text='Das wars!'
            print("Das wars!")
        else:
            button.text = 'Discord'

    def guilde(self,button,gui,app):
        for x in [self,button,gui,app]:
            print(x)
        if button.text == 'Guild Wars 2':
            button.text='Das wars!'
            print("Das wars!")
        else:
            button.text = 'Guild Wars 2'

    def button_pressed(self,button):
        print(button.text)
        print(self.root.ids)
        if self.root.ids.outputLabel.text == 'Willkommen':
            self.root.ids.outputLabel.text=button.text
        elif button.text == 'Leertaste':
            self.root.ids.outputLabel.text += ' '
        else:
            self.root.ids.outputLabel.text+= button.text

meineAnwendung=RechnerApp()
print(meineAnwendung)
RechnerApp().run()

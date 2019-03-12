from kivy.app import App
from kivy.uix.button import Button

class RechnerApp(App):
    pass

    def berechne(self,button,gui,app):
        print("LoL wird ausgeführt!")
        for x in [self,button,gui,app]:
            print(x)
        button.text='LoL ist fertig'
        print("Das wars!")

    def discorde(self,button,gui,app):
        print("Discord wird ausgeführt!")
        for x in [self,button,gui,app]:
            print(x)
        button.text='Discord ist fertig'
        print("Das wars!")

meineAnwendung=RechnerApp()
print(meineAnwendung)
RechnerApp().run()

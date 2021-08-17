# программа с двумя экранами
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
# Экран (объект класса Screen) - это виджет типа "макет" (Screen - наследник класса RelativeLayout).
# ScreenManager - это особый виджет, который делает видимым один из прописанных в нём экранов.

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        btn = Button(text="НЕТ")
        btn.on_press = self.next
        self.add_widget(btn) # экран - это виджет, на котором могут создаваться все другие (потомки)

    def next(self):
        self.manager.transition.direction = 'down' # объект класса Screen имеет свойство manager 
                                                   # - это ссылка на родителя
        self.manager.current = 'second'

def todo(dt):
    print("прошло",dt,"секунд")
    if random() > 0.9
        print()


class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        btn = Button(text="ДА")
        btn.on_press = self.next
        self.add_widget(btn)
        
    def next(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'first'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        # будет показан FirstScr, потому что он добавлен первым. Это можно поменять вот так:
        # sm.current = 'second'
        return sm

app = MyApp()
app.run()
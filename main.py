from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

Builder.load_file('frontend.kv')


class MainScreen(Screen):

    def start(self):
        pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()

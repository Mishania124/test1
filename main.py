from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
import sqlite3
import datetime

con = sqlite3.connect('identifier.sqlite')
cur = con.cursor()
cur.execute('SELECT * from test')

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

Builder.load_file('frontend.kv')


class MainScreen(Screen):

    def insert(self):
        cur.execute(f'INSERT INTO test (date) VALUES (\'{datetime.datetime.now()}\');')
        con.commit()
        cur.execute('SELECT * from test order by id desc limit 1')
        self.ids.time_label.text = cur.fetchone()[1]


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()

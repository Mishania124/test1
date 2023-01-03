from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
import requests
import json
import datetime
import mysql.connector

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
Builder.load_file('frontend.kv')
url = 'https://test-bd0b8-default-rtdb.europe-west1.firebasedatabase.app/'

result = requests.get(url + '.json')
data = json.loads(result.content.decode())
print(data)

class MainScreen(Screen):

    def insert(self):
        result = requests.get(url + 'test.json')
        data_count = len(json.loads(result.content.decode()))

        requests.patch(url+'test.json', data='{"'+str(data_count)+'": "'+str(datetime.datetime.now())+'"}')

        result = requests.get(url + 'test.json')

        all_data = json.loads(result.content.decode())
        self.ids.time_label.text = str(all_data[-1])


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()

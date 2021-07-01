# source kivy_venv/bin/activate

import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.video import Video

class TestScreen(GridLayout):

    def __init__(self, **kwargs):
        super(TestScreen, self).__init__(**kwargs)

class TestApp(App):

    def build(self):
        video = Video(source='test.m4v',state='play',options = {'eos': 'loop'})
        #video.allow_stretch=True
        return video
        #return TestScreen()

if __name__ == '__main__':
    TestApp().run()

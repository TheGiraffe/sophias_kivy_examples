import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty

class Screen1(Screen):
    pass
class Screen2(Screen):
    pass
class Screen3(Screen):
    pass
class Screen4(Screen):
    pass
class Screen5(Screen):
    pass
class Screen6(Screen):
    pass

class TestContainer(FloatLayout):
    karen = ScreenManager()
    screen = NumericProperty(1)

    def __init__(self, **kwargs):
        super(TestContainer, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self.start_keyboard()

    def start_keyboard(self):
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'right':
            if self.screen < 6:
                self.screen+=1
            else:
                self.screen = 1
            self.speak_to_the_manager()
        if keycode[1] == 'left':
            if self.screen > 1:
                self.screen-=1
            else:
                self.screen = 6
            self.speak_to_the_manager()
        return True

    def speak_to_the_manager(self):
        """Change screen, lol. Karen talks to herself, because she is the manager!"""
        self.karen.current = 'screen'+str(self.screen)

class ScreenmanagerApp(App):

    def build(self):
        return TestContainer()

if __name__ == '__main__':
    ScreenmanagerApp().run()

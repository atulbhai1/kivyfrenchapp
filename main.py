from kivy.lang import Builder
from kivy.app import App
from pygtranslate.translator import Translator
from kivy.uix.screenmanager import Screen, ScreenManager
translationInfo = {"To": None,"From": None, "FromText": None, "toText":None}
client = Translator()
class MainWindow(Screen):
    global translationInfo
    def translate(self):
        global translationInfo
        App.get_running_app().root.current = 'second'
        self.manager.transition.direction = "left"
        translationInfo['FromText'] = self.ids.toTranslate.text
        translationInfo['To'] = self.ids.translateInto.text
        translationInfo['From'] = self.ids.translateFrom.text
        translationInfo['toText'] = client.translate(translationInfo['FromText'], from_lang=translationInfo['From'], to_lang=translationInfo['To'])


class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass
kv = Builder.load_file("my.kv")
class MyApp(App):
    def build(self):
        return kv
if __name__ == "__main__":
    MyApp().run()
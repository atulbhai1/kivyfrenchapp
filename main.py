from kivy.lang import Builder
from kivy.app import App
from googletrans import Translator
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
translationInfo = {"To": None,"From": None, "FromText": None, "toText":None}
translator = Translator()
class P(FloatLayout):
    text = "An error occurred"
def show_popup():
    show = P()
    popupWindow = Popup(title="An error occurred", content=show, size_hint=(None, None), size=(400, 400))
    popupWindow.open()

class MainWindow(Screen):
    global translationInfo
    def translate(self):
        global translationInfo
        App.get_running_app().root.transition.direction = "left"
        translationInfo['FromText'] = self.ids.toTranslate.text
        translationInfo['To'] = self.ids.translateInto.text
        translationInfo['From'] = self.ids.translateFrom.text
        try:
            translationInfo['toText'] = translator.translate(translationInfo['FromText'], src=translationInfo['From'], dest=translationInfo['To']).text
        except Exception:
            show_popup()
        App.get_running_app().root.current = 'second'
        self.manager.get_screen('second').refreshInfo()
class SecondWindow(Screen):
    toShow = "Hi"
    global translationInfo
    def refreshInfo(self):
        global translationInfo
        self.fromLang = translationInfo['From']
        self.toLang = translationInfo['To']
        self.fromText = translationInfo['FromText']
        self.newText = translationInfo['toText']
        self.toShow = f'You translated "{self.fromText}"({self.fromLang}) into "{self.newText}"({self.toLang})'
        self.ids.theLabel.text = self.toShow
        translationInfo = {"To": None,"From": None, "FromText": None, "toText":None}
class ThirdWindow(Screen): pass
class WindowManager(ScreenManager):
    pass
kv = Builder.load_file("my.kv")
class MyApp(App):
    def build(self):
        return kv
if __name__ == "__main__":
    MyApp().run()
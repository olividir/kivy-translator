from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from googletrans import Translator


class Translate(GridLayout):

    def translate(self, *args):
        translator = Translator()
      

        translated = translator.translate(*args)
        self.lbl.text = translated.text

class LanguageApp(App):

    def build(self):
        return Translate()


langApp = LanguageApp()

if __name__ == '__main__':
    langApp.run()

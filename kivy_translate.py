from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from googletrans import Translator


class Translate(GridLayout):

    def translate(self, *args):
        translator = Translator()
        def trans(self, b):
            if b;
            try:
                self.prefix.text = str(b)
            except Exception:
                self.display.text = 'Error'

        translated = translator.translate(*args, dest=b)
        self.lbl.text = translated.text

class LanguageApp(App):

    def build(self):
        return Translate()


langApp = LanguageApp()

if __name__ == '__main__':
    langApp.run()
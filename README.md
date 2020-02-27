# kivy-translator
Kivy based translate program

This program is heavily influenced by emryscass and can be found here: https://github.com/emryscass/kivy-language-translation

Remember that this uses Kivy addons for python, more information on how to install Kivy can be found here: https://kivy.org/doc/stable/installation/installation-linux.html

I am currently working on making this app able to translate to every language. To have it translate to English, you will need to remove this from the "language.kv" file:



  TextInput:
            size_hint_x: 0.2
            id: trans
            text: ''
            


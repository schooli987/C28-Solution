from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
   
    def build(self):
        self.input = TextInput(text=" ",readonly=True, halign="right", font_size=40)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.input)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+',
         
        ]

        grid = GridLayout(cols=4)
        for b in buttons:
            grid.add_widget(Button(text=b, on_press=self.handle))
        layout.add_widget(grid)
        return layout

    def handle(self, instance):
        text = instance.text
        if text == 'C':
            self.input.text = ''
        else:
            self.input.text += text

if __name__ == '__main__':
    CalculatorApp().run()

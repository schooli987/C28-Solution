from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class BMICalculatorApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.weight_input = TextInput(hint_text="Enter weight in kg", font_size=30, input_filter='float')
        layout.add_widget(self.weight_input)

        self.height_input = TextInput(hint_text="Enter height in cm", font_size=30, input_filter='float')
        layout.add_widget(self.height_input)

        self.calculate_btn = Button(text="Calculate BMI")
        self.calculate_btn.bind(on_press=self.calculate_bmi)  # Bind button press
        layout.add_widget(self.calculate_btn)

        self.result_label = Label(text="BMI: ", font_size=30, size_hint=(1, 0.2))
        layout.add_widget(self.result_label)

        return layout

    def calculate_bmi(self, instance):
        try:
            weight = float(self.weight_input.text)
            height_cm = float(self.height_input.text)
            height_m = height_cm / 100

            bmi = weight / (height_m ** 2)
            category = self.get_bmi_category(bmi)

            self.result_label.text = f"BMI: {bmi:.2f} - {category}"
        except:
            self.result_label.text = "Please enter valid numbers for weight and height."
        
if __name__ == "__main__":
    BMICalculatorApp().run()

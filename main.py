from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from generator import generate_constants
from model import model_operation
from result import compare_results, save_results_to_file


class ArithmeticApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.username_input = TextInput(hint_text='Введите ФИО пользователя', multiline=False)
        self.layout.add_widget(self.username_input)

        self.run_number_input = TextInput(hint_text='Введите № прогона', multiline=False)
        self.layout.add_widget(self.run_number_input)

        self.seed_input = TextInput(hint_text='Введите seed для ГСЧ', multiline=False)
        self.layout.add_widget(self.seed_input)

        self.generate_button = Button(text='Сгенерировать данные')
        self.generate_button.bind(on_press=self.generate_data)
        self.layout.add_widget(self.generate_button)

        self.result_label = Label(text='Результаты будут здесь')
        self.layout.add_widget(self.result_label)

        self.operation_input = TextInput(hint_text='Введите операцию (+, -, *, /)', multiline=False)
        self.layout.add_widget(self.operation_input)

        self.run_button = Button(text='Запуск модели')
        self.run_button.bind(on_press=self.run_model)
        self.layout.add_widget(self.run_button)

        self.output_label = Label(text='Выходные данные')
        self.layout.add_widget(self.output_label)

        return self.layout

    def generate_data(self, instance):
        seed = int(self.seed_input.text)
        self.constants = generate_constants(seed)
        self.inputs = [(self.constants['a'], self.constants['b']), (self.constants['b'], self.constants['c'])]
        self.result_label.text = f"Сгенерированные данные: {self.inputs}"

    def run_model(self, instance):
        operation = self.operation_input.text
        model_results = model_operation(self.inputs, operation)

        user_results = [int(x) for x in self.run_number_input.text.split()]
        comparison_results = compare_results(user_results, model_results)

        self.output_label.text = f"Результаты: {model_results}\nСравнение: {comparison_results}"

        save_results_to_file('results.txt', user_results, model_results, comparison_results)


if __name__ == '__main__':
    ArithmeticApp().run()

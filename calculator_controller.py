from calculator_view import CalculatorView
from calculator_model import CalculatorModel


class CalculatorController:
    def __init__(self, calculate_model: CalculatorModel, calculate_view: CalculatorView):
        self.calculate_model = calculate_model
        self.calculate_view = calculate_view
        self.bind_button()

    def bind_button(self):
        self.calculate_view.keypad.bind('<Button>', self.handler)
        self.calculate_view.operator_pad.bind('<Button>', self.handler)
        self.calculate_view.math_func.bind('<<ComboboxSelected>>', self.func_handler)
        self.calculate_view.history.bind('<Motion>', self.calculate_view.show_history)
        self.calculate_view.history_menu.bind('<<ComboboxSelected>>', self.calculate_model.history_recall)
        self.calculate_view.history_menu.bind('<Leave>', self.calculate_view.hide_history)
        self.calculate_view.delete.bind('<Button>', self.calculate_model.delete)
        self.calculate_view.clr.bind('<Button>', self.clear)

    def handler(self, event):
        text = str(self.calculate_view.display['text']) + event.widget['text']
        if text[-1] == '=':
            self.calculate_model.calculate()
            return
        self.calculate_view.display.config(text=text, fg='yellow')

    def func_handler(self, event):
        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        choice = self.calculate_view.math_func.get()
        text = str(self.calculate_view.display['text'])
        check = text[-1] if text else None
        if not text or check in self.calculate_view.operator:
            text += choice + '('
            self.calculate_view.display.config(text=text, fg='yellow')
        elif check in num:
            new = choice + '(' + text + ')'
            self.calculate_view.display.config(text=new, fg='yellow')

    def clear(self, event):
        self.calculate_view.display.config(text='', fg='yellow')

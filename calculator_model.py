import math
from math import *


class CalculatorModel:
    def __init__(self, view):
        self.history = []
        self.view = view

    def calculate(self):
        text = self.view.display['text']
        text = text.replace('sin', 'math.sin')
        text = text.replace('cos', 'math.cos')
        text = text.replace('tan', 'math.tan')
        text = text.replace('log', 'math.log')
        text = text.replace('ln', 'math.log')
        try:
            result = eval(text)
            history = self.view.display['text'] + '=' + str(result)
        except Exception:
            result = "Invalid Result"
            self.view.display.config(text=result, fg='red')
            self.view.sound.play()
            return
        self.view.display.config(text=result, fg='yellow')
        self.view.all_history.append(history)
        self.view.history_menu['values'] = self.view.all_history

    def history_recall(self, event):
        recall = self.view.history_menu.get()
        n = 0
        for key in recall:
            n += 1
            if key == '=':
                recall = recall[:n-1]
        self.view.display.config(text=recall)

    def delete(self, event):
        text = str(self.view.display['text'])
        if not text:
            return

        check = text[-1]
        if check.isalpha():
            i = len(text) - 1
            while i >= 0 and text[i].isalpha():
                i -= 1
            text = text[:i + 1]
        else:
            text = text[:-1]
        self.view.display.config(text=text)

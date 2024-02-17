import math
from keypad import Keypad
import tkinter as tk
from tkinter import ttk
from math import *
import pygame


class CalculatorUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.geometry('325x300')
        self.display = tk.Label(self, text='', bg='black', fg='yellow', font=('monospace', 30), anchor=tk.E)
        self.history = tk.Label(self, text='', bg='lightgrey', fg='grey', font=('monospace', 15), anchor=tk.E)
        self.keypad = Keypad(self, list('789456123 0.'), 3)
        self.operator = ['(', ')', '*', '/', '+', '-', '^', '=']
        self.operator_pad = Keypad(self, self.operator, 2)
        self.clr = tk.Button(self, text='CLR', command=self.clear)
        self.delete = tk.Button(self, text='DEL', command=self.delete)
        self.math_func = ttk.Combobox(self)
        self.sound = None
        self.init_component()

    def init_component(self):
        self.keypad.bind('<Button>', self.handler)
        self.operator_pad.bind('<Button>', self.handler)
        self.math_func.bind('<<ComboboxSelected>>', self.func_handler)
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound('notification_sound.mp3')

        self.history.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.display.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.math_func['value'] = ['exp', 'ln', 'log', 'log2', 'sqrt', 'sin', 'cos', 'tan']
        self.math_func.config(width=6, height=15)
        self.math_func.pack(side=tk.TOP, anchor=tk.CENTER, padx=5, expand=True, fill=tk.BOTH)
        self.clr.config(width=3, height=2)
        self.clr.pack(side=tk.TOP, anchor=tk.W, expand=True, fill=tk.BOTH, pady=5)
        self.delete.config(width=3, height=2)
        self.delete.pack(side=tk.RIGHT, anchor=tk.W, expand=True, fill=tk.BOTH, pady=5)
        self.keypad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.operator_pad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

    def handler(self, event):
        text = str(self.display['text']) + event.widget['text']
        if text[-1] == '=':
            self.calculate()
            return
        self.display.config(text=text, fg='yellow')

    def func_handler(self, event):
        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        choice = self.math_func.get()
        text = self.display['text']
        check = text[-1] if text else None
        if not text or check in self.operator:
            text += choice + '('
            self.display.config(text=text)
        elif check in num:
            new = choice + '(' + text + ')'
            self.display.config(text=new)

    def calculate(self):
        text = self.display['text']
        text = text.replace('sin', 'math.sin')
        text = text.replace('cos', 'math.cos')
        text = text.replace('tan', 'math.tan')
        text = text.replace('ln', 'math.log')
        text = text.replace('log', 'math.log10')
        try:
            result = eval(text)
            history = self.history['text'] + '\n' + text + '=' + str(result)
        except Exception:
            result = "Invalid Result"
            self.display.config(text=result, fg='red')
            self.sound.play()
            return
        self.display.config(text=result)
        self.history.config(text=history)

    def clear(self):
        self.display.config(text='', fg='yellow')

    def delete(self):
        text = str(self.display['text'])
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
        self.display.config(text=text)

    def run(self):
        self.mainloop()

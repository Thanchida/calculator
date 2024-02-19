import tkinter as tk
from keypad import Keypad
from tkinter import ttk
import pygame


class CalculatorView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.geometry('400x400')
        self.display = tk.Label(self, text='', bg='black', fg='yellow', font=('monospace', 30), anchor=tk.E)
        self.history = tk.Label(self, text='history', fg='grey', font=('monospace', 15), anchor=tk.W)
        self.history_menu = ttk.Combobox(self)
        self.all_history = []
        self.keypad = Keypad(self, list('789456123 0.'), 3)
        self.operator = ['(', ')', '*', '/', '+', '-', '^', '=']
        self.operator_pad = Keypad(self, self.operator, 2)
        self.clr = tk.Button(self, text='CLR')
        self.delete = tk.Button(self, text='DEL')
        self.math_func = ttk.Combobox(self)
        self.sound = None
        self.init_component()

    def init_component(self):
        self.history.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.display.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.math_func['value'] = ['exp', 'ln', 'log10', 'log2', 'sqrt', 'sin', 'cos', 'tan']
        self.math_func.config(width=6, height=15)
        self.math_func.pack(side=tk.TOP, anchor=tk.CENTER, padx=5, expand=True, fill=tk.BOTH)
        self.clr.config(width=3, height=2)
        self.clr.pack(side=tk.TOP, anchor=tk.W, expand=True, fill=tk.BOTH, pady=5)
        self.delete.config(width=3, height=2)
        self.delete.pack(side=tk.RIGHT, anchor=tk.W, expand=True, fill=tk.BOTH, pady=5)
        self.keypad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.operator_pad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound('error_sound.mp3')

    def show_history(self, event):
        self.history_menu.pack(side=tk.TOP, anchor=tk.E)

    def hide_history(self, event):
        self.history_menu.pack_forget()

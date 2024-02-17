import tkinter as tk
from tkinter import *


class Keypad(Frame):

    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        super().__init__(parent, **kwargs)
        # keynames and columns
        self.keynames = keynames
        self.parent = parent
        self.init_components(columns)

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        row_pad = len(self.keynames)//columns
        option = {'sticky': tk.NSEW}
        for key in range(len(self.keynames)):
            row = key // columns
            column = key % columns
            keypad = tk.Button(self, text=self.keynames[key], width=2, height=4)
            keypad.grid(row=row, column=column, padx=2, pady=4, **option)

        for i in range(columns):
            self.columnconfigure(i, weight=5)
        for j in range(row_pad):
            self.rowconfigure(j, weight=5)

    def bind(self, sequence=None, func=None, add=None):
        """Bind an event handler to an event sequence."""
        for w in self.winfo_children():
            w.bind(sequence, func)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for button in self.winfo_children():
            button[key] = value

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        for button in self.winfo_children():
            return button[key]

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """
        for button in self.winfo_children():
            button.configure(cnf, **kwargs)


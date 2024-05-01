# THIS IS GOING TO BE THE INTEGRATED DOCUMENT WITH THE
# KEYBOARD, OSCILLOSCOPE, and RECORD BUTTONS

import tkinter as tk
from Oscilloscope import OscilloscopeGUI

class PureToneKeyboard:
    def __init__(self, main):
        self.main = main
        self.main.title("Pure Tone Keyboard with Oscilloscope and Recording ")

        self.canvas_width = 700
        self.canvas_height = 500
        self.canvas = tk.Canvas(self.main, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()
        # Assign the oscilloscope visual to the main 
        self.oscilloscope_visual = OscilloscopeGUI()

window = tk.Tk()
oscilloscope_gui = PureToneKeyboard(window)
window.mainloop()
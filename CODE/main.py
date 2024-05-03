# THIS IS GOING TO BE THE INTEGRATED DOCUMENT WITH THE
# KEYBOARD, OSCILLOSCOPE, and RECORD BUTTONS
import tkinter
import tkinter as tk
import PySimpleGUI as sg  # Import PySimpleGUI
from Oscilloscope import OscilloscopeGUI  # Import OscilloscopeGUI from your file

import tkinter as tk
import PySimpleGUI as sg  # Import PySimpleGUI
from Oscilloscope import OscilloscopeGUI  # Import OscilloscopeGUI from your file

class PureToneKeyboard:
    def __init__(self, master):
        self.master = master
        self.on_screen = []
        self.notes = []
        self.master.title("Pure Tone Keyboard with Oscilloscope and Recording")
        self.master.geometry(f'{self.master.winfo_screenwidth() // 2}x{self.master.winfo_screenheight() // 1.5:.0f}')

        self.oscilloscope_frame = tk.Frame(self.master)
        self.oscilloscope_frame.pack()

        # Create an instance of OscilloscopeGUI
        self.oscilloscope_visual = OscilloscopeGUI()
        # Set the frame of the OscilloscopeGUI
        self.oscilloscope_visual.frame = self.oscilloscope_frame
        self.on_screen.append(self.oscilloscope_visual)

        # Create a canvas for other elements
        self.canvas_width = 700
        self.canvas_height = 500
        self.canvas = tk.Canvas(self.master, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

def main():
    window = tk.Tk()
    app = PureToneKeyboard(window)
    window.mainloop()

if __name__ == "__main__":
    main()

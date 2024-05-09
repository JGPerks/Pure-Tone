import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import PySimpleGUI as sg
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Oscilloscope import OscilloscopeGUI

# Initialize OscilloscopeGUI
oscilloscope_gui = OscilloscopeGUI()

# Create Tkinter window
psg_tk_window = tk.Tk()
psg_tk_window.title('Tkinter version')

# Convert PySimpleGUI to Tkinter widgets version
psg_tk_label = tk.Label(psg_tk_window, text='Tkinter Window of Oscilloscope')
psg_tk_label.pack()
progress = Progressbar(psg_tk_window, orient=HORIZONTAL, length=4000, mode='indeterminate')
progress.pack()
listen_button = tk.Button(psg_tk_window, text='Listen')
listen_button.pack()
stop_button = tk.Button(psg_tk_window, text='Stop')
stop_button.pack()
exit_button = tk.Button(psg_tk_window, text='Exit')
exit_button.pack()

# -----------------------------------------------------------
# # Original layout from the Oscilloscope class
oscilloscope_layout = [
    [sg.Canvas(key='figCanvas')],
    [sg.ProgressBar(4000, orientation='h', size=(60, 20), key='-PROG-')],
    [sg.Button('Listen'),
     sg.Button('Stop', disabled=True),
     sg.Button('Exit')]
]

# In the main part of your code, when using the layout
psg_window_layout = [
    [sg.Text('PySimpleGUI Window')],
    oscilloscope_layout,  # Use the layout directly
    # Add other elements here if needed
]

# Create PySimpleGUI window
psg_window = sg.Window('PySimpleGUI Window with Oscilloscope', layout=psg_window_layout)

# Set window positions
psg_window_location = (100, 100)  # Coordinates for PySimpleGUI window
tk_window_position = "+200+200"     # Coordinates for Tkinter window

# Finalize the PySimpleGUI window to access the TKroot
psg_window.finalize()

# Set PySimpleGUI window location // CAN ADJUST
psg_window.TKroot.geometry(f"+{psg_window_location[0]}+{psg_window_location[1]}")

# Set Tkinter window location
psg_tk_window.geometry(tk_window_position)

# Event loop for Tkinter window
psg_tk_window.mainloop()

# Event loop for PySimpleGUI window
while True:
    event, values = psg_window.read()
    if event == sg.WINDOW_CLOSED:
        break

# Close windows
psg_window.close()
psg_tk_window.destroy()

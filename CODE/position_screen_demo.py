import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import PySimpleGUI as sg
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Oscilloscope import OscilloscopeGUI

oscilloscope_gui = OscilloscopeGUI()
psg_tk_window = tk.Tk()
# # Progress bar widget
progress = Progressbar(psg_tk_window, orient=HORIZONTAL,
                       length=4000, mode='indeterminate')
canvas_tk = tk.Canvas(psg_tk_window)
listen_button = tk.Button(text='Button')
stop_button = tk.Button(text='Stop')
exit_button = tk.Button(text='Exit')
layout = [canvas_tk,progress,listen_button,stop_button,exit_button]
# Create PySimpleGUI window with layout including OscilloscopeGUI
# psg_tk_window = tk.Tk([canvas_tk,progress,listen_button,stop_button,exit_button])# Create Tkinter window
psg_tk_window.title('This is the Tkinter Window')
psg_tk_label = tk.Label(psg_tk_window, text='Tkinter Window')
psg_tk_label.pack()

# progress = tk.Progressbar(root, orient = tk.horizontal,
#               length = 4000, size=(60, 20), mode = 'determinate')

# tk_window('PySimpleGUI Window with Oscilloscope', layout=[
#     [sg.Text('PySimpleGUI Window')],
#     oscilloscope_gui.layout()  # Use layout of OscilloscopeGUI directly in the PySimpleGUI layout
# ])
# Finalize the window to access the TKroot
# psg_tk_window.finalize()

# Set window positions
psg_window_location = (100, 100)  # Coordinates for PySimpleGUI window
tk_window_position = "+200+200"     # Coordinates for Tkinter window

# Set PySimpleGUI window location
psg_tk_window.geometry(f"+{psg_window_location[0]}+{psg_window_location[1]}")

# Set Tkinter window location
psg_tk_window.geometry(tk_window_position)

# Event loop
while True:
    # event captures the event, such as button clicks of cancel or window closure.
    # values holds the current state of the input element with the key '-NAME-', which is the input field where the user can enter their name.
    event, values = psg_tk_window.read()
    if event == sg.WINDOW_CLOSED:
        break
# Close windows
psg_tk_window.close()
psg_tk_window.destroy()

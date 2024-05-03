# Use this file to test out imports for the sake of figuring out what does and doesn't work
# import os
#
# for i in os.listdir('Sound Files/Pure Keys'):
#     print('Sound Files/Pure Keys/' + i)

 # ----------------------------------------------------------------
import tkinter as tk
import PySimpleGUI as sg

def tkinter_window():
    root = tk.Tk()
    root.title("Tkinter Window")

    label = tk.Label(root, text="This is a tkinter label")
    label.pack()

    root.mainloop()

import tkinter as tk
import PySimpleGUI as sg

def pysimplegui_in_tkinter():
    window = tk.Tk()
    window.title("PySimpleGUI in Tkinter")

    # Define PySimpleGUI layout
    layout = [
        [sg.Text("This is a PySimpleGUI text element")],
        [sg.Button("PySimpleGUI Button")]
    ]

    # Create PySimpleGUI window within tkinter window
    sg_window = sg.Window("PySimpleGUI Window", layout, finalize=True, element_justification='center', location=(0,0), no_titlebar=True, alpha_channel=0.0, grab_anywhere=True, keep_on_top=True, disable_close=True, resizable=True)

    while True:
        event, values = sg_window.read(timeout=10)  # Update PySimpleGUI window
        if event == sg.WIN_CLOSED:  # Check if PySimpleGUI window is closed
            break

    sg_window.close()  # Close PySimpleGUI window
    window.destroy()  # Close tkinter window

pysimplegui_in_tkinter()

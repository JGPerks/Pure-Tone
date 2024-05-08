import PySimpleGUI as sg
import tkinter as tk

# Create PySimpleGUI window
psg_window = sg.Window('This is the PySimpleGUI Window', layout=[[sg.Text('PySimpleGUI Window')]])
# Finalize the window to access the TKroot
psg_window.finalize()
# Create Tkinter window
tk_window = tk.Tk()
tk_window.title('This is the Tkinter Window')
tk_label = tk.Label(tk_window, text='Tkinter Window')
tk_label.pack()

# Set window positions
psg_window_location = (100, 100)  # Coordinates for PySimpleGUI window
tk_window_position = "+200+200"     # Coordinates for Tkinter window

# Set PySimpleGUI window location
psg_window.TKroot.geometry(f"+{psg_window_location[0]}+{psg_window_location[1]}")

# Set Tkinter window location
tk_window.geometry(tk_window_position)

# Event loop
while True:
    # event captures the event, such as button clicks of cancel or window closure.
    # values holds the current state of the input element with the key '-NAME-', which is the input field where the user can enter their name.
    event, values = psg_window.read()
    if event == sg.WINDOW_CLOSED:
        break
# Close windows
psg_window.close()
tk_window.destroy()

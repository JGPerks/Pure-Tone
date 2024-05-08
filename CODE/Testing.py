# Use this file to test out imports for the sake of figuring out what does and doesn't work
# import os
#
# for i in os.listdir('Sound Files/Pure Keys'):
#     print('Sound Files/Pure Keys/' + i)

 # ----------------------------------------------------------------
# importing tkinter module
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
# import PySimpleGUI as sg
root = tk.Tk()
root.title("PySimpleGUI to Tkinter Window")
#
# label = tk.Label(root, text="This is a tkinter label")
# label.pack()
#
# # Progress bar widget
progress = Progressbar(root, orient=HORIZONTAL,
                       length=4000, mode='indeterminate')
# progress = tk.Progressbar(root, orient = tk.horizontal,
#               length = 4000, size=(60, 20), mode = 'determinate')
canvas_tk = tk.Canvas(root)
listen_button = tk.Button(text='Button')
stop_button = tk.Button(text='Stop')
exit_button = tk.Button(text='Exit')
layout = [canvas_tk,progress,listen_button,stop_button,exit_button],
#
# # self.layout = [[sg.Canvas(key='figCanvas')],
# #                   [sg.ProgressBar(4000, orientation='h', size=(60, 20), key='-PROG-')],
# #                   [sg.Button('Listen', font=self.AppFont),
# #                    sg.Button('Stop', font=self.AppFont, disabled=True),
# #                    sg.Button('Exit', font=self.AppFont)]]
#
#
# root.mainloop()

# -----------------------------------------------------------------------------------

#
# # creating tkinter window
# root = Tk()
#
# # Progress bar widget
# progress = Progressbar(root, orient=HORIZONTAL,
#                        length=100, mode='indeterminate')
#
#
# Function responsible for the updation
# of the progress bar value
def bar():
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 40
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 50
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 60
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 100
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 60
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 50
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 40
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 20
    root.update_idletasks()
    time.sleep(0.5)
    progress['value'] = 0


progress.pack(pady=10)

# This button will initialize
# the progress bar
Button(root, text='Start', command=bar).pack(pady=10)

# infinite loop
mainloop()

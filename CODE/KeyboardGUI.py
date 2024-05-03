# Importing library for parsing command-line arguments
import argparse
import threading

from playsound import playsound
import SoundGenerator
import time as t

# Importing Tkinter for GUI
import tkinter as tk
import tkinter.font as tkf

# Importing custom keyboard modules for Tkinter and layout
import keyboardlayout as kl
import keyboardlayout.tkinter as klt

import sounddevice as sd
import soundfile as sf
from tkinter import Button, Label, filedialog
# Import recording from stereo mix functionality
#import Recorder



# Defining variables for colors and key sizes
grey = '#bebebe'
dark_grey = '#414141'
key_size = 100

# Function creates visual keyboard
def get_keyboard(window: tk.Tk, layout_name: kl.LayoutName, key_info: kl.KeyInfo) -> klt.KeyboardLayout:
    # Defining keyboard information
    keyboard_info = kl.KeyboardInfo(
        position=(0, 0),
        padding=2,
        color=dark_grey
    )
    # Defining key sizes(width, height)
    letter_key_size = (key_size, key_size)

    # Creating keyboard layout
    keyboard_layout = klt.KeyboardLayout(
        layout_name,
        keyboard_info,
        letter_key_size,
        key_info,
        master=window
    )
    return keyboard_layout

# Function runs loop until window is closed
def run_until_user_closes_window(
    window: tk.Tk,
    keyboard: klt.KeyboardLayout,
    released_key_info: kl.KeyInfo,
):
    # Defines key pressed that will be lit up
    pressed_key_info = kl.KeyInfo(
        margin=14,
        color='black',
        txt_color='white',
        txt_font=tkf.Font(family='Arial', size=key_size//4),
        txt_padding=(key_size//6, key_size//10)
    )
    # Keeps track of dead key
    dead_key_pressed = False

    # Contains all dead keys
    dead_key_keys = {kl.Key.CIRCUMFLEX, kl.Key.DIACRATICAL}

# Function handles key release events
    def keyup(e):
        # Obtaining key information
        key = keyboard.get_key(e)
        channel = player.getChannel(key)
        player.stop(channel)
        # Verify key is part of virtual keyboard
        if key is None:
            return
        # Update appearance of the pressed key on the virtual keyboard
        keyboard.update_key(
            key, released_key_info)
        nonlocal dead_key_pressed
        # If a dead key was previously pressed and the released key is not a dead key then
        # reset the dead_key_pressed flag and update the appearance of the circumflex key
        if dead_key_pressed and key not in dead_key_keys:
            dead_key_pressed = False
            keyboard.update_key(
                kl.Key.CIRCUMFLEX, released_key_info)

#Function handles key press events
    def keydown(e):
        key = keyboard.get_key(e)
        keyNote = player.getKeyNote(key)
        channel = player.getChannel(key)
        if channel.get_busy() == False:
            player.play(keyNote, channel)
        if key is None:
            return
        keyboard.update_key(key, pressed_key_info)
        # If the pressed key is a dead key then set the dead_key_pressed flag to True
        if key in dead_key_keys:
            nonlocal dead_key_pressed
            dead_key_pressed = True

    # Bind key press and release events to the keyboard layout
    keyboard.bind("<KeyPress>", keydown)
    keyboard.bind("<KeyRelease>", keyup)
    # Focus_set has any keyboard input directed to the virtual keyboard
    keyboard.focus_set()
    # Runs the Tkinter event loop
    window.mainloop()


# Function creates example of visual keyboard
def keyboard_example(layout_name: kl.LayoutName):
    window = tk.Tk()
    window.resizable(False, False)

    # Defines key information
    key_info = kl.KeyInfo(
        margin=10,
        color=grey,
        txt_color=dark_grey,
        txt_font=tkf.Font(family='Arial', size=key_size//4),
        txt_padding=(key_size//6, key_size//10)
    )
    # Calls and creates virtual keyboard
    keyboard = get_keyboard(window, layout_name, key_info)

    button = Button(window, text="Record", command=recAudio)
    button.pack()
    # Runs Tkinter event loop until the user closes the window
    run_until_user_closes_window(window, keyboard, key_info)


def recAudio():
    def rec():
        #recorder = Recorder
        #recorder.startRecording()

#    threading.Thread(target=rec).start()
        print('test')

if __name__ == "__main__":
    # Creating an argument parser object
    player = SoundGenerator.BOBsHeart()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'layout_name',
        nargs='?',
        type=kl.LayoutName,
        default=kl.LayoutName.QWERTY,
        help='the layout_name to use'
    )
    args = parser.parse_args()
    # Creates keyboard example w/ layout_name
    keyboard_example(args.layout_name)
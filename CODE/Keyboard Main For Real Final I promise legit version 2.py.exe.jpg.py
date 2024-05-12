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

# DO NOT USE THIS LIBRARY FILE: [import keyboardlayout.tkinter as klt], use following line instead
import keayboardlayout_with_place_instead_pack as klt

import sounddevice as sd
import soundfile as sf
from tkinter import Button, Label, filedialog
# Import recording for stereo mix functionality
from Recorder import Recorder
from tkinter import simpledialog

from PIL import ImageTk, Image

# Defining variables for colors and key sizes
grey = '#bebebe'
dark_grey = '#414141'
key_size = 75


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
        txt_font=tkf.Font(family='Arial', size=key_size // 4),
        txt_padding=(key_size // 6, key_size // 10)
    )
    # Keeps track of dead key
    dead_key_pressed = False

    # Contains all dead keys
    dead_key_keys = {kl.Key.CIRCUMFLEX, kl.Key.DIACRATICAL}

    # Function handles key release events
    def keyup(e):
        # Obtaining key information
        key = keyboard.get_key(e)
        try:
            channel = player.getChannel(key)
            player.stop(channel)
        except KeyError:
            print()
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

    # Function handles key press events
    def keydown(e):
        key = keyboard.get_key(e)
        player.checkKey(key)
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
    window.resizable(True, True)
    window.minsize(window.winfo_screenwidth(), window.winfo_screenheight())

    # Defines key information
    key_info = kl.KeyInfo(
        margin=10,
        color=grey,
        txt_color=dark_grey,
        txt_font=tkf.Font(family='Arial', size=key_size // 4),
        txt_padding=(key_size // 6, key_size // 10)
    )
    # Calls and creates virtual keyboard
    keyboard = get_keyboard(window, layout_name, key_info)

    button = Button(window, text="Record", command=lambda: recAudio(button))
    button.pack()

    sine_image = Image.open("Wave Image Files\Sine Wave.PNG")
    sine_image = sine_image.resize((200, 200), Image.BILINEAR)
    sine_image = ImageTk.PhotoImage(sine_image)
    square_image = Image.open("Wave Image Files\Square Wave.PNG")
    square_image = square_image.resize((200, 200), Image.BILINEAR)
    square_image = ImageTk.PhotoImage(square_image)
    sawtooth_image = Image.open("Wave Image Files\Sawtooth Wave.PNG")
    sawtooth_image = sawtooth_image.resize((200, 200), Image.BILINEAR)
    sawtooth_image = ImageTk.PhotoImage(sawtooth_image)
    triangle_image = Image.open("Wave Image Files\Triangle Wave.PNG")
    triangle_image = triangle_image.resize((200, 200), Image.BILINEAR)
    triangle_image = ImageTk.PhotoImage(triangle_image)

    current_wave_upper = sine_image
    current_wave_lower = sine_image

    waves = {"sawtooth": "Sawtooth Wave.PNG", "sine": "Sine Wave.PNG", "square": "Square Wave.PNG",
             "triangle": "Triangle Wave.PNG"}
    wave_tuple = ("Sawtooth Wave.PNG", "Sine Wave.PNG", "Square Wave.PNG", "Triangle Wave.PNG")
    wave_images_tuple = (sine_image, square_image, sawtooth_image, triangle_image)


    upper_label = tk.Label(window, image=sine_image)
    upper_label.place(x=1125, y=0)

    # lower_photo = ImageTk.PhotoImage(square_image)

    lower_label = tk.Label(window, image=sine_image)
    lower_label.place(x=1125, y=200)

    # Runs Tkinter event loop until the user closes the window
    run_until_user_closes_window(window, keyboard, key_info)


def update_wave_image(position, file):
    # if position == upper/lower
    pass


def increment_wave_indicator(current_image):
    index = wave_images_tuple.index(current_image)
    index += 1
    index %= 3
    new_image = wave_tuple[index]

    return new_image


def decrement_wave_indicator(current_image):
    index = wave_images_tuple.index(current_image)
    index -= 1
    if index < 0:
        index = len(wave_images_tuple) - 1
    index %= 3
    new_image = wave_tuple[index]

    return new_image


def giveName():
    print("Unfinished")

def toggleButton(button):
    if recorder.live is True:
        button.config(text="Stop Recording", command=lambda: stopAudio(button))
    else:
        button.config(text="Record", command=lambda: recAudio(button))


<<<<<<< HEAD
# recorder = Recorder("BOB.wav")
# recorder = Recorder("BOB.wav.wav")
=======
>>>>>>> 1e322134a351bb793df5ac6c88efb6c10da476ca
recorder = Recorder()


def recAudio(button):
    name = simpledialog.askstring("Input", "What would you like to call this masterpiece: ")
    def rec():
        recorder.startRecording(name)

    threading.Thread(target=rec).start()
    toggleButton(button)

def stopAudio(button):
    def stopRec():
        recorder.stopRecording()

    threading.Thread(target=stopRec()).start()
    toggleButton(button)

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

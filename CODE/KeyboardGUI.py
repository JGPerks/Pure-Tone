# Importing library for parsing command-line arguments
import argparse

from playsound import playsound
import pygame
import time as t

# Importing Tkinter for GUI
import tkinter as tk
import tkinter.font as tkf

# Importing custom keyboard modules for Tkinter and layout
import keyboardlayout as kl
import keyboardlayout.tkinter as klt

class BOBsHeart:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(36)

        self.channels = {'Key.DIGIT_1': pygame.mixer.Channel(26),
                        'Key.DIGIT_2': pygame.mixer.Channel(27),
                        'Key.DIGIT_3': pygame.mixer.Channel(28),
                        'Key.DIGIT_4': pygame.mixer.Channel(29),
                        'Key.DIGIT_5': pygame.mixer.Channel(30),
                        'Key.DIGIT_6': pygame.mixer.Channel(31),
                        'Key.DIGIT_7': pygame.mixer.Channel(32),
                        'Key.DIGIT_8': pygame.mixer.Channel(33),
                        'Key.DIGIT_9': pygame.mixer.Channel(34),
                        'Key.DIGIT_0': pygame.mixer.Channel(35),
                        'Key.Q': pygame.mixer.Channel(0),
                        'Key.W': pygame.mixer.Channel(1),
                        'Key.E': pygame.mixer.Channel(2),
                        'Key.R': pygame.mixer.Channel(3),
                        'Key.T': pygame.mixer.Channel(4),
                        'Key.Y': pygame.mixer.Channel(5),
                        'Key.U': pygame.mixer.Channel(6),
                        'Key.I': pygame.mixer.Channel(7),
                        'Key.O': pygame.mixer.Channel(8),
                        'Key.P': pygame.mixer.Channel(9),
                        'Key.A': pygame.mixer.Channel(10),
                        'Key.S': pygame.mixer.Channel(11),
                        'Key.D': pygame.mixer.Channel(12),
                        'Key.F': pygame.mixer.Channel(13),
                        'Key.G': pygame.mixer.Channel(14),
                        'Key.H': pygame.mixer.Channel(15),
                        'Key.J': pygame.mixer.Channel(16),
                        'Key.K': pygame.mixer.Channel(17),
                        'Key.L': pygame.mixer.Channel(18),
                        'Key.Z': pygame.mixer.Channel(19),
                        'Key.X': pygame.mixer.Channel(20),
                        'Key.C': pygame.mixer.Channel(21),
                        'Key.V': pygame.mixer.Channel(22),
                        'Key.B': pygame.mixer.Channel(23),
                        'Key.N': pygame.mixer.Channel(24),
                        'Key.M': pygame.mixer.Channel(25)}

        self.keysounds = {'Key.DIGIT_1': 'Sound Files/Pure Keys/C3.wav',
                        'Key.DIGIT_2': 'Sound Files/Pure Keys/D3.wav',
                        'Key.DIGIT_3': 'Sound Files/Pure Keys/E3.wav',
                        'Key.DIGIT_4': 'Sound Files/Pure Keys/f3.wav',
                        'Key.DIGIT_5': 'Sound Files/Pure Keys/G3.wav',
                        'Key.DIGIT_6': 'Sound Files/Pure Keys/A3.wav',
                        'Key.DIGIT_7': 'Sound Files/Pure Keys/B3.wav',
                        'Key.DIGIT_8': 'Sound Files/Pure Keys/c4.wav',
                        'Key.DIGIT_9': 'Sound Files/Pure Keys/D4.wav',
                        'Key.DIGIT_0': 'Sound Files/Pure Keys/D4_2.wav',
                        'Key.Q': 'Sound Files/Pure Keys/F4.wav',
                        'Key.W': 'Sound Files/Pure Keys/G4.wav',
                        'Key.E': 'Sound Files/Pure Keys/B4.wav',
                        'Key.R': 'Sound Files/Pure Keys/',
                        'Key.T': 'Sound Files/Pure Keys/',
                        'Key.Y': 'Sound Files/Pure Keys/',
                        'Key.U': 'Sound Files/Pure Keys/',
                        'Key.I': 'Sound Files/Pure Keys/',
                        'Key.O': 'Sound Files/Pure Keys/',
                        'Key.P': 'Sound Files/Pure Keys/',
                        'Key.A': 'Sound Files/Pure Keys/',
                        'Key.S': 'Sound Files/Pure Keys/',
                        'Key.D': 'Sound Files/Pure Keys/',
                        'Key.F': 'Sound Files/Pure Keys/',
                        'Key.G': 'Sound Files/Pure Keys/',
                        'Key.H': 'Sound Files/Pure Keys/',
                        'Key.I': 'Sound Files/Pure Keys/',
                        'Key.J': 'Sound Files/Pure Keys/',
                        'Key.K': 'Sound Files/Pure Keys/',
                        'Key.L': 'Sound Files/Pure Keys/',
                        'Key.Z': 'Sound Files/Pure Keys/',
                        'Key.X': 'Sound Files/Pure Keys/',
                        'Key.C': 'Sound Files/Pure Keys/',
                        'Key.V': 'Sound Files/Pure Keys/',
                        'Key.B': 'Sound Files/Pure Keys/',
                        'Key.N': 'Sound Files/Pure Keys/',
                        'Key.M': 'Sound Files/Pure Keys/'}



    def getKeyNote(self, key):
        keyNote = self.keysounds[str(key)]
        return keyNote

    def getChannel(self, key):
        channel = self.channels[str(key)]
        return channel

    def play(self, sound, channel):
        channel.play(pygame.mixer.Sound(sound))

    def stop(self, channel):
        channel.fadeout(50)


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

    # Runs Tkinter event loop until the user closes the window
    run_until_user_closes_window(window, keyboard, key_info)


if __name__ == "__main__":
    # Creating an argument parser object
    player = BOBsHeart()
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

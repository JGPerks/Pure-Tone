# audio visualizer program that maps microphone inputs
# From https://medium.com/geekculture/real-time-audio-wave-visualization-in-python-b1c5b96e2d39

import PySimpleGUI as sg
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


""" Microphone waveform display with Pyaudio, Pyplot and PysimpleGUI """

# VARS CONSTS:
# Define dictionary
# Create variable names and then set each variable initially equal to false
# These data will plot and handle data
_VARS = {'window': False,
         'stream': False,
         'fig_agg': False,
         'pltFig': False,
         'xData': False,
         'yData': False,
         # Set audioData to an empty numPy array
         'audioData': np.array([])}

# pysimpleGUI INIT:
AppFont = 'Any 16'
# Set theme ('DarkTeal2')
sg.theme('DarkTeal2')
layout = [[sg.Canvas(key='figCanvas')], # Create Canvas
          [sg.ProgressBar(4000, orientation='h',
                          size=(60, 20), key='-PROG-')], # Create horizontal progress bar
          [sg.Button('Listen', font=AppFont), # Create Listen button
           sg.Button('Stop', font=AppFont, disabled=True),# Create Stop button
           sg.Button('Exit', font=AppFont)]]# Create Exit button
_VARS['window'] = sg.Window('Microphone Waveform Pyplot', #The window is then created and stored in the _VARS dictionary under the key 'window'
                            layout, finalize=True,
                            location=(400, 100)) # Screen location


# PyAudio INIT:
# In audio processing a chunk  refers to a segment of audio data that is processed/analyzed at a time
CHUNK = 1024  # Samples: 1024,  512, 256, 128
# the sampling rate, which is the number of samples per second
RATE = 44100  # Equivalent to Human Hearing at 40 kHz
INTERVAL = 1  # Sampling Interval in Seconds ie Interval to listen
TIMEOUT = 10  # In ms for the event loop
# initializes an instance of the PyAudio class, allowing the Python script to interact with the audio input/output devices on the system. This instance is stored in the variable pAud
pAud = pyaudio.PyAudio()

# \\  -------- PYPLOT -------- //


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def drawPlot():
    _VARS['pltFig'] = plt.figure()
    plt.plot(_VARS['xData'], _VARS['yData'], '--k')
    plt.ylim(-4000, 4000)
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])

# See also the following for alternatives to updating pyplot in a
# more performant way:
# https://stackoverflow.com/questions/4098131/how-to-update-a-plot-in-matplotlib


def updatePlot(data):
    _VARS['fig_agg'].get_tk_widget().forget()
    plt.cla()
    plt.clf()
    plt.plot(_VARS['xData'], data, '--k')
    plt.ylim(-4000, 4000)
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])

# \\  -------- PYPLOT -------- //

# FUNCTIONS:


def stop():
    if _VARS['stream']:
        _VARS['stream'].stop_stream()
        _VARS['stream'].close()
        _VARS['window']['-PROG-'].update(0)
        _VARS['window'].FindElement('Stop').Update(disabled=True)
        _VARS['window'].FindElement('Listen').Update(disabled=False)


def callback(in_data, frame_count, time_info, status):
    _VARS['audioData'] = np.frombuffer(in_data, dtype=np.int16)
    return (in_data, pyaudio.paContinue)


def listen():
    _VARS['window'].FindElement('Stop').Update(disabled=False)
    _VARS['window'].FindElement('Listen').Update(disabled=True)
    _VARS['stream'] = pAud.open(format=pyaudio.paInt16,
                                channels=1,
                                rate=RATE,
                                input=True,
                                frames_per_buffer=CHUNK,
                                stream_callback=callback)

    _VARS['stream'].start_stream()


# INIT Pyplot:
plt.style.use('ggplot')
_VARS['xData'] = np.linspace(0, CHUNK, num=CHUNK, dtype=int)
_VARS['yData'] = np.zeros(CHUNK)
drawPlot()


# MAIN LOOP
while True: # While True continuously check for events from PySimpleGUI window
    event, values = _VARS['window'].read(timeout=TIMEOUT) #use read() method to read events
    # If the "event" is sg.WIN_CLOSED(representing the window closed event) or if the 'Exit' button is clicked call stop()
    if event == sg.WIN_CLOSED or event == 'Exit':
        stop()
        pAud.terminate()
        break
    # If the "event" is listen then call listen function
    if event == 'Listen':
        listen()
    # If the "event" is Stop then call stop function
    elif event == 'Stop':
        stop()
    # If the size of the audioData array in _VARS is not zero
    elif _VARS['audioData'].size != 0:
        # Update the progress bar with the MAX value in the 'audioData' array
        _VARS['window']['-PROG-'].update(np.amax(_VARS['audioData']))
        # Update the plot using updatePlot() function
        updatePlot(_VARS['audioData'])

_VARS['window'].close()

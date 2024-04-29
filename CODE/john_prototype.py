# audio visualizer program that maps microphone inputs
# From https://medium.com/geekculture/real-time-audio-wave-visualization-in-python-b1c5b96e2d39

import PySimpleGUI as sg
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


""" Microphone waveform display with Pyaudio, Pyplot and PysimpleGUI """

# VARS CONSTS:
_VARS = {'window': False,
         'stream': False,
         'fig_agg': False,
         'pltFig': False,
         'xData': False,
         'yData': False,
         'audioData': np.array([])}

# pysimpleGUI INIT:
AppFont = 'Any 16'
sg.theme('DarkTeal2')
layout = [[sg.Canvas(key='figCanvas')],
          [sg.ProgressBar(4000, orientation='h',
                          size=(60, 20), key='-PROG-')],
          [sg.Button('Listen', font=AppFont),
           sg.Button('Stop', font=AppFont, disabled=True),
           sg.Button('Exit', font=AppFont)]]
_VARS['window'] = sg.Window('Microphone Waveform Pyplot',
                            layout, finalize=True,
                            location=(400, 100))


# PyAudio INIT:
CHUNK = 1024  # Samples: 1024,  512, 256, 128
RATE = 44100  # Equivalent to Human Hearing at 40 kHz
INTERVAL = 1  # Sampling Interval in Seconds ie Interval to listen
TIMEOUT = 10  # In ms for the event loop
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
while True:
    event, values = _VARS['window'].read(timeout=TIMEOUT)
    if event == sg.WIN_CLOSED or event == 'Exit':
        stop()
        pAud.terminate()
        break
    if event == 'Listen':
        listen()
    elif event == 'Stop':
        stop()
    elif _VARS['audioData'].size != 0:
        _VARS['window']['-PROG-'].update(np.amax(_VARS['audioData']))
        updatePlot(_VARS['audioData'])

_VARS['window'].close()

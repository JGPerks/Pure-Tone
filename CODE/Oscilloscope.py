# audio visualizer program that maps microphone inputs
# From https://medium.com/geekculture/real-time-audio-wave-visualization-in-python-b1c5b96e2d39

import PySimpleGUI as sg
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


""" Microphone waveform display with Pyaudio, Pyplot and PysimpleGUI """
class OscilloscopeGUI:
    def __init__(self):
        # VARS CONSTS:
        # Define dictionary
        # Create variable names and then set each variable initially equal to false
        # These data will plot and handle data
        self._VARS = {'window': False,
                      'stream': False,
                      'fig_agg': False,
                      'pltFig': False,
                      'xData': False,
                      'yData': False,
                      'audioData': np.array([])} # Set audioData to an empty numPy array
        # Determine the font and theme
        self.AppFont = 'Any 16'
        sg.theme('DarkTeal2')
        # Create the canvas, Create horizontal progress bar, Create Listen, Stop, and Exit buttons
        self.layout = [[sg.Canvas(key='figCanvas')],
                  [sg.ProgressBar(4000, orientation='h', size=(60, 20), key='-PROG-')],
                  [sg.Button('Listen', font=self.AppFont),
                   sg.Button('Stop', font=self.AppFont, disabled=True),
                   sg.Button('Exit', font=self.AppFont)]]
        # The window is then created and stored in the _VARS dictionary under the key 'window'
        self._VARS['window'] = sg.Window('Microphone Waveform Pyplot', self.layout, finalize=True, location=(400, 100))
        self.CHUNK = 1024
        self.RATE = 44100
        self.INTERVAL = 1
        self.TIMEOUT = 10
        self.pAud = pyaudio.PyAudio()

    def draw_figure(self, canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    def drawPlot(self):
        self._VARS['pltFig'] = plt.figure()
        plt.plot(self._VARS['xData'], self._VARS['yData'], '--k')
        plt.ylim(-4000, 4000)
        self._VARS['fig_agg'] = self.draw_figure(
            self._VARS['window']['figCanvas'].TKCanvas, self._VARS['pltFig'])
    def updatePlot(self, data):
        self._VARS['fig_agg'].get_tk_widget().forget()
        plt.cla()
        plt.clf()
        plt.plot(self._VARS['xData'], data, '--k')
        plt.ylim(-4000, 4000)
        self._VARS['fig_agg'] = self.draw_figure(
            self._VARS['window']['figCanvas'].TKCanvas, self._VARS['pltFig'])
    def run(self):
        while True:
            event, values = self._VARS['window'].read()
            if event == sg.WINDOW_CLOSED or event == 'Exit':
                break
    # FUNCTIONS:
    def stop(self):
        if self._VARS['stream']:
            self._VARS['stream'].stop_stream()
            self._VARS['stream'].close()
            self._VARS['window']['-PROG-'].update(0)
            self._VARS['window'].FindElement('Stop').Update(disabled=True)
            self._VARS['window'].FindElement('Listen').Update(disabled=False)

    def callback(self, in_data, frame_count, time_info, status):
        self._VARS['audioData'] = np.frombuffer(in_data, dtype=np.int16)
        return (in_data, pyaudio.paContinue)

    def listen(self):
        self._VARS['window'].FindElement('Stop').Update(disabled=False)
        self._VARS['window'].FindElement('Listen').Update(disabled=True)
        self._VARS['stream'] = self.pAud.open(format=pyaudio.paInt16,
                                    channels=1,
                                    rate=self.RATE,
                                    input=True,
                                    frames_per_buffer=self.CHUNK,
                                    stream_callback=self.callback)

        self._VARS['stream'].start_stream()

    # INIT Pyplot:
    def plot_things(self):
        plt.style.use('ggplot')
        self._VARS['xData'] = np.linspace(0, self.CHUNK, num=self.CHUNK, dtype=int)
        self._VARS['yData'] = np.zeros(self.CHUNK)
        self.drawPlot()

    # MAIN LOOP
    def run_oscilloscope(self):
        while True:  # While True continuously check for events from PySimpleGUI window
            event, values = self._VARS['window'].read(timeout=self.TIMEOUT)  # use read() method to read events
            # If the "event" is sg.WIN_CLOSED(representing the window closed event) or if the 'Exit' button is clicked call stop()
            if event == sg.WIN_CLOSED or event == 'Exit':
                self.stop()
                self.pAud.terminate()
                break
            # If the "event" is listen then call listen function
            if event == 'Listen':
                self.listen()
            # If the "event" is Stop then call stop function
            elif event == 'Stop':
                self.stop()
            # If the size of the audioData array in _VARS is not zero
            elif self._VARS['audioData'].size != 0:
                # Update the progress bar with the MAX value in the 'audioData' array
                self._VARS['window']['-PROG-'].update(np.amax(self._VARS['audioData']))
                # Update the plot using updatePlot() function
                self.updatePlot(self._VARS['audioData'])

        self._VARS['window'].close()
if __name__ == "__main__":
    software = OscilloscopeGUI()
    software.plot_things()
    software.run_oscilloscope()
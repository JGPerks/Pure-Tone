import numpy as np
import PySimpleGUI as sg
import pyaudio
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def fft_analysis(data, rate):
    """ Perform FFT analysis and return frequencies and their corresponding magnitudes """
    fft_result = np.fft.fft(data)
    freq = np.fft.fftfreq(len(data), 1.0 / rate)
    magnitude = np.abs(fft_result)
    return freq[:len(data) // 2], magnitude[:len(data) // 2]  # Return only positive frequencies

def detect_waveform_type(magnitude):
    """ Simple heuristic to detect waveform type based on FFT characteristics """
    # Thresholds and logic to determine waveform type will be simplistic and for demonstration
    peak = np.argmax(magnitude)
    if peak == 0:
        return "DC or Silence"
    elif np.allclose(magnitude[peak] / magnitude[1:peak], 1, atol=0.5):
        return "Square Wave"
    elif magnitude[1] > magnitude[2] * 2:
        return "Sine Wave"
    else:
        return "Complex or Noise"

def update_fft_plot(freq, magnitude, waveform_type):
    """ Update the plot with new FFT data """
    ax.clear()
    ax.semilogy(freq, magnitude)  # Log scale for magnitude
    ax.set_title(f"Detected Waveform: {waveform_type}")
    ax.set_xlim(0, RATE // 2)  # Display up to Nyquist frequency
    ax.set_ylim(1, max(magnitude) + 100)  # Avoid log(0) and adjust ylim dynamically
    fig_agg.draw()

# Initialize PyAudio and set constants
p = pyaudio.PyAudio()
CHUNK = 1024
RATE = 44100
FORMAT = pyaudio.paInt16
CHANNELS = 1

# Define GUI layout
layout = [
    [sg.Text('Real-Time Audio Waveform', font='Any 16')],
    [sg.Canvas(key='figCanvas')],
    [sg.Button('Start'), sg.Button('Stop', disabled=True), sg.Button('Exit')]
]

window = sg.Window('Real-Time Audio FFT', layout, finalize=True)

# Setup matplotlib figure and axes
fig, ax = plt.subplots()
fig_agg = FigureCanvasTkAgg(fig, window['figCanvas'].TKCanvas)
fig_agg.draw()
fig_agg.get_tk_widget().pack(side='top', fill='both', expand=1)

def callback(in_data, frame_count, time_info, status):
    """ Audio stream callback function """
    data = np.frombuffer(in_data, dtype=np.int16)
    freq, magnitude = fft_analysis(data, RATE)
    waveform_type = detect_waveform_type(magnitude)
    window.write_event_value('-FFT_UPDATE-', (freq, magnitude, waveform_type))
    return (in_data, pyaudio.paContinue)

# Event loop
stream = None
while True:
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Start':
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, frames_per_buffer=CHUNK,
                        input=True, stream_callback=callback)
        stream.start_stream()
        window['Stop'].update(disabled=False)
        window['Start'].update(disabled=True)
    elif event == 'Stop':
        if stream:
            stream.stop_stream()
            stream.close()
            stream = None
        window['Start'].update(disabled=False)
        window['Stop'].update(disabled=True)
    elif event == '-FFT_UPDATE-':
        freq, magnitude, waveform_type = values['-FFT_UPDATE-']
        update_fft_plot(freq, magnitude, waveform_type)

window.close()
p.terminate()

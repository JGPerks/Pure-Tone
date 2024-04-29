import tkinter as tk
from math import sin, pi

class Oscilloscope:
    def __init__(self, main):
        self.main = main
        self.main.title("Oscilloscope using Tkinter")

        self.canvas_width = 700
        self.canvas_height = 500
        self.canvas = tk.Canvas(self.main, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        self.start_button = tk.Button(self.main, text="START", command=self.start)
        self.start_button.pack()

        self.stop_button = tk.Button(self.main, text="END", command=self.stop)
        self.stop_button.pack()
        # Initially set running to false, don't want to run wave yet
        self.running = False
        # Can change these
        self.amplitude = 50
        self.frequency = 1
        self.phase = 0
        self.sample_rate = 100
        self.sample_interval = 1000 / self.sample_rate
        # Calls the function to update the plot
        self.update_plot()

    def start(self):
        self.running = True
        self.update_plot()

    def stop(self):
        self.running = False

    def update_plot(self):
        if self.running:
            self.canvas.delete("waveform")
            x_prev = 0
            y_prev = self.canvas_height / 2
            # For a sine wave
            for x in range(1, self.canvas_width):
                y = self.canvas_height / 2 - self.amplitude * sin(
                    (x / self.canvas_width) * (2 * pi * self.frequency) + self.phase)
                self.canvas.create_line(x_prev, y_prev, x, y, fill="red", tags="waveform")
                x_prev, y_prev = x, y
            self.main.after(int(self.sample_interval), self.update_plot)

window = tk.Tk()
oscilloscope_gui = Oscilloscope(window)
window.mainloop()


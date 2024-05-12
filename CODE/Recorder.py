import pyaudio
import wave
import time


class Recorder(pyaudio.PyAudio):
    def __init__(self):
        super().__init__()
        self.startTime = 0
        self.endTime = 0
        self.frames = None
        self.stream = None
        self.p = None
        self.found = False
        self.live = True
        self.chunk = 1024  # Record in chunks of 1024 samples
        self.sample_format = pyaudio.paInt16  # 16 bits per sample
        self.channels = 1
        self.rate = 44100  # Record at 44100 samples per second
        self.dev_index = 0
        self.filename = None

    def startRecording(self, name):
        # Create an interface to PortAudio
        self.p = pyaudio.PyAudio()
        self.live = True
        self.startTime = time.time()
        self.filename = "Saved Songs/" + name + ".wav"

        # Below finds your (Stereo Mix) index and auto assigns it, print statement is for testing purposes
        for i in range(self.p.get_device_count()):
            if "Stereo" in self.p.get_device_info_by_index(i).get("name") and self.found is False:
                self.dev_index = i
                self.found = True

        self.stream = self.p.open(format=self.sample_format,
                                  channels=self.channels,
                                  rate=self.rate,
                                  input_device_index=self.dev_index,
                                  frames_per_buffer=self.chunk,
                                  input=True)

        self.frames = []  # Initialize array to store frames

        print("Your (Stereo Mix) index is: " + str(self.dev_index))
        print('Recording')

        # Stores data in chunks for 210 seconds/3.5 minutes
        while self.live is True:
            if self.endTime - self.startTime < 210:
                data = self.stream.read(self.chunk)
                self.frames.append(data)
                self.endTime = time.time()
            else:
                self.live = False
                Recorder.stopRecording(self)

        # Added to exit early from recording

    def stopRecording(self):
        self.live = False
        # Stop and close the stream
        self.stream.stop_stream()
        self.stream.close()
        # Terminate the PortAudio interface
        self.p.terminate()

        print('Finished recording')

        # Save the recorded data as a WAV file
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()
